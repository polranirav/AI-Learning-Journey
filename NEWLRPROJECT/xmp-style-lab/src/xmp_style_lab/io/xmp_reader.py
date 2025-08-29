# src/xmp_style_lab/parsing/xmp_reader.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional
from lxml import etree
from pathlib import Path
import json
from datetime import datetime, timezone

CRS_NS = "http://ns.adobe.com/camera-raw-settings/1.0/"
RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
X_NS   = "adobe:ns:meta/"

NSMAP = {"crs": CRS_NS, "rdf": RDF_NS, "x": X_NS}

META_PREFIX = [
    "file_name",
    "relative_path",
    "collection",
    "format",
    "file_size_bytes",
    "mtime_iso",
    "id",
    "title",
    "internalName",
    "type",
    "x:xmptk",
]

def _coerce_scalar(val: Optional[str]):
    if val is None:
        return None
    s = str(val).strip()
    if s == "":
        return ""
    # strip leading '+'
    if s.startswith("+"):
        s = s[1:]
    # booleans
    low = s.lower()
    if low in ("true", "false"):
        return True if low == "true" else False
    # numbers
    try:
        if "." in s:
            return float(s)
        return int(s)
    except ValueError:
        return s

def _text_or_empty(el: etree._Element) -> str:
    t = el.text if el is not None else ""
    return "" if t is None else t

def _parse_rdf_alt(el: etree._Element) -> List[Dict[str, Optional[str]]]:
    items: List[Dict[str, Optional[str]]] = []
    for li in el.xpath("./rdf:Alt/rdf:li", namespaces=NSMAP):
        lang = li.get("{http://www.w3.org/XML/1998/namespace}lang")
        items.append({"_lang": lang or "x-default", "value": li.text})
    return items

def _parse_rdf_seq_strings(el: etree._Element) -> List[str]:
    vals: List[str] = []
    for li in el.xpath("./rdf:Seq/rdf:li", namespaces=NSMAP):
        txt = _text_or_empty(li)
        vals.append(txt)
    return vals

def _parse_curve_points(seq_strings: List[str]) -> List[Tuple[Optional[float], Optional[float]]]:
    pts: List[Tuple[Optional[float], Optional[float]]] = []
    for s in seq_strings:
        # common form "x, y" (with spaces). Fallback: "x,y" or "x  y"
        if "," in s:
            parts = [p.strip() for p in s.split(",")]
        else:
            parts = s.split()
        if len(parts) >= 2:
            try:
                x = float(parts[0])
                y = float(parts[1])
            except ValueError:
                x = _coerce_scalar(parts[0])
                y = _coerce_scalar(parts[1])
        else:
            x, y = None, None
        pts.append((x, y))
    return pts

def _flatten_curve(name: str, pts: List[Tuple[Optional[float], Optional[float]]], max_pts: int) -> Dict[str, object]:
    out: Dict[str, object] = {}
    # store as JSON string list of "x, y" to match common CSV dumps, plus count
    s_list = [f"{int(x) if isinstance(x, float) and x.is_integer() else x}, {int(y) if isinstance(y, float) and y.is_integer() else y}"
              for (x, y) in pts]
    out[f"settings.{name}"] = json.dumps(s_list, ensure_ascii=False)
    out[f"settings.{name}__count"] = float(len(pts))  # keep numeric for easy stats

    # per-point columns up to max_pts
    for i in range(max_pts):
        xi = pts[i][0] if i < len(pts) else None
        yi = pts[i][1] if i < len(pts) else None
        out[f"settings.{name}_Pt{i+1}_X"] = xi
        out[f"settings.{name}_Pt{i+1}_Y"] = yi
    return out

def _gather_crs_description(doc: etree._ElementTree) -> List[etree._Element]:
    descs = doc.xpath("//rdf:Description", namespaces=NSMAP)
    # Keep all rdf:Description nodes; many files have just one
    return [d for d in descs]

@dataclass
class XMPParseResult:
    row: Dict[str, object]
    warnings: List[str]

def parse_xmp_file(
    path: Path,
    base_dir: Optional[Path] = None,
    tonecurve_max_points: int = 16
) -> XMPParseResult:
    warnings: List[str] = []
    row: Dict[str, object] = {}
    row["format"] = "xmp"
    row["collection"] = "."
    row["file_name"] = path.name
    row["file_size_bytes"] = path.stat().st_size
    row["mtime_iso"] = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).isoformat()
    if base_dir:
        try:
            row["relative_path"] = str(path.relative_to(base_dir))
        except Exception:
            row["relative_path"] = path.name
    else:
        row["relative_path"] = path.name

    # parse xml
    parser = etree.XMLParser(remove_blank_text=False, recover=True)
    doc = etree.parse(str(path), parser)
    root = doc.getroot()

    # root meta (x:xmptk)
    xmptk = root.get("{%s}xmptk" % X_NS)
    if xmptk:
        row["x:xmptk"] = xmptk

    # collect Description nodes
    descriptions = _gather_crs_description(doc)
    if not descriptions:
        return XMPParseResult(row=row, warnings=warnings + ["No rdf:Description found"])

    # unify over all descriptions (typically one)
    crs_attrs: Dict[str, object] = {}
    alt_blocks: Dict[str, List[Dict[str, Optional[str]]]] = {}
    curve_blocks: Dict[str, Dict[str, object]] = {}
    other_elements: Dict[str, object] = {}

    for d in descriptions:
        # attributes (namespaced)
        for qname, val in d.attrib.items():
            if not isinstance(qname, str):  # safety
                continue
            if qname.startswith("{%s}" % CRS_NS):
                name = qname.split("}", 1)[1]
                crs_attrs[name] = _coerce_scalar(val)
            elif qname.endswith("about"):
                # rdf:about; not very useful for single-preset XMP
                pass
            else:
                # capture unknown attrs with ns prefix if present
                # e.g., crs on element, or any others
                try:
                    ns_uri, local = qname[1:].split("}")
                    key = f"attr[{ns_uri}]::{local}"
                    other_elements[key] = val
                except Exception:
                    other_elements[qname] = val

        # child elements we care about
        for child in d:
            if child.tag == "{%s}Name" % CRS_NS:
                alt_blocks["Name"] = _parse_rdf_alt(child)
            elif child.tag == "{%s}ShortName" % CRS_NS:
                alt_blocks["ShortName"] = _parse_rdf_alt(child)
            elif child.tag == "{%s}SortName" % CRS_NS:
                alt_blocks["SortName"] = _parse_rdf_alt(child)
            elif child.tag == "{%s}Group" % CRS_NS:
                alt_blocks["Group"] = _parse_rdf_alt(child)
            elif child.tag == "{%s}Description" % CRS_NS:
                alt_blocks["Description"] = _parse_rdf_alt(child)
            elif child.tag.startswith("{%s}ToneCurve" % CRS_NS):
                # master + RGB + Extended variants
                local = child.tag.split("}", 1)[1]  # e.g., ToneCurvePV2012Blue
                seq = _parse_rdf_seq_strings(child)
                pts = _parse_curve_points(seq)
                curve_blocks[local] = _flatten_curve(local, pts, tonecurve_max_points)
            elif child.tag == "{%s}Look" % CRS_NS:
                # flatten Look attributes under settings.Look.*
                for k, v in child.attrib.items():
                    row[f"settings.Look.{k}"] = _coerce_scalar(v)
            else:
                # generic capture if needed
                # store element text if it has any (rare in crs)
                if child.text and child.text.strip():
                    local = child.tag.split("}", 1)[1] if "}" in child.tag else child.tag
                    other_elements[f"elem.{local}"] = child.text.strip()

    # map crs attrs to "settings.*"
    for k, v in crs_attrs.items():
        row[f"settings.{k}"] = v

    # identity & friendly fields
    row["id"] = crs_attrs.get("UUID")
    # title/internalName from Name[x-default] if present
    title = None
    if "Name" in alt_blocks and alt_blocks["Name"]:
        # pick x-default first if available
        by_lang = {i.get("_lang") or "x-default": i.get("value") for i in alt_blocks["Name"]}
        title = by_lang.get("x-default") or next((i.get("value") for i in alt_blocks["Name"] if i.get("value")), None)
    row["title"] = title
    row["internalName"] = title
    row["type"] = crs_attrs.get("PresetType")

    # alt blocks as JSON
    for name, items in alt_blocks.items():
        row[f"settings.{name}__alt_json"] = json.dumps({"kind": "Alt", "items": items}, ensure_ascii=False)

    # tone curve blocks (already flattened)
    for name, fields in curve_blocks.items():
        row.update(fields)

    # stash any unexpected attrs/elements (namespaced) for completeness
    for k, v in other_elements.items():
        row[k] = v

    return XMPParseResult(row=row, warnings=warnings)
