# src/xmp_style_lab/cli/preset_extract.py
import argparse, sys, yaml, json, csv
from pathlib import Path
from typing import List, Dict, Set
from tqdm import tqdm

from xmp_style_lab.parsing.xmp_reader import parse_xmp_file, META_PREFIX

def _find_xmp_files(root: Path) -> List[Path]:
    if not root.exists():
        return []
    return sorted([p for p in root.rglob("*.xmp") if p.is_file()])

def _union_keys(rows: List[Dict[str, object]]) -> List[str]:
    # stable order: meta first, then settings.*, then the rest
    keys_all: Set[str] = set()
    for r in rows:
        keys_all.update(r.keys())

    meta = [k for k in META_PREFIX if k in keys_all]
    settings = sorted([k for k in keys_all if k.startswith("settings.")])
    other = sorted([k for k in keys_all if k not in set(meta) and not k.startswith("settings.")])
    return meta + settings + other

def main(argv=None):
    ap = argparse.ArgumentParser(description="Extract XMP files into a wide CSV and JSONL (XMP-only).")
    ap.add_argument("--config", required=True, help="Path to extract.yaml")
    args = ap.parse_args(argv)

    cfg = yaml.safe_load(open(args.config))
    xmp_dir = Path(cfg.get("xmp_dir", "data/raw/xmp"))
    out_csv = Path(cfg.get("out_csv", "data/processed/presets_full_wide.csv"))
    out_jsonl = Path(cfg.get("out_jsonl", "data/interim/raw_dump.jsonl"))
    tonecurve_max_points = int(cfg.get("tonecurve_max_points", 16))

    files = _find_xmp_files(xmp_dir)
    if not files:
        print(f"[preset_extract] No .xmp files under {xmp_dir}")
        sys.exit(0)

    rows: List[Dict[str, object]] = []
    warns_total = 0

    print(f"[preset_extract] Parsing {len(files)} XMPs from {xmp_dir} ...")
    for p in tqdm(files):
        res = parse_xmp_file(p, base_dir=xmp_dir, tonecurve_max_points=tonecurve_max_points)
        rows.append(res.row)
        warns_total += len(res.warnings)

    cols = _union_keys(rows)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    out_jsonl.parent.mkdir(parents=True, exist_ok=True)

    # CSV
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in cols})

    # JSONL
    with out_jsonl.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"[preset_extract] Wrote CSV -> {out_csv}")
    print(f"[preset_extract] Wrote JSONL -> {out_jsonl}")
    if warns_total:
        print(f"[preset_extract] Warnings encountered: {warns_total}")

if __name__ == "__main__":
    main()
