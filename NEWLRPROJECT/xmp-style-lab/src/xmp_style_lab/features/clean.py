from __future__ import annotations

from typing import Any, Dict

from xmp_style_lab.parsing.validators import coerce_scalar


def clean_row(row: Dict[str, Any]) -> Dict[str, Any]:
    return {k: coerce_scalar(v) for k, v in row.items()}


