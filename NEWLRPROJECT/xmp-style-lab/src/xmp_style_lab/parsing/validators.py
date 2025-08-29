from __future__ import annotations

from typing import Any


def safe_cast_bool(value: Any) -> bool | None:
    if isinstance(value, bool):
        return value
    if value is None:
        return None
    s = str(value).strip().lower()
    if s in {"true", "yes", "1"}:
        return True
    if s in {"false", "no", "0"}:
        return False
    return None


def safe_cast_int(value: Any) -> int | None:
    try:
        if value is None:
            return None
        if isinstance(value, bool):
            return int(value)
        return int(str(value).strip())
    except Exception:
        return None


def safe_cast_float(value: Any) -> float | None:
    try:
        if value is None:
            return None
        if isinstance(value, bool):
            return float(int(value))
        return float(str(value).strip().replace("+", ""))
    except Exception:
        return None


def coerce_scalar(value: Any) -> Any:
    b = safe_cast_bool(value)
    if b is not None:
        return b
    i = safe_cast_int(value)
    if i is not None:
        return i
    f = safe_cast_float(value)
    if f is not None:
        return f
    if value is None:
        return None
    return str(value)


