.PHONY: setup reset run setup-uv reset-uv update-uv

UV_VERSION := 0.11.18

setup: setup-uv

reset: 
	@rm -rf .venv
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	${MAKE} reset-uv

run:
	@uv run fastapi dev main.py

setup-uv:
	@curl -LsSf https://astral.sh/uv/$(UV_VERSION)/install.sh | sh
	@uv sync

update-uv:
	@uv self update

reset-uv:
	@uv cache clean || true
	@rm -r "$(uv python dir)" || true
	@rm -r "$(uv tool dir)" || true
	@rm ~/.local/bin/uv ~/.local/bin/uvx || true