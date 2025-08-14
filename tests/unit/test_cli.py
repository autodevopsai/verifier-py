"""Tests for the CLI entry point."""

from typer.testing import CliRunner

from verifier.cli import app
from verifier import __version__

runner = CliRunner()


def test_version() -> None:
    """CLI returns version."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_help() -> None:
    """CLI shows help message."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Verifier CLI tool" in result.stdout
