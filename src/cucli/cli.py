"""Click CLI for ClickUp."""

import json

import click
import httpx
from cucli.api import ClickUpClient
from cucli.models import (
    Checklist,
    ClickUpList,
    Comment,
    Folder,
    ListMember,
    Space,
    Tag,
    Task,
    TaskMember,
    Team,
)


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


@cli.command(name="spaces")
@click.argument("team_id")
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
@click.option(
    "--archived",
    is_flag=True,
    help="Include archived spaces.",
)
def spaces(team_id: str, format: str, raw: bool, archived: bool) -> None:
    """List spaces in a workspace.

    TEAM_ID: The ID of the team/workspace.
    """
    try:
        with ClickUpClient() as client:
            data = client.get_spaces(team_id, archived=archived)

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            spaces_list = [Space(**space) for space in data["spaces"]]
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()

    if format == "json":
        output = [
            {
                "id": s.id,
                "name": s.name,
                "private": s.private,
                "archived": s.archived,
            }
            for s in spaces_list
        ]
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        if not spaces_list:
            click.echo("No spaces found.")
            return

        # Calculate column widths
        max_id = max(len(s.id) for s in spaces_list)
        max_name = max(len(s.name) for s in spaces_list)

        # Print header
        click.echo(f"{'ID'.ljust(max_id)}  {'NAME'.ljust(max_name)}  {'PRIVATE'}")
        click.echo("-" * (max_id + max_name + 8))

        # Print rows
        for space in spaces_list:
            private_str = "Yes" if space.private else "No"
            click.echo(
                f"{space.id.ljust(max_id)}  {space.name.ljust(max_name)}  {private_str}"
            )


@cli.command(name="folders")
@click.argument("space_id")
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
@click.option(
    "--archived",
    is_flag=True,
    help="Include archived folders.",
)
def folders(space_id: str, format: str, raw: bool, archived: bool) -> None:
    """List folders in a space.

    SPACE_ID: The ID of the space.
    """
    try:
        with ClickUpClient() as client:
            data = client.get_folders(space_id, archived=archived)

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            folders_list = [Folder(**folder) for folder in data["folders"]]
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()

    if format == "json":
        output = [
            {
                "id": f.id,
                "name": f.name,
                "hidden": f.hidden,
                "task_count": f.task_count,
            }
            for f in folders_list
        ]
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        if not folders_list:
            click.echo("No folders found.")
            return

        # Calculate column widths
        max_id = max(len(f.id) for f in folders_list)
        max_name = max(len(f.name) for f in folders_list)
        max_count = max(len(str(f.task_count)) for f in folders_list)

        # Print header
        click.echo(
            f"{'ID'.ljust(max_id)}  {'NAME'.ljust(max_name)}  {'TASKS'.ljust(max_count)}  {'HIDDEN'}"
        )
        click.echo("-" * (max_id + max_name + max_count + 12))

        # Print rows
        for folder in folders_list:
            hidden_str = "Yes" if folder.hidden else "No"
            click.echo(
                f"{folder.id.ljust(max_id)}  {folder.name.ljust(max_name)}  {str(folder.task_count).ljust(max_count)}  {hidden_str}"
            )


@cli.command(name="create-folder")
@click.argument("space_id")
@click.option("--name", required=True, help="Folder name (required).")
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
def create_folder(space_id: str, name: str, format: str, raw: bool) -> None:
    """Create a new folder in a space.

    SPACE_ID: The ID of the space to create the folder in.
    """
    try:
        with ClickUpClient() as client:
            data = client.create_folder(space_id, name=name)

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            if format == "json":
                output = {
                    "id": data.get("id"),
                    "name": data.get("name"),
                    "space_id": data.get("space", {}).get("id"),
                    "task_count": data.get("task_count"),
                }
                click.echo(json.dumps(output, indent=2))
            elif format == "table":
                click.echo(f"ID:        {data.get('id')}")
                click.echo(f"Name:      {data.get('name')}")
                click.echo(f"Space ID:  {data.get('space', {}).get('id')}")
                click.echo(f"Task Count: {data.get('task_count')}")
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        raise click.Abort()


@cli.command(name="create-list")
@click.argument("folder_id")
@click.option("--name", required=True, help="List name (required).")
@click.option("--description", help="List description (text content).")
@click.option("--markdown-description", help="List description (markdown content).")
@click.option(
    "--due-date",
    type=int,
    help="Due date as Unix timestamp in milliseconds.",
)
@click.option("--due-date-time", is_flag=True, help="Due date includes a time.")
@click.option(
    "--priority",
    type=int,
    help="List priority (0: Urgent, 1: High, 2: Normal, 3: Low, 4: None).",
)
@click.option("--assignee", type=int, help="Assignee user ID to assign the list to.")
@click.option("--status", help="List status (color).")
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
def create_list(
    folder_id: str,
    name: str,
    description: str | None,
    markdown_description: str | None,
    due_date: int | None,
    due_date_time: bool,
    priority: int | None,
    assignee: int | None,
    status: str | None,
    format: str,
    raw: bool,
) -> None:
    """Create a new list in a folder.

    FOLDER_ID: The ID of the folder to create the list in.
    """
    try:
        with ClickUpClient() as client:
            data = client.create_list(
                folder_id,
                name=name,
                content=description,
                markdown_content=markdown_description,
                due_date=due_date,
                due_date_time=due_date_time,
                priority=priority,
                assignee=assignee,
                status=status,
            )

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            if format == "json":
                output = {
                    "id": data.get("id"),
                    "name": data.get("name"),
                    "folder_id": data.get("folder", {}).get("id"),
                    "space_id": data.get("space", {}).get("id"),
                    "task_count": data.get("task_count"),
                }
                click.echo(json.dumps(output, indent=2))
            elif format == "table":
                click.echo(f"ID:         {data.get('id')}")
                click.echo(f"Name:       {data.get('name')}")
                click.echo(f"Folder ID:  {data.get('folder', {}).get('id')}")
                click.echo(f"Space ID:   {data.get('space', {}).get('id')}")
                click.echo(f"Task Count: {data.get('task_count')}")
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        raise click.Abort()


@cli.command(name="lists")
@click.argument("folder_id")
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
@click.option(
    "--archived",
    is_flag=True,
    help="Include archived lists.",
)
def lists(folder_id: str, format: str, raw: bool, archived: bool) -> None:
    """List lists in a folder.

    FOLDER_ID: The ID of the folder.
    """
    try:
        with ClickUpClient() as client:
            data = client.get_lists(folder_id, archived=archived)

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            lists_list = [ClickUpList(**lst) for lst in data["lists"]]
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()

    if format == "json":
        output = [
            {
                "id": lst.id,
                "name": lst.name,
                "archived": lst.archived,
                "task_count": str(lst.task_count),
            }
            for lst in lists_list
        ]
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        if not lists_list:
            click.echo("No lists found.")
            return

        # Calculate column widths
        max_id = max(len(lst.id) for lst in lists_list)
        max_name = max(len(lst.name) for lst in lists_list)
        max_count = max(len(str(lst.task_count)) for lst in lists_list)

        # Print header
        click.echo(
            f"{'ID'.ljust(max_id)}  {'NAME'.ljust(max_name)}  {'TASKS'.ljust(max_count)}  {'ARCHIVED'}"
        )
        click.echo("-" * (max_id + max_name + max_count + 14))

        # Print rows
        for lst in lists_list:
            archived_str = "Yes" if lst.archived else "No"
            click.echo(
                f"{lst.id.ljust(max_id)}  {lst.name.ljust(max_name)}  {str(lst.task_count).ljust(max_count)}  {archived_str}"
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


@cli.command(name="create-task")
@click.argument("list_id")
@click.option("--name", required=True, help="Task name (required).")
@click.option("--description", help="Task description (text content).")
@click.option("--markdown-description", help="Task description (markdown content).")
@click.option("--status", help="Task status.")
@click.option(
    "--priority",
    type=int,
    help="Task priority (0: Urgent, 1: High, 2: Normal, 3: Low, 4: None).",
)
@click.option(
    "--assignee",
    multiple=True,
    type=int,
    help="Assignee user ID (can use multiple).",
)
@click.option("--tag", multiple=True, help="Tag name (can use multiple).")
@click.option(
    "--due-date",
    type=int,
    help="Due date as Unix timestamp in milliseconds.",
)
@click.option(
    "--start-date",
    type=int,
    help="Start date as Unix timestamp in milliseconds.",
)
@click.option(
    "--time-estimate",
    type=int,
    help="Time estimate in milliseconds.",
)
@click.option("--points", type=int, help="Sprint points.")
@click.option("--parent", help="Parent task ID (for subtasks).")
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
def create_task(
    list_id: str,
    name: str,
    description: str | None,
    markdown_description: str | None,
    status: str | None,
    priority: int | None,
    assignee: tuple[int, ...],
    tag: tuple[str, ...],
    due_date: int | None,
    start_date: int | None,
    time_estimate: int | None,
    points: int | None,
    parent: str | None,
    format: str,
    raw: bool,
) -> None:
    """Create a new task in a list.

    LIST_ID: The ID of the list to create the task in.
    """
    try:
        with ClickUpClient() as client:
            data = client.create_task(
                list_id,
                name=name,
                description=description,
                markdown_description=markdown_description,
                status=status,
                priority=priority,
                assignees=list(assignee) if assignee else None,
                tags=list(tag) if tag else None,
                due_date=due_date,
                start_date=start_date,
                time_estimate=time_estimate,
                points=points,
                parent=parent,
            )

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            if format == "json":
                output = {
                    "id": data.get("id"),
                    "name": data.get("name"),
                    "status": data.get("status", {}).get("status")
                    if data.get("status")
                    else None,
                    "priority": data.get("priority", {}).get("priority")
                    if data.get("priority")
                    else None,
                    "url": data.get("url"),
                }
                click.echo(json.dumps(output, indent=2))
            elif format == "table":
                click.echo(f"ID:       {data.get('id')}")
                click.echo(f"Name:     {data.get('name')}")
                if data.get("status"):
                    click.echo(f"Status:   {data.get('status', {}).get('status')}")
                if data.get("priority"):
                    click.echo(f"Priority: {data.get('priority', {}).get('priority')}")
                if data.get("url"):
                    click.echo(f"URL:      {data.get('url')}")
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        raise click.Abort()


@cli.command(name="update-task")
@click.argument("task_id")
@click.option("--name", help="Task name.")
@click.option("--description", help="Task description (text content).")
@click.option("--markdown-description", help="Task description (markdown content).")
@click.option("--status", help="Task status.")
@click.option(
    "--priority",
    type=int,
    help="Task priority (0: Urgent, 1: High, 2: Normal, 3: Low, 4: None).",
)
@click.option(
    "--due-date",
    type=int,
    help="Due date as Unix timestamp in milliseconds.",
)
@click.option(
    "--start-date",
    type=int,
    help="Start date as Unix timestamp in milliseconds.",
)
@click.option(
    "--time-estimate",
    type=int,
    help="Time estimate in milliseconds.",
)
@click.option("--points", type=int, help="Sprint points.")
@click.option("--parent", help="Parent task ID (for subtasks).")
@click.option(
    "--assignee-add",
    multiple=True,
    type=int,
    help="Assignee user ID to add (can use multiple).",
)
@click.option(
    "--assignee-remove",
    multiple=True,
    type=int,
    help="Assignee user ID to remove (can use multiple).",
)
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
def update_task(
    task_id: str,
    name: str | None,
    description: str | None,
    markdown_description: str | None,
    status: str | None,
    priority: int | None,
    due_date: int | None,
    start_date: int | None,
    time_estimate: int | None,
    points: int | None,
    parent: str | None,
    assignee_add: tuple[int, ...],
    assignee_remove: tuple[int, ...],
    format: str,
    raw: bool,
) -> None:
    """Update a task.

    TASK_ID: The ID of the task to update.
    """
    try:
        with ClickUpClient() as client:
            data = client.update_task(
                task_id,
                name=name,
                description=description,
                markdown_description=markdown_description,
                status=status,
                priority=priority,
                due_date=due_date,
                start_date=start_date,
                time_estimate=time_estimate,
                points=points,
                parent=parent,
                assignees_add=list(assignee_add) if assignee_add else None,
                assignees_remove=list(assignee_remove) if assignee_remove else None,
            )

            if raw:
                if data:
                    click.echo(json.dumps(data, indent=2))
                else:
                    click.echo("{}")
                return

            if not data:
                click.echo("No updates provided.")
                return

            if format == "json":
                output = {
                    "id": data.get("id"),
                    "name": data.get("name"),
                    "status": data.get("status", {}).get("status")
                    if data.get("status")
                    else None,
                    "priority": data.get("priority", {}).get("priority")
                    if data.get("priority")
                    else None,
                    "url": data.get("url"),
                }
                click.echo(json.dumps(output, indent=2))
            elif format == "table":
                click.echo(f"ID:       {data.get('id')}")
                click.echo(f"Name:     {data.get('name')}")
                if data.get("status"):
                    click.echo(f"Status:   {data.get('status', {}).get('status')}")
                if data.get("priority"):
                    click.echo(f"Priority: {data.get('priority', {}).get('priority')}")
                if data.get("url"):
                    click.echo(f"URL:      {data.get('url')}")
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        raise click.Abort()


@cli.command(name="delete-task")
@click.argument("task_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation prompt.")
def delete_task(task_id: str, yes: bool) -> None:
    """Delete a task.

    TASK_ID: The ID of the task to delete.
    """
    if not yes:
        if not click.confirm(f"Are you sure you want to delete task {task_id}?"):
            click.echo("Deletion cancelled.")
            return

    try:
        with ClickUpClient() as client:
            client.delete_task(task_id)
            click.echo(f"Task {task_id} deleted successfully.")
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        raise click.Abort()


@cli.command(name="task-comments")
@click.argument("task_id")
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
def task_comments(task_id: str, format: str, raw: bool) -> None:
    """List comments on a task.

    TASK_ID: The ID of the task to get comments from.
    """
    try:
        with ClickUpClient() as client:
            data = client.get_task_comments(task_id)

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            comments = [Comment(**comment) for comment in data["comments"]]
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()

    if not comments:
        click.echo("No comments found.")
        return

    if format == "json":
        output = [
            {
                "id": c.id,
                "text": c.comment_text,
                "user": c.user.username,
                "resolved": c.resolved,
                "date": c.date,
            }
            for c in comments
        ]
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        # Calculate column widths
        max_id = max(len(c.id) for c in comments)
        max_user = max(len(c.user.username) for c in comments)

        # Print header
        click.echo(
            f"{'ID'.ljust(max_id)}  {'USER'.ljust(max_user)}  {'TEXT'}  {'RESOLVED'}"
        )
        click.echo("-" * (max_id + max_user + 40))

        # Print rows
        for comment in comments:
            resolved_str = "Yes" if comment.resolved else "No"
            # Truncate comment text to 30 chars for display
            text = (
                comment.comment_text[:30] + "..."
                if len(comment.comment_text) > 30
                else comment.comment_text
            )
            click.echo(
                f"{comment.id.ljust(max_id)}  {comment.user.username.ljust(max_user)}  {text.ljust(33)}  {resolved_str}"
            )


@cli.command(name="add-comment")
@click.argument("task_id")
@click.option("--text", required=True, help="Comment text (required).")
@click.option("--assignee", type=int, help="Assignee user ID to assign the comment to.")
@click.option(
    "--no-notify", is_flag=True, help="Don't notify everyone (default: notify all)."
)
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
def add_comment(
    task_id: str,
    text: str,
    assignee: int | None,
    no_notify: bool,
    format: str,
    raw: bool,
) -> None:
    """Add a comment to a task.

    TASK_ID: The ID of the task to add a comment to.
    """
    try:
        with ClickUpClient() as client:
            data = client.create_task_comment(
                task_id, comment_text=text, assignee=assignee, notify_all=not no_notify
            )

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            if format == "json":
                output = {
                    "id": str(data.get("id")),
                    "date": data.get("date"),
                }
                click.echo(json.dumps(output, indent=2))
            elif format == "table":
                click.echo(f"ID:   {data.get('id')}")
                click.echo(f"Date: {data.get('date')}")
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        raise click.Abort()


@cli.command(name="create-checklist")
@click.argument("task_id")
@click.option("--name", required=True, help="Checklist name (required).")
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
def create_checklist(task_id: str, name: str, format: str, raw: bool) -> None:
    """Create a new checklist on a task.

    TASK_ID: The ID of the task to create the checklist on.
    """
    try:
        with ClickUpClient() as client:
            data = client.create_checklist(task_id, name=name)

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            checklist = Checklist(**data["checklist"])

            if format == "json":
                output = {
                    "id": checklist.id,
                    "task_id": checklist.task_id,
                    "name": checklist.name,
                    "resolved": checklist.resolved,
                    "unresolved": checklist.unresolved,
                }
                click.echo(json.dumps(output, indent=2))
            elif format == "table":
                click.echo(f"ID:         {checklist.id}")
                click.echo(f"Task ID:    {checklist.task_id}")
                click.echo(f"Name:       {checklist.name}")
                click.echo(f"Resolved:    {checklist.resolved}")
                click.echo(f"Unresolved:  {checklist.unresolved}")
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        raise click.Abort()


@cli.command(name="create-checklist-item")
@click.argument("checklist_id")
@click.option("--name", required=True, help="Checklist item name (required).")
@click.option("--assignee", type=int, help="Assignee user ID.")
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
def create_checklist_item(
    checklist_id: str, name: str, assignee: int | None, format: str, raw: bool
) -> None:
    """Create a new item in a checklist.

    CHECKLIST_ID: The ID of the checklist to add the item to.
    """
    try:
        with ClickUpClient() as client:
            data = client.create_checklist_item(
                checklist_id, name=name, assignee=assignee
            )

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            checklist = Checklist(**data["checklist"])

            if format == "json":
                output = {
                    "id": checklist.id,
                    "task_id": checklist.task_id,
                    "name": checklist.name,
                    "resolved": checklist.resolved,
                    "unresolved": checklist.unresolved,
                }
                click.echo(json.dumps(output, indent=2))
            elif format == "table":
                click.echo(f"ID:         {checklist.id}")
                click.echo(f"Task ID:    {checklist.task_id}")
                click.echo(f"Name:       {checklist.name}")
                click.echo(f"Resolved:    {checklist.resolved}")
                click.echo(f"Unresolved:  {checklist.unresolved}")
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        raise click.Abort()


@cli.command(name="update-checklist")
@click.argument("checklist_id")
@click.option("--name", help="Checklist name.")
@click.option(
    "--position",
    type=int,
    help="Position of the checklist (order).",
)
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
def update_checklist(
    checklist_id: str, name: str | None, position: int | None, format: str, raw: bool
) -> None:
    """Update a checklist.

    CHECKLIST_ID: The ID of the checklist to update.
    """
    try:
        with ClickUpClient() as client:
            data = client.update_checklist(checklist_id, name=name, position=position)

            if raw:
                if data:
                    click.echo(json.dumps(data, indent=2))
                else:
                    click.echo("{}")
                return

            if not data:
                click.echo("No updates provided.")
                return

            if format == "json":
                click.echo(json.dumps(data, indent=2))
            elif format == "table":
                click.echo(f"Checklist {checklist_id} updated successfully.")
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        raise click.Abort()


@cli.command(name="update-checklist-item")
@click.argument("checklist_id")
@click.argument("checklist_item_id")
@click.option("--name", help="Checklist item name.")
@click.option("--assignee", type=int, help="Assignee user ID.")
@click.option("--resolved", type=bool, help="Mark as resolved (completed).")
@click.option(
    "--parent",
    help="Parent checklist item ID (for nesting).",
)
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
def update_checklist_item(
    checklist_id: str,
    checklist_item_id: str,
    name: str | None,
    assignee: int | None,
    resolved: bool | None,
    parent: str | None,
    format: str,
    raw: bool,
) -> None:
    """Update a checklist item.

    CHECKLIST_ID: The ID of the checklist.
    CHECKLIST_ITEM_ID: The ID of the checklist item to update.
    """
    try:
        with ClickUpClient() as client:
            data = client.update_checklist_item(
                checklist_id,
                checklist_item_id,
                name=name,
                assignee=assignee,
                resolved=resolved,
                parent=parent,
            )

            if raw:
                if data:
                    click.echo(json.dumps(data, indent=2))
                else:
                    click.echo("{}")
                return

            if not data:
                click.echo("No updates provided.")
                return

            checklist = Checklist(**data["checklist"])

            if format == "json":
                output = {
                    "id": checklist.id,
                    "task_id": checklist.task_id,
                    "name": checklist.name,
                    "resolved": checklist.resolved,
                    "unresolved": checklist.unresolved,
                }
                click.echo(json.dumps(output, indent=2))
            elif format == "table":
                click.echo(f"ID:         {checklist.id}")
                click.echo(f"Task ID:    {checklist.task_id}")
                click.echo(f"Name:       {checklist.name}")
                click.echo(f"Resolved:    {checklist.resolved}")
                click.echo(f"Unresolved:  {checklist.unresolved}")
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        raise click.Abort()


@cli.command(name="delete-checklist")
@click.argument("checklist_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation prompt.")
def delete_checklist(checklist_id: str, yes: bool) -> None:
    """Delete a checklist.

    CHECKLIST_ID: The ID of the checklist to delete.
    """
    if not yes:
        if not click.confirm(
            f"Are you sure you want to delete checklist {checklist_id}?"
        ):
            click.echo("Deletion cancelled.")
            return

    try:
        with ClickUpClient() as client:
            client.delete_checklist(checklist_id)
            click.echo(f"Checklist {checklist_id} deleted successfully.")
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        raise click.Abort()


@cli.command(name="delete-checklist-item")
@click.argument("checklist_id")
@click.argument("checklist_item_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation prompt.")
def delete_checklist_item(checklist_id: str, checklist_item_id: str, yes: bool) -> None:
    """Delete a checklist item.

    CHECKLIST_ID: The ID of the checklist.
    CHECKLIST_ITEM_ID: The ID of the checklist item to delete.
    """
    if not yes:
        if not click.confirm(
            f"Are you sure you want to delete checklist item {checklist_item_id}?"
        ):
            click.echo("Deletion cancelled.")
            return

    try:
        with ClickUpClient() as client:
            client.delete_checklist_item(checklist_id, checklist_item_id)
            click.echo(
                f"Checklist item {checklist_item_id} deleted successfully from checklist {checklist_id}."
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


@cli.command(name="task-members")
@click.argument("task_id")
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
def task_members(task_id: str, format: str, raw: bool) -> None:
    """Get members with explicit access to a task.

    TASK_ID: The ID of the task to get members from.
    """
    try:
        with ClickUpClient() as client:
            data = client.get_task_members(task_id)

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            members = [TaskMember(**member) for member in data["members"]]
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()

    if not members:
        click.echo("No members found.")
        return

    if format == "json":
        output = [
            {
                "id": m.id,
                "username": m.username,
                "email": m.email,
                "initials": m.initials,
            }
            for m in members
        ]
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        # Calculate column widths
        max_id = max(len(str(m.id)) for m in members)
        max_user = max(len(m.username) for m in members)
        max_email = max(len(m.email) for m in members)

        # Print header
        click.echo(f"{'ID'.ljust(max_id)}  {'USERNAME'.ljust(max_user)}  {'EMAIL'}")
        click.echo("-" * (max_id + max_user + max_email + 6))

        # Print rows
        for member in members:
            click.echo(
                f"{str(member.id).ljust(max_id)}  {member.username.ljust(max_user)}  {member.email}"
            )


@cli.command(name="list-members")
@click.argument("list_id")
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
def list_members(list_id: str, format: str, raw: bool) -> None:
    """Get members with explicit access to a list.

    LIST_ID: The ID of the list to get members from.
    """
    try:
        with ClickUpClient() as client:
            data = client.get_list_members(list_id)

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            members = [ListMember(**member) for member in data["members"]]
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()

    if not members:
        click.echo("No members found.")
        return

    if format == "json":
        output = [
            {
                "id": m.id,
                "username": m.username,
                "email": m.email,
                "initials": m.initials,
            }
            for m in members
        ]
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        # Calculate column widths
        max_id = max(len(str(m.id)) for m in members)
        max_user = max(len(m.username) for m in members)
        max_email = max(len(m.email) for m in members)

        # Print header
        click.echo(f"{'ID'.ljust(max_id)}  {'USERNAME'.ljust(max_user)}  {'EMAIL'}")
        click.echo("-" * (max_id + max_user + max_email + 6))

        # Print rows
        for member in members:
            click.echo(
                f"{str(member.id).ljust(max_id)}  {member.username.ljust(max_user)}  {member.email}"
            )


@cli.command(name="tags")
@click.argument("space_id")
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
def tags(space_id: str, format: str, raw: bool) -> None:
    """List tags in a space.

    SPACE_ID: The ID of the space.
    """
    try:
        with ClickUpClient() as client:
            data = client.get_space_tags(space_id)

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            tags_list = [Tag(**tag) for tag in data["tags"]]
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()

    if not tags_list:
        click.echo("No tags found.")
        return

    if format == "json":
        output = [
            {
                "name": t.name,
                "foreground_color": t.tag_fg,
                "background_color": t.tag_bg,
            }
            for t in tags_list
        ]
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        # Calculate column widths
        max_name = max(len(t.name) for t in tags_list)

        # Print header
        click.echo(f"{'NAME'.ljust(max_name)}  {'FG COLOR'}  {'BG COLOR'}")
        click.echo("-" * (max_name + 22))

        # Print rows
        for tag in tags_list:
            click.echo(
                f"{tag.name.ljust(max_name)}  {tag.tag_fg.ljust(10)}  {tag.tag_bg}"
            )


@cli.command(name="create-tag")
@click.argument("space_id")
@click.option("--name", required=True, help="Tag name (required).")
@click.option(
    "--fg-color",
    required=True,
    help="Tag foreground color (hex, e.g., #000000).",
)
@click.option(
    "--bg-color",
    required=True,
    help="Tag background color (hex, e.g., #FFFFFF).",
)
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
def create_tag(
    space_id: str, name: str, fg_color: str, bg_color: str, format: str, raw: bool
) -> None:
    """Create a new tag in a space.

    SPACE_ID: The ID of the space to create the tag in.
    """
    try:
        with ClickUpClient() as client:
            data = client.create_space_tag(
                space_id, name=name, tag_fg=fg_color, tag_bg=bg_color
            )

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            if format == "json":
                output = {
                    "name": name,
                    "foreground_color": fg_color,
                    "background_color": bg_color,
                }
                click.echo(json.dumps(output, indent=2))
            elif format == "table":
                click.echo(f"Name:        {name}")
                click.echo(f"FG Color:     {fg_color}")
                click.echo(f"BG Color:     {bg_color}")
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()


@cli.command(name="add-tag")
@click.argument("task_id")
@click.argument("tag_name")
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
def add_tag(task_id: str, tag_name: str, format: str, raw: bool) -> None:
    """Add a tag to a task.

    TASK_ID: The ID of the task to add the tag to.
    TAG_NAME: The name of the tag to add.
    """
    try:
        with ClickUpClient() as client:
            data = client.add_tag_to_task(task_id, tag_name)

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            if format == "json":
                output = {
                    "task_id": task_id,
                    "tag": tag_name,
                }
                click.echo(json.dumps(output, indent=2))
            elif format == "table":
                click.echo(f"Task ID:  {task_id}")
                click.echo(f"Tag:      {tag_name}")
                click.echo("Tag added successfully.")
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()


@cli.command(name="remove-tag")
@click.argument("task_id")
@click.argument("tag_name")
@click.option(
    "--format",
    type=click.Choice(["json", "table"], case_sensitive=False),
    default="json",
    help="Output format.",
)
@click.option("--raw", is_flag=True, help="Output raw JSON without model validation.")
def remove_tag(task_id: str, tag_name: str, format: str, raw: bool) -> None:
    """Remove a tag from a task.

    TASK_ID: The ID of the task to remove the tag from.
    TAG_NAME: The name of the tag to remove.
    """
    try:
        with ClickUpClient() as client:
            data = client.remove_tag_from_task(task_id, tag_name)

            if raw:
                click.echo(json.dumps(data, indent=2))
                return

            if format == "json":
                output = {
                    "task_id": task_id,
                    "tag": tag_name,
                }
                click.echo(json.dumps(output, indent=2))
            elif format == "table":
                click.echo(f"Task ID:  {task_id}")
                click.echo(f"Tag:      {tag_name}")
                click.echo("Tag removed successfully.")
    except httpx.HTTPStatusError as e:
        click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
        raise click.Abort()
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()


def main() -> None:
    """Entry point for the CLI."""
    cli()
