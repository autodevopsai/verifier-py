.PHONY: help install-dev lint format test

help:
	@echo "Commands:"
	@echo "  install-dev: Install development dependencies"
	@echo "  lint       : Run linters"
	@echo "  format     : Format code"
	@echo "  test       : Run tests"

install-dev:
	pip install -e ".[dev]"

lint:
	pylint src
	mypy src

format:
	black src
	isort src

test:
	pytest
