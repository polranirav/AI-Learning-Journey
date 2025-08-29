from __future__ import annotations

import os

from xmp_style_lab.io.lrtemplate_reader import parse_lrtemplate


def test_parse_lrtemplate_sample():
    here = os.path.dirname(__file__)
    sample = os.path.join(here, "samples", "sample.lrtemplate")
    data = parse_lrtemplate(sample)
    assert data["source"] == "lrtemplate"
    assert data["file_name"].endswith("sample.lrtemplate")
    assert str(data.get("ProcessVersion")) in {"11.0", "11"}
    assert int(data.get("Contrast2012")) == 25


