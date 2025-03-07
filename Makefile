.PHONY: setup dev autofix format serve

setup:
	asdf install
	uv pip install -r pyproject.toml

dev:
	uv run uvicorn app.main:app --reload --port 8000

autofix:
	uv run ruff check --fix .

format:
	uv run ruff format .

serve:
	uv run uvicorn app.main:app --host 0.0.0.0 --port 80


