from __future__ import annotations

from typing import Iterable, List


FIXED_PREFIX_COLUMNS: list[str] = [
    "source",
    "file_name",
    "preset_name",
]


def canonical_columns(dynamic_keys: Iterable[str]) -> List[str]:
    return [*FIXED_PREFIX_COLUMNS, *sorted(set(dynamic_keys))]


