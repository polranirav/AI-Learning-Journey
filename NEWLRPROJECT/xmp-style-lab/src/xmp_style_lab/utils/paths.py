from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class ProjectPaths:
    raw_xmp_dir: str
    raw_lrtemplate_dir: str
    processed_dir: str


def ensure_dirs(paths: ProjectPaths) -> None:
    os.makedirs(paths.processed_dir, exist_ok=True)


