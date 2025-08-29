from __future__ import annotations

from typing import Iterable, List


def expand_curve(curve_str: str) -> List[float]:
    # Very simple CSV-of-numbers parser for initial tests
    if not curve_str:
        return []
    parts = [p.strip() for p in curve_str.split(',')]
    out: List[float] = []
    for p in parts:
        try:
            out.append(float(p))
        except Exception:
            pass
    return out


