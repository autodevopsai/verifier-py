"""CLI entry point for the verifier tool."""

from __future__ import annotations

import typer

from . import __version__
from .commands import doctor, init, run, token_usage

app = typer.Typer(name="verifier", help="Verifier CLI tool")
app.command()(init)
app.command()(run)
app.command("token-usage")(token_usage)
app.command()(doctor)


def version_callback(value: bool) -> None:
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@app.callback()
def main(  # pylint: disable=unused-argument
    version: bool = typer.Option(
        False,
        "--version",
        "-v",
        help="Show version and exit",
        callback=version_callback,
        is_eager=True,
    )
) -> None:
    """Main entry point for the CLI."""


def run_app() -> None:
    """Run the Typer application."""
    app()


if __name__ == "__main__":
    run_app()
