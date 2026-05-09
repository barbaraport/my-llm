.PHONY: setup reset run setup-uv reset-uv update-uv

setup: setup-uv

reset: reset-uv

run:
	@uv run fastapi dev main.py

setup-uv:
	@curl -LsSf https://astral.sh/uv/install.sh | sh
	@uv sync

update-uv:
	@uv self update

reset-uv:
	@uv cache clean || true
	@rm -r "$(uv python dir)" || true
	@rm -r "$(uv tool dir)" || true
	@rm ~/.local/bin/uv ~/.local/bin/uvx || true