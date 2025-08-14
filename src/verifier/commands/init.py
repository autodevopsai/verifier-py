"""Init command."""

import typer


def init(  # pylint: disable=unused-argument
    force: bool = typer.Option(False, "--force", help="Overwrite existing configuration")
) -> None:
    """Initialize verifier in this repository."""
    typer.echo("Initialization not implemented yet.")
