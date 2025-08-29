from __future__ import annotations

from typing import Any, Dict


def build_xmp_from_dict(params: Dict[str, Any]) -> str:
    # Minimal synthetic XMP builder for roundtrip tests; not full-fidelity.
    crs_attrs = []
    for k, v in params.items():
        if k.startswith("crs:"):
            local = k.split(":", 1)[1]
            crs_attrs.append(f'crs:{local}="{v}"')
    attrs_str = "\n      ".join(crs_attrs)
    return (
        "<x:xmpmeta xmlns:x=\"adobe:ns:meta/\">\n"
        "  <rdf:RDF xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\">\n"
        "    <rdf:Description xmlns:crs=\"http://ns.adobe.com/camera-raw-settings/1.0/\"\n"
        f"      {attrs_str}>\n"
        "    </rdf:Description>\n"
        "  </rdf:RDF>\n"
        "</x:xmpmeta>\n"
    )


