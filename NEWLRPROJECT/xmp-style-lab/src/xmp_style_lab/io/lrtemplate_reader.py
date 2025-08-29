from __future__ import annotations

import os
import re
from typing import Any, Dict

from slpp import slpp as lua


TOP_TABLE_REGEX = re.compile(r"\{[\s\S]*\}")


def _decode_lua_table(text: str) -> Dict[str, Any]:
    match = TOP_TABLE_REGEX.search(text)
    if not match:
        raise ValueError("No Lua table found in .lrtemplate")
    table_text = match.group(0)
    data = lua.decode(table_text)
    if not isinstance(data, dict):
        raise ValueError("Decoded .lrtemplate is not a dict")
    return data


def parse_lrtemplate(file_path: str) -> Dict[str, Any]:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    data = _decode_lua_table(text)

    settings = {}
    if "settings" in data and isinstance(data["settings"], dict):
        settings.update({str(k): v for k, v in data["settings"].items()})
    elif "value" in data and isinstance(data["value"], dict):
        settings.update({str(k): v for k, v in data["value"].items()})

    preset_name = None
    for possible in ("title", "internalName", "name"):
        if isinstance(data.get(possible), str):
            preset_name = data[possible]
            break

    merged: Dict[str, Any] = {str(k): v for k, v in data.items() if not isinstance(v, (dict, list))}
    merged.update(settings)
    merged.update(
        {
            "source": "lrtemplate",
            "file_name": os.path.basename(file_path),
            "preset_name": preset_name,
        }
    )
    return merged


