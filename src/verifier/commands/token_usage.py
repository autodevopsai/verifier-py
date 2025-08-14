"""Token usage command."""

import typer


def token_usage(
    period: str = typer.Option("daily", "-p", "--period", help="hourly|daily|weekly|monthly"),
    output_format: str = typer.Option("table", "--format", help="table|json"),
) -> None:
    """Show token usage."""
    typer.echo(f"Token usage not implemented yet. period={period} format={output_format}")
