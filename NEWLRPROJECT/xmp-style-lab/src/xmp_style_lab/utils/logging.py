from __future__ import annotations

import logging


def setup_logging(level: int = logging.INFO) -> None:
    logging.basicConfig(format="[%(levelname)s] %(message)s", level=level)


