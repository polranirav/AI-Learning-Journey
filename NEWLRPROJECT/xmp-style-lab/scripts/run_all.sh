#!/usr/bin/env bash
set -euo pipefail

. .venv/bin/activate
PYTHONPATH=src python -m xmp_style_lab.cli.preset_extract --config config/extract.yaml
# Future:
# PYTHONPATH=src python -m xmp_style_lab.cli.preset_train --config config/train.yaml
# PYTHONPATH=src python -m xmp_style_lab.cli.preset_generate --config config/generate.yaml


