from __future__ import annotations

from xmp_style_lab.parsing.field_map import canonical_columns


def test_canonical_columns_order():
    cols = canonical_columns(["b", "a"])
    assert cols[:3] == ["source", "file_name", "preset_name"]
    assert cols[3:] == ["a", "b"]


