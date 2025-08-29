from __future__ import annotations

from xmp_style_lab.parsing.tonecurve import expand_curve


def test_expand_curve_basic():
    assert expand_curve("0, 0, 255, 255") == [0.0, 0.0, 255.0, 255.0]


