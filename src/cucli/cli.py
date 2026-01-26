"""Click CLI for ClickUp."""

import json

import click
import httpx
from cucli.api import ClickUpClient
from cucli.models import Team, Task


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


@cli.command(name="task")
@click.argument("task_id")
@click.option(
    "--format",
    type=click.Choice(["json", "table", "markdown"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
@click.option("--md-only", is_flag=True, help="Output only the Markdown description.")
def task(task_id: str, format: str, raw: bool, md_only: bool) -> None:
    """Get details for a specific task.

    TASK_ID: The ID of the task to retrieve.
    """
    try:
        with ClickUpClient() as client:
            data = client.get_task(task_id)

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            task = Task(**data)

            if md_only:
                # Use markdown_description if available, otherwise fall back to description
                desc = task.markdown_description or task.description
                if desc:
                    click.echo(desc)
                else:
                    click.echo("(No description)")
                return

            if format == "json":
                output = {
                    "id": task.id,
                    "name": task.name,
                    "description": task.description,
                    "markdown_description": task.markdown_description,
                    "status": task.status.get("status") if task.status else None,
                    "priority": task.priority.get("priority")
                    if task.priority
                    else None,
                    "assignees": [a.get("username") for a in task.assignees],
                    "tags": [t.get("name") for t in task.tags],
                    "due_date": task.due_date,
                    "start_date": task.start_date,
                }
                click.echo(json.dumps(output, indent=2))
            elif format == "table":
                click.echo(f"ID:       {task.id}")
                click.echo(f"Name:     {task.name}")
                if task.status:
                    click.echo(f"Status:   {task.status.get('status')}")
                if task.priority:
                    click.echo(f"Priority: {task.priority.get('priority')}")
                if task.assignees:
                    click.echo(
                        f"Assignees: {', '.join(a.get('username', '') for a in task.assignees)}"
                    )
                if task.tags:
                    click.echo(
                        f"Tags:     {', '.join(t.get('name', '') for t in task.tags)}"
                    )
                if task.due_date:
                    click.echo(f"Due Date: {task.due_date}")
                # Use markdown_description if available, otherwise fall back to description
                desc = task.markdown_description or task.description
                if desc:
                    click.echo("\nDescription:")
                    click.echo(desc)
            elif format == "markdown":
                # Use markdown_description if available, otherwise fall back to description
                desc = task.markdown_description or task.description
                if desc:
                    click.echo(desc)
                else:
                    click.echo("(No description)")
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        raise click.Abort()


@cli.command(name="tasks")
@click.argument("team_id")
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
@click.option("--page", type=int, help="Page to fetch (starts at 0).")
@click.option("--status", multiple=True, help="Filter by status (can use multiple).")
@click.option(
    "--include-closed",
    is_flag=True,
    help="Include closed tasks.",
)
@click.option(
    "--space-id", multiple=True, help="Filter by space ID (can use multiple)."
)
@click.option("--list-id", multiple=True, help="Filter by list ID (can use multiple).")
@click.option(
    "--assignee", multiple=True, help="Filter by assignee ID (can use multiple)."
)
@click.option("--tag", multiple=True, help="Filter by tag (can use multiple).")
def tasks(
    team_id: str,
    format: str,
    raw: bool,
    page: int | None,
    status: tuple[str, ...],
    include_closed: bool,
    space_id: tuple[str, ...],
    list_id: tuple[str, ...],
    assignee: tuple[str, ...],
    tag: tuple[str, ...],
) -> None:
    """List tasks in a team/workspace.

    TEAM_ID: The ID of the team/workspace.
    """
    try:
        with ClickUpClient() as client:
            data = client.get_team_tasks(
                team_id,
                page=page,
                include_markdown_description=True,
                statuses=list(status) if status else None,
                include_closed=include_closed,
                space_ids=list(space_id) if space_id else None,
                list_ids=list(list_id) if list_id else None,
                assignees=list(assignee) if assignee else None,
                tags=list(tag) if tag else None,
            )

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            tasks_list = data.get("tasks", [])

            if format == "json":
                output = []
                for task_data in tasks_list:
                    task = Task(**task_data)
                    output.append(
                        {
                            "id": task.id,
                            "name": task.name,
                            "status": task.status.get("status")
                            if task.status
                            else None,
                            "priority": task.priority.get("priority")
                            if task.priority
                            else None,
                            "assignees": [a.get("username") for a in task.assignees],
                            "tags": [t.get("name") for t in task.tags],
                            "due_date": task.due_date,
                            "url": task_data.get("url"),
                        }
                    )
                click.echo(json.dumps(output, indent=2))
            elif format == "table":
                if not tasks_list:
                    click.echo("No tasks found.")
                    return

                # Calculate column widths
                max_id = max(len(t.get("id", "")) for t in tasks_list)
                max_name = max(len(t.get("name", "")) for t in tasks_list)
                max_status = max(
                    len(str(t.get("status", {}).get("status", ""))) for t in tasks_list
                )

                # Print header
                click.echo(
                    f"{'ID'.ljust(max_id)}  {'NAME'.ljust(max_name)}  {'STATUS'}"
                )
                click.echo("-" * (max_id + max_name + max_status + 6))

                # Print rows
                for task_data in tasks_list:
                    task = Task(**task_data)
                    status_val = task.status.get("status") if task.status else ""
                    click.echo(
                        f"{task.id.ljust(max_id)}  {task.name.ljust(max_name)}  {status_val}"
                    )
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        raise click.Abort()


def main() -> None:
    """Entry point for the CLI."""
    cli()
