from __future__ import annotations

import os

from xmp_style_lab.io.xmp_reader import parse_xmp


def test_parse_xmp_sample():
    here = os.path.dirname(__file__)
    sample = os.path.join(here, "samples", "sample.xmp")
    data = parse_xmp(sample)
    assert data["source"] == "xmp"
    assert data["file_name"].endswith("sample.xmp")
    assert data.get("crs:ProcessVersion") == "11.0"
    assert data.get("crs:Contrast2012") in {"25", 25, "+25"}


