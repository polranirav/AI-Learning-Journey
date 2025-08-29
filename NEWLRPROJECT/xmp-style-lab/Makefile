PYTHON := python3
VENV := .venv

.PHONY: venv install test extract

venv:
	$(PYTHON) -m venv $(VENV)
	. $(VENV)/bin/activate; pip install -U pip

install: venv
	. $(VENV)/bin/activate; pip install -r requirements.txt

test:
	PYTHONPATH=src . $(VENV)/bin/activate; pytest -q

extract:
	PYTHONPATH=src . $(VENV)/bin/activate; python -m xmp_style_lab.cli.preset_extract --config config/extract.yaml


