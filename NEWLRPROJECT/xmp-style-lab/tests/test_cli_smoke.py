from __future__ import annotations

import os
import subprocess


def test_cli_stubs_run():
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"

    # Extract (creates stub outputs)
    subprocess.run(["python", "-m", "xmp_style_lab.cli.preset_extract", "--config", "config/extract.yaml"], check=True, env=env)
    assert os.path.exists("data/processed/presets.csv")
    assert os.path.exists("data/processed/presets.jsonl")

    # Train stub
    subprocess.run(["python", "-m", "xmp_style_lab.cli.preset_train", "--config", "config/train.yaml"], check=True, env=env)

    # Generate stub
    subprocess.run(["python", "-m", "xmp_style_lab.cli.preset_generate", "--config", "config/generate.yaml"], check=True, env=env)


