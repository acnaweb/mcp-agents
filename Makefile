.PHONY: venv install run test clean lint docs-serve

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

venv:
	python3 -m venv $(VENV)

install: venv
	$(PIP) install --upgrade pip
	pip install -e .
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) src/mcp_agents/orchestrator/main.py

test:
	$(PYTHON) -m pytest tests/

lint:
	$(PYTHON) -m black src/ tests/

docs-serve:
	$(PYTHON) -m mkdocs serve

clean:
	rm -rf $(VENV)
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type f -name '*.pyc' -delete
