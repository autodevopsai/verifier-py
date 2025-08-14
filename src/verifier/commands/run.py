"""Run command."""

from typing import List, Optional

import typer


def run(
    agent: str,
    files: Optional[List[str]] = typer.Option(None, "-f", "--files", help="Files to include"),
) -> None:
    """Run a verifier agent."""
    typer.echo(f"Running agent {agent} (stub).")
    if files:
        typer.echo(f"Files: {', '.join(files)}")
