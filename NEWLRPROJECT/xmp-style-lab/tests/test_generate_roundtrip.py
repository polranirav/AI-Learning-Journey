from __future__ import annotations

import os
import tempfile

from xmp_style_lab.io.xmp_writer import build_xmp_from_dict
from xmp_style_lab.io.xmp_reader import parse_xmp


def test_roundtrip_minimal_xmp():
    params = {
        "crs:ProcessVersion": "11.0",
        "crs:Contrast2012": "+25",
    }
    xml = build_xmp_from_dict(params)
    with tempfile.TemporaryDirectory() as td:
        path = os.path.join(td, "tmp.xmp")
        with open(path, "w", encoding="utf-8") as f:
            f.write(xml)
        parsed = parse_xmp(path)
        assert parsed.get("crs:ProcessVersion") == "11.0"
        assert parsed.get("crs:Contrast2012") in {"25", "+25", 25}


