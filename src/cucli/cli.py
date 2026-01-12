"""Click CLI for ClickUp."""
import json

import click
from cucli.api import ClickUpClient
from cucli.models import Team


@click.group()
@click.version_option()
def cli() -> None:
    """cucli - ClickUp CLI."""
    pass


@cli.command(name="workspaces")
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
def workspaces(format: str, raw: bool) -> None:
    """List your ClickUp workspaces."""
    try:
        with ClickUpClient() as client:
            data = client.get_teams()

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            teams = [Team(**team) for team in data["teams"]]
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()

    if format == "json":
        output = [{"id": t.id, "name": t.name, "color": t.color} for t in teams]
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        if not teams:
            click.echo("No workspaces found.")
            return

        # Calculate column widths
        max_id = max(len(t.id) for t in teams)
        max_name = max(len(t.name) for t in teams)
        max_color = max(len(t.color) for t in teams)

        # Print header
        click.echo(f"{'ID'.ljust(max_id)}  {'NAME'.ljust(max_name)}  {'COLOR'}")
        click.echo("-" * (max_id + max_name + max_color + 6))

        # Print rows
        for team in teams:
            click.echo(
                f"{team.id.ljust(max_id)}  {team.name.ljust(max_name)}  {team.color}"
            )


def main() -> None:
    """Entry point for the CLI."""
    cli()
