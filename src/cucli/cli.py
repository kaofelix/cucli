"""Click CLI for ClickUp."""

import json

import click
from cucli.api import ClickUpClient, with_client
from cucli.decorators import common_output_options, handle_api_errors
from cucli.helpers import (
    confirm_deletion,
    format_table,
    handle_empty_collection,
    handle_raw_output,
    parse_models_with_raw,
    validate_team_id_for_custom_tasks,
)
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
@common_output_options
@handle_api_errors
def workspaces(format: str, raw: bool) -> None:
    """List your ClickUp workspaces."""
    data = with_client(lambda client: client.get_teams())

    teams = parse_models_with_raw(data, "teams", Team, raw)
    if teams is None:
        return

    if format == "json":
        output = [{"id": t.id, "name": t.name, "color": t.color} for t in teams]
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        format_table(
            teams,
            [
                {"header": "ID", "key": "id"},
                {"header": "NAME", "key": "name"},
                {"header": "COLOR", "key": "color"},
            ],
            empty_message="No workspaces found.",
        )


@cli.command(name="spaces")
@click.argument("team_id")
@common_output_options
@click.option(
    "--archived",
    is_flag=True,
    help="Include archived spaces.",
)
@handle_api_errors
def spaces(team_id: str, format: str, raw: bool, archived: bool) -> None:
    """List spaces in a workspace.

    TEAM_ID: The ID of the team/workspace.
    """
    data = with_client(lambda client: client.get_spaces(team_id, archived=archived))

    spaces_list = parse_models_with_raw(data, "spaces", Space, raw)
    if spaces_list is None:
        return

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
        format_table(
            spaces_list,
            [
                {"header": "ID", "key": "id"},
                {"header": "NAME", "key": "name"},
                {
                    "header": "PRIVATE",
                    "key": "private",
                    "get_value": lambda x: "Yes" if x else "No",
                },
            ],
            empty_message="No spaces found.",
        )


@cli.command(name="folders")
@click.argument("space_id")
@common_output_options
@click.option(
    "--archived",
    is_flag=True,
    help="Include archived folders.",
)
@handle_api_errors
def folders(space_id: str, format: str, raw: bool, archived: bool) -> None:
    """List folders in a space.

    SPACE_ID: The ID of the space.
    """
    data = with_client(lambda client: client.get_folders(space_id, archived=archived))

    folders_list = parse_models_with_raw(data, "folders", Folder, raw)
    if folders_list is None:
        return

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
        format_table(
            folders_list,
            [
                {"header": "ID", "key": "id"},
                {"header": "NAME", "key": "name"},
                {"header": "TASKS", "key": "task_count", "get_value": str},
                {
                    "header": "HIDDEN",
                    "key": "hidden",
                    "get_value": lambda x: "Yes" if x else "No",
                },
            ],
            empty_message="No folders found.",
        )


@cli.command(name="create-folder")
@click.argument("space_id")
@click.option("--name", required=True, help="Folder name (required).")
@common_output_options
@handle_api_errors
def create_folder(space_id: str, name: str, format: str, raw: bool) -> None:
    """Create a new folder in a space.

    SPACE_ID: The ID of the space to create the folder in.
    """
    data = with_client(lambda client: client.create_folder(space_id, name=name))

    if handle_raw_output(data, raw):
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


@cli.command(name="folder")
@click.argument("folder_id")
@common_output_options
@handle_api_errors
def folder(folder_id: str, format: str, raw: bool) -> None:
    """Get details for a specific folder.

    FOLDER_ID: The ID of the folder to retrieve.
    """
    data = with_client(lambda client: client.get_folder(folder_id))

    if handle_raw_output(data, raw):
        return

    if format == "json":
        output = {
            "id": data.get("id"),
            "name": data.get("name"),
            "hidden": data.get("hidden"),
            "task_count": data.get("task_count"),
        }
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        click.echo(f"ID:         {data.get('id')}")
        click.echo(f"Name:       {data.get('name')}")
        click.echo(f"Hidden:     {data.get('hidden')}")
        click.echo(f"Task Count: {data.get('task_count')}")


@cli.command(name="update-folder")
@click.argument("folder_id")
@click.option("--name", required=True, help="New folder name (required).")
@common_output_options
@handle_api_errors
def update_folder_cli(folder_id: str, name: str, format: str, raw: bool) -> None:
    """Update a folder.

    FOLDER_ID: The ID of the folder to update.
    """
    data = with_client(lambda client: client.update_folder(folder_id, name=name))

    if handle_raw_output(data, raw):
        return

    if not data:
        click.echo("No updates provided.")
        return

    if format == "json":
        output = {
            "id": data.get("id"),
            "name": data.get("name"),
        }
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        click.echo(f"Folder {folder_id} updated successfully.")


@cli.command(name="delete-folder")
@click.argument("folder_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation prompt.")
@handle_api_errors
def delete_folder(folder_id: str, yes: bool) -> None:
    """Delete a folder.

    FOLDER_ID: The ID of the folder to delete.
    """
    if not confirm_deletion("folder", folder_id, yes):
        return

    with_client(lambda client: client.delete_folder(folder_id))
    click.echo(f"Folder {folder_id} deleted successfully.")


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
@common_output_options
@handle_api_errors
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

        if handle_raw_output(data, raw):
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


@cli.command(name="lists")
@click.argument("folder_id")
@common_output_options
@click.option(
    "--archived",
    is_flag=True,
    help="Include archived lists.",
)
@handle_api_errors
def lists(folder_id: str, format: str, raw: bool, archived: bool) -> None:
    """List lists in a folder.

    FOLDER_ID: The ID of the folder.
    """
    data = with_client(lambda client: client.get_lists(folder_id, archived=archived))

    lists_list = parse_models_with_raw(data, "lists", ClickUpList, raw)
    if lists_list is None:
        return

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
        format_table(
            lists_list,
            [
                {"header": "ID", "key": "id"},
                {"header": "NAME", "key": "name"},
                {"header": "TASKS", "key": "task_count", "get_value": str},
                {
                    "header": "ARCHIVED",
                    "key": "archived",
                    "get_value": lambda x: "Yes" if x else "No",
                },
            ],
            empty_message="No lists found.",
        )


@cli.command(name="list")
@click.argument("list_id")
@common_output_options
@handle_api_errors
def get_list_cli(list_id: str, format: str, raw: bool) -> None:
    """Get details for a specific list.

    LIST_ID: The ID of list to retrieve.
    """
    data = with_client(lambda client: client.get_list(list_id))

    if handle_raw_output(data, raw):
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
            "task_count": data.get("task_count"),
            "archived": data.get("archived"),
        }
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        click.echo(f"ID:         {data.get('id')}")
        click.echo(f"Name:       {data.get('name')}")
        if data.get("status"):
            click.echo(f"Status:     {data.get('status', {}).get('status')}")
        if data.get("priority"):
            click.echo(f"Priority:   {data.get('priority', {}).get('priority')}")
        click.echo(f"Task Count: {data.get('task_count')}")
        click.echo(f"Archived:   {data.get('archived')}")


@cli.command(name="update-list")
@click.argument("list_id")
@click.option("--name", help="New list name.")
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
@click.option("--assignee", type=int, help="Assignee user ID.")
@click.option("--status", help="List status (color).")
@click.option("--unset-status", is_flag=True, help="Remove list status (color).")
@common_output_options
@handle_api_errors
def update_list_cli(
    list_id: str,
    name: str | None,
    description: str | None,
    markdown_description: str | None,
    due_date: int | None,
    due_date_time: bool,
    priority: int | None,
    assignee: int | None,
    status: str | None,
    unset_status: bool,
    format: str,
    raw: bool,
) -> None:
    """Update a list.

    LIST_ID: The ID of list to update.
    """
    with ClickUpClient() as client:
        data = client.update_list(
            list_id,
            name=name,
            content=description,
            markdown_content=markdown_description,
            due_date=due_date,
            due_date_time=due_date_time,
            priority=priority,
            assignee=assignee,
            status=status,
            unset_status=unset_status,
        )

        if handle_raw_output(data, raw):
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
            }
            click.echo(json.dumps(output, indent=2))
        elif format == "table":
            click.echo(f"ID:      {data.get('id')}")
            click.echo(f"Name:    {data.get('name')}")
            if data.get("status"):
                click.echo(f"Status:  {data.get('status', {}).get('status')}")
            if data.get("priority"):
                click.echo(f"Priority: {data.get('priority', {}).get('priority')}")
            click.echo("Updated successfully.")


@cli.command(name="delete-list")
@click.argument("list_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation prompt.")
@handle_api_errors
def delete_list(list_id: str, yes: bool) -> None:
    """Delete a list.

    LIST_ID: The ID of list to delete.
    """
    if not confirm_deletion("list", list_id, yes):
        return

    with_client(lambda client: client.delete_list(list_id))
    click.echo(f"List {list_id} deleted successfully.")


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
@handle_api_errors
def task(task_id: str, format: str, raw: bool, md_only: bool) -> None:
    """Get details for a specific task.

    TASK_ID: The ID of the task to retrieve.
    """
    data = with_client(lambda client: client.get_task(task_id))

    if handle_raw_output(data, raw):
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
            "priority": task.priority.get("priority") if task.priority else None,
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
            click.echo(f"Tags:     {', '.join(t.get('name', '') for t in task.tags)}")
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


@cli.command(name="tasks")
@click.argument("team_id")
@common_output_options
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
@handle_api_errors
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
    data = with_client(
        lambda client: client.get_team_tasks(
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
    )

    if handle_raw_output(data, raw):
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
                    "status": task.status.get("status") if task.status else None,
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
        format_table(
            tasks_list,
            [
                {"header": "ID", "key": "id"},
                {"header": "NAME", "key": "name"},
                {
                    "header": "STATUS",
                    "key": "status",
                    "get_value": lambda x: x.get("status", "") if x else "",
                },
            ],
            empty_message="No tasks found.",
        )


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
@common_output_options
@handle_api_errors
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

        if handle_raw_output(data, raw):
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
@common_output_options
@handle_api_errors
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

        if handle_raw_output(data, raw):
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


@cli.command(name="delete-task")
@click.argument("task_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation prompt.")
@handle_api_errors
def delete_task(task_id: str, yes: bool) -> None:
    """Delete a task.

    TASK_ID: The ID of the task to delete.
    """
    if not confirm_deletion("task", task_id, yes):
        return

    with_client(lambda client: client.delete_task(task_id))
    click.echo(f"Task {task_id} deleted successfully.")


@cli.command(name="task-comments")
@click.argument("task_id")
@common_output_options
@handle_api_errors
def task_comments(task_id: str, format: str, raw: bool) -> None:
    """List comments on a task.

    TASK_ID: The ID of the task to get comments from.
    """
    data = with_client(lambda client: client.get_task_comments(task_id))

    comments = parse_models_with_raw(data, "comments", Comment, raw)
    if comments is None:
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
        format_table(
            comments,
            [
                {"header": "ID", "key": "id"},
                {"header": "USER", "key": "user.username"},
                {
                    "header": "TEXT",
                    "key": "comment_text",
                    "get_value": lambda x: x[:30] + "..." if len(x) > 30 else x,
                },
                {
                    "header": "RESOLVED",
                    "key": "resolved",
                    "get_value": lambda x: "Yes" if x else "No",
                },
            ],
            empty_message="No comments found.",
        )


@cli.command(name="add-comment")
@click.argument("task_id")
@click.option("--text", required=True, help="Comment text (required).")
@click.option("--assignee", type=int, help="Assignee user ID to assign the comment to.")
@click.option(
    "--no-notify", is_flag=True, help="Don't notify everyone (default: notify all)."
)
@common_output_options
@handle_api_errors
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
    with ClickUpClient() as client:
        data = client.create_task_comment(
            task_id, comment_text=text, assignee=assignee, notify_all=not no_notify
        )

        if handle_raw_output(data, raw):
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


@cli.command(name="list-comments")
@click.argument("list_id")
@common_output_options
@handle_api_errors
def list_comments(list_id: str, format: str, raw: bool) -> None:
    """List comments on a list.

    LIST_ID: The ID of the list to get comments from.
    """
    data = with_client(lambda client: client.get_list_comments(list_id))

    comments = parse_models_with_raw(data, "comments", Comment, raw)
    if comments is None:
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
        format_table(
            comments,
            [
                {"header": "ID", "key": "id"},
                {"header": "USER", "key": "user.username"},
                {
                    "header": "TEXT",
                    "key": "comment_text",
                    "get_value": lambda x: x[:30] + "..." if len(x) > 30 else x,
                },
                {
                    "header": "RESOLVED",
                    "key": "resolved",
                    "get_value": lambda x: "Yes" if x else "No",
                },
            ],
            empty_message="No comments found.",
        )


@cli.command(name="add-list-comment")
@click.argument("list_id")
@click.option("--text", required=True, help="Comment text (required).")
@click.option("--assignee", type=int, help="Assignee user ID to assign the comment to.")
@click.option(
    "--no-notify", is_flag=True, help="Don't notify everyone (default: notify all)."
)
@common_output_options
@handle_api_errors
def add_list_comment(
    list_id: str,
    text: str,
    assignee: int | None,
    no_notify: bool,
    format: str,
    raw: bool,
) -> None:
    """Add a comment to a list.

    LIST_ID: The ID of the list to add a comment to.
    """
    with ClickUpClient() as client:
        data = client.create_list_comment(
            list_id, comment_text=text, assignee=assignee, notify_all=not no_notify
        )

        if handle_raw_output(data, raw):
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


@cli.command(name="create-checklist")
@click.argument("task_id")
@click.option("--name", required=True, help="Checklist name (required).")
@common_output_options
@handle_api_errors
def create_checklist(task_id: str, name: str, format: str, raw: bool) -> None:
    """Create a new checklist on a task.

    TASK_ID: The ID of the task to create the checklist on.
    """
    data = with_client(lambda client: client.create_checklist(task_id, name=name))

    if handle_raw_output(data, raw):
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


@cli.command(name="create-checklist-item")
@click.argument("checklist_id")
@click.option("--name", required=True, help="Checklist item name (required).")
@click.option("--assignee", type=int, help="Assignee user ID.")
@common_output_options
@handle_api_errors
def create_checklist_item(
    checklist_id: str, name: str, assignee: int | None, format: str, raw: bool
) -> None:
    """Create a new item in a checklist.

    CHECKLIST_ID: The ID of the checklist to add the item to.
    """
    data = with_client(
        lambda client: client.create_checklist_item(
            checklist_id, name=name, assignee=assignee
        )
    )

    if handle_raw_output(data, raw):
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


@cli.command(name="update-checklist")
@click.argument("checklist_id")
@click.option("--name", help="Checklist name.")
@click.option(
    "--position",
    type=int,
    help="Position of the checklist (order).",
)
@common_output_options
@handle_api_errors
def update_checklist(
    checklist_id: str, name: str | None, position: int | None, format: str, raw: bool
) -> None:
    """Update a checklist.

    CHECKLIST_ID: The ID of the checklist to update.
    """
    data = with_client(
        lambda client: client.update_checklist(
            checklist_id, name=name, position=position
        )
    )

    if handle_raw_output(data, raw):
        return

    if not data:
        click.echo("No updates provided.")
        return

    if format == "json":
        click.echo(json.dumps(data, indent=2))
    elif format == "table":
        click.echo(f"Checklist {checklist_id} updated successfully.")


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
@common_output_options
@handle_api_errors
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
    with ClickUpClient() as client:
        data = client.update_checklist_item(
            checklist_id,
            checklist_item_id,
            name=name,
            assignee=assignee,
            resolved=resolved,
            parent=parent,
        )

        if handle_raw_output(data, raw):
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


@cli.command(name="delete-checklist")
@click.argument("checklist_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation prompt.")
@handle_api_errors
def delete_checklist(checklist_id: str, yes: bool) -> None:
    """Delete a checklist.

    CHECKLIST_ID: The ID of the checklist to delete.
    """
    if not confirm_deletion("checklist", checklist_id, yes):
        return

    with_client(lambda client: client.delete_checklist(checklist_id))
    click.echo(f"Checklist {checklist_id} deleted successfully.")


@cli.command(name="delete-checklist-item")
@click.argument("checklist_id")
@click.argument("checklist_item_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation prompt.")
@handle_api_errors
def delete_checklist_item(checklist_id: str, checklist_item_id: str, yes: bool) -> None:
    """Delete a checklist item.

    CHECKLIST_ID: The ID of the checklist.
    CHECKLIST_ITEM_ID: The ID of the checklist item to delete.
    """
    if not confirm_deletion("checklist item", checklist_item_id, yes):
        return

    with_client(
        lambda client: client.delete_checklist_item(checklist_id, checklist_item_id)
    )
    click.echo(
        f"Checklist item {checklist_item_id} deleted successfully from checklist {checklist_id}."
    )


@cli.command(name="task-members")
@click.argument("task_id")
@common_output_options
@handle_api_errors
def task_members(task_id: str, format: str, raw: bool) -> None:
    """Get members with explicit access to a task.

    TASK_ID: The ID of the task to get members from.
    """
    data = with_client(lambda client: client.get_task_members(task_id))

    members = parse_models_with_raw(data, "members", TaskMember, raw)
    if members is None:
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
        format_table(
            members,
            [
                {"header": "ID", "key": "id", "get_value": str},
                {"header": "USERNAME", "key": "username"},
                {"header": "EMAIL", "key": "email"},
            ],
            empty_message="No members found.",
        )


@cli.command(name="list-members")
@click.argument("list_id")
@common_output_options
@handle_api_errors
def list_members(list_id: str, format: str, raw: bool) -> None:
    """Get members with explicit access to a list.

    LIST_ID: The ID of the list to get members from.
    """
    data = with_client(lambda client: client.get_list_members(list_id))

    members = parse_models_with_raw(data, "members", ListMember, raw)
    if members is None:
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
        format_table(
            members,
            [
                {"header": "ID", "key": "id", "get_value": str},
                {"header": "USERNAME", "key": "username"},
                {"header": "EMAIL", "key": "email"},
            ],
            empty_message="No members found.",
        )


@cli.command(name="tags")
@click.argument("space_id")
@common_output_options
@handle_api_errors
def tags(space_id: str, format: str, raw: bool) -> None:
    """List tags in a space.

    SPACE_ID: The ID of the space.
    """
    data = with_client(lambda client: client.get_space_tags(space_id))

    tags_list = parse_models_with_raw(data, "tags", Tag, raw)
    if tags_list is None:
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
        format_table(
            tags_list,
            [
                {"header": "NAME", "key": "name"},
                {"header": "FG COLOR", "key": "tag_fg", "width": 10},
                {"header": "BG COLOR", "key": "tag_bg"},
            ],
            empty_message="No tags found.",
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
@common_output_options
@handle_api_errors
def create_tag(
    space_id: str, name: str, fg_color: str, bg_color: str, format: str, raw: bool
) -> None:
    """Create a new tag in a space.

    SPACE_ID: The ID of the space to create the tag in.
    """
    with ClickUpClient() as client:
        data = client.create_space_tag(
            space_id, name=name, tag_fg=fg_color, tag_bg=bg_color
        )

        if handle_raw_output(data, raw):
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


@cli.command(name="add-tag")
@click.argument("task_id")
@click.argument("tag_name")
@common_output_options
@handle_api_errors
def add_tag(task_id: str, tag_name: str, format: str, raw: bool) -> None:
    """Add a tag to a task.

    TASK_ID: The ID of the task to add the tag to.
    TAG_NAME: The name of the tag to add.
    """
    data = with_client(lambda client: client.add_tag_to_task(task_id, tag_name))

    if handle_raw_output(data, raw):
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


@cli.command(name="remove-tag")
@click.argument("task_id")
@click.argument("tag_name")
@common_output_options
@handle_api_errors
def remove_tag(task_id: str, tag_name: str, format: str, raw: bool) -> None:
    """Remove a tag from a task.

    TASK_ID: The ID of the task to remove the tag from.
    TAG_NAME: The name of the tag to remove.
    """
    data = with_client(lambda client: client.remove_tag_from_task(task_id, tag_name))

    if handle_raw_output(data, raw):
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


@cli.command(name="running-time-entry")
@click.argument("team_id")
@common_output_options
@handle_api_errors
def running_time_entry(team_id: str, format: str, raw: bool) -> None:
    """Get the currently running time entry.

    TEAM_ID: The ID of the team/workspace.
    """
    data = with_client(lambda client: client.get_running_time_entry(team_id))

    if handle_raw_output(data, raw):
        return

    entry = data.get("data", {})

    if not entry:
        click.echo("No running timer found.")
        return

    if format == "json":
        output = {
            "id": entry.get("id"),
            "wid": entry.get("wid"),
            "start": entry.get("start"),
            "duration": entry.get("duration"),
            "description": entry.get("description"),
            "task_id": entry.get("task", {}).get("id") if entry.get("task") else None,
        }
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        click.echo(f"ID:          {entry.get('id')}")
        click.echo(f"Start:       {entry.get('start')}")
        click.echo(f"Duration:    {entry.get('duration')}")
        if entry.get("description"):
            click.echo(f"Description: {entry.get('description')}")
        if entry.get("task"):
            click.echo(f"Task ID:     {entry.get('task', {}).get('id')}")


@cli.command(name="start-time-entry")
@click.argument("team_id")
@click.option("--description", help="Time entry description.")
@click.option("--task-id", help="Task ID to associate with the time entry.")
@click.option("--billable", is_flag=True, help="Mark the time entry as billable.")
@common_output_options
@handle_api_errors
def start_time_entry(
    team_id: str,
    description: str | None,
    task_id: str | None,
    billable: bool,
    format: str,
    raw: bool,
) -> None:
    """Start a time entry.

    TEAM_ID: The ID of the team/workspace.
    """
    with ClickUpClient() as client:
        data = client.start_time_entry(
            team_id, task_id=task_id, description=description, billable=billable
        )

        if handle_raw_output(data, raw):
            return

        entry = data.get("data", {})

        if format == "json":
            output = {
                "id": entry.get("id"),
                "wid": entry.get("wid"),
                "start": entry.get("start"),
                "duration": entry.get("duration"),
                "description": entry.get("description"),
                "task_id": entry.get("task", {}).get("id")
                if entry.get("task")
                else None,
            }
            click.echo(json.dumps(output, indent=2))
        elif format == "table":
            click.echo(f"ID:          {entry.get('id')}")
            click.echo(f"Start:       {entry.get('start')}")
            click.echo(f"Duration:    {entry.get('duration')}")
            if entry.get("description"):
                click.echo(f"Description: {entry.get('description')}")
            if entry.get("task"):
                click.echo(f"Task ID:     {entry.get('task', {}).get('id')}")
            click.echo("Timer started successfully.")


@cli.command(name="stop-time-entry")
@click.argument("team_id")
@common_output_options
@handle_api_errors
def stop_time_entry(team_id: str, format: str, raw: bool) -> None:
    """Stop the currently running time entry.

    TEAM_ID: The ID of the team/workspace.
    """
    data = with_client(lambda client: client.stop_time_entry(team_id))

    if handle_raw_output(data, raw):
        return

    entry = data.get("data", {})

    if format == "json":
        output = {
            "id": entry.get("id"),
            "wid": entry.get("wid"),
            "start": entry.get("start"),
            "end": entry.get("end"),
            "duration": entry.get("duration"),
            "description": entry.get("description"),
            "task_id": entry.get("task", {}).get("id") if entry.get("task") else None,
        }
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        click.echo(f"ID:          {entry.get('id')}")
        click.echo(f"Start:       {entry.get('start')}")
        click.echo(f"End:         {entry.get('end')}")
        click.echo(f"Duration:    {entry.get('duration')}")
        if entry.get("description"):
            click.echo(f"Description: {entry.get('description')}")
        if entry.get("task"):
            click.echo(f"Task ID:     {entry.get('task', {}).get('id')}")
        click.echo("Timer stopped successfully.")


@cli.command(name="time-entries")
@click.argument("team_id")
@click.option(
    "--start-date", type=int, help="Start date as Unix timestamp in milliseconds."
)
@click.option(
    "--end-date", type=int, help="End date as Unix timestamp in milliseconds."
)
@click.option("--assignee", type=int, help="Filter by assignee user ID.")
@click.option("--space-id", type=int, help="Filter by space ID.")
@click.option("--folder-id", type=int, help="Filter by folder ID.")
@click.option("--list-id", type=int, help="Filter by list ID.")
@click.option("--task-id", help="Filter by task ID.")
@click.option("--billable", is_flag=True, help="Filter by billable entries.")
@common_output_options
@handle_api_errors
def time_entries(
    team_id: str,
    start_date: int | None,
    end_date: int | None,
    assignee: int | None,
    space_id: int | None,
    folder_id: int | None,
    list_id: int | None,
    task_id: str | None,
    billable: bool,
    format: str,
    raw: bool,
) -> None:
    """List time entries within a date range.

    TEAM_ID: The ID of the team/workspace.
    """
    with ClickUpClient() as client:
        data = client.get_time_entries(
            team_id,
            start_date=start_date,
            end_date=end_date,
            assignee=assignee,
            space_id=space_id,
            folder_id=folder_id,
            list_id=list_id,
            task_id=task_id,
            is_billable=billable if billable else None,
        )

        if handle_raw_output(data, raw):
            return

        entries = data.get("data", [])

        if handle_empty_collection(entries, format, "No time entries found."):
            return

        if format == "json":
            output = []
            for entry in entries:
                output.append(
                    {
                        "id": entry.get("id"),
                        "wid": entry.get("wid"),
                        "start": entry.get("start"),
                        "duration": entry.get("duration"),
                        "description": entry.get("description"),
                        "task_id": entry.get("task", {}).get("id")
                        if entry.get("task")
                        else None,
                    }
                )
            click.echo(json.dumps(output, indent=2))
        elif format == "table":
            format_table(
                entries,
                [
                    {"header": "ID", "key": "id", "get_value": str},
                    {
                        "header": "DESCRIPTION",
                        "key": "description",
                        "get_value": lambda x: x[:30] + "..."
                        if x and len(x) > 30
                        else x or "",
                    },
                    {
                        "header": "DURATION",
                        "key": "duration",
                        "get_value": lambda x: f"{x / 3600000:.2f}h" if x else "0h",
                    },
                ],
            )


@cli.command(name="create-time-entry")
@click.argument("team_id")
@click.option(
    "--start",
    type=int,
    required=True,
    help="Start time as Unix timestamp in milliseconds (required).",
)
@click.option(
    "--duration", type=int, required=True, help="Duration in milliseconds (required)."
)
@click.option("--description", help="Time entry description.")
@click.option("--task-id", help="Task ID to associate with the time entry.")
@click.option("--billable", is_flag=True, help="Mark the time entry as billable.")
@common_output_options
@handle_api_errors
def create_time_entry(
    team_id: str,
    start: int,
    duration: int,
    description: str | None,
    task_id: str | None,
    billable: bool,
    format: str,
    raw: bool,
) -> None:
    """Create a manual time entry.

    TEAM_ID: The ID of the team/workspace.
    """
    with ClickUpClient() as client:
        data = client.create_time_entry(
            team_id,
            start=start,
            duration=duration,
            description=description,
            task_id=task_id,
            billable=billable,
        )

        if handle_raw_output(data, raw):
            return

        entry = data.get("data", {})

        if format == "json":
            output = {
                "id": entry.get("id"),
                "wid": entry.get("wid"),
                "start": entry.get("start"),
                "duration": entry.get("duration"),
                "description": entry.get("description"),
                "task_id": entry.get("task", {}).get("id")
                if entry.get("task")
                else None,
            }
            click.echo(json.dumps(output, indent=2))
        elif format == "table":
            click.echo(f"ID:          {entry.get('id')}")
            click.echo(f"Start:       {entry.get('start')}")
            click.echo(f"Duration:    {entry.get('duration')}")
            if entry.get("description"):
                click.echo(f"Description: {entry.get('description')}")
            if entry.get("task"):
                click.echo(f"Task ID:     {entry.get('task', {}).get('id')}")
            click.echo("Time entry created successfully.")


@cli.command(name="update-time-entry")
@click.argument("team_id")
@click.argument("timer_id")
@click.option("--description", help="Time entry description.")
@click.option("--start", type=int, help="Start time as Unix timestamp in milliseconds.")
@click.option("--end", type=int, help="End time as Unix timestamp in milliseconds.")
@click.option("--duration", type=int, help="Duration in milliseconds.")
@click.option("--task-id", help="Task ID to associate with the time entry.")
@click.option("--billable", is_flag=True, help="Mark the time entry as billable.")
@common_output_options
def update_time_entry(
    team_id: str,
    timer_id: str,
    description: str | None,
    start: int | None,
    end: int | None,
    duration: int | None,
    task_id: str | None,
    billable: bool,
    format: str,
    raw: bool,
) -> None:
    """Update a time entry.

    TEAM_ID: The ID of the team/workspace.
    TIMER_ID: The ID of the time entry to update.
    """
    with ClickUpClient() as client:
        data = client.update_time_entry(
            team_id,
            timer_id,
            description=description,
            start=start,
            end=end,
            duration=duration,
            task_id=task_id,
            billable=billable if billable else None,
        )

        if handle_raw_output(data, raw):
            return

        entry = data.get("data", {})

        if format == "json":
            output = {
                "id": entry.get("id"),
                "wid": entry.get("wid"),
                "start": entry.get("start"),
                "duration": entry.get("duration"),
                "description": entry.get("description"),
                "task_id": entry.get("task", {}).get("id")
                if entry.get("task")
                else None,
                "billable": entry.get("billable"),
            }
            click.echo(json.dumps(output, indent=2))
        elif format == "table":
            click.echo(f"ID:          {entry.get('id')}")
            click.echo(f"Start:       {entry.get('start')}")
            click.echo(f"Duration:    {entry.get('duration')}")
            if entry.get("description"):
                click.echo(f"Description: {entry.get('description')}")
            if entry.get("task"):
                click.echo(f"Task ID:     {entry.get('task', {}).get('id')}")
            click.echo("Time entry updated successfully.")


@cli.command(name="delete-time-entry")
@click.argument("team_id")
@click.argument("timer_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation prompt.")
@handle_api_errors
def delete_time_entry(team_id: str, timer_id: str, yes: bool) -> None:
    """Delete a time entry.

    TEAM_ID: The ID of the team/workspace.
    TIMER_ID: The ID of the time entry to delete.
    """
    if not confirm_deletion("time entry", timer_id, yes):
        return

    with_client(lambda client: client.delete_time_entry(team_id, timer_id))
    click.echo(f"Time entry {timer_id} deleted successfully.")


@cli.command(name="add-dependency")
@click.argument("task_id")
@click.option(
    "--depends-on",
    "depends_on",
    help="Task ID that must be completed before this task can start.",
)
@click.option(
    "--dependency-of",
    "dependency_of",
    help="Task ID that is waiting for this task to be completed.",
)
@click.option(
    "--custom-task-ids",
    is_flag=True,
    help="Use custom task IDs instead of default task IDs.",
)
@click.option("--team-id", help="Workspace ID (required when using --custom-task-ids).")
@common_output_options
@handle_api_errors
def add_dependency(
    task_id: str,
    depends_on: str | None,
    dependency_of: str | None,
    custom_task_ids: bool,
    team_id: str | None,
    format: str,
    raw: bool,
) -> None:
    """Add a dependency between tasks.

    TASK_ID: The task ID to add the dependency to.
    """
    if not depends_on and not dependency_of:
        click.echo(
            "Error: Either --depends-on or --dependency-of must be specified.",
            err=True,
        )
        raise click.Abort()

    validate_team_id_for_custom_tasks(custom_task_ids, team_id)

    with ClickUpClient() as client:
        data = client.add_dependency(
            task_id,
            depends_on=depends_on,
            dependency_of=dependency_of,
            custom_task_ids=custom_task_ids,
            team_id=team_id,
        )

        if handle_raw_output(data, raw):
            return

        if format == "json":
            output = {"task_id": task_id}
            if depends_on:
                output["depends_on"] = depends_on
            if dependency_of:
                output["dependency_of"] = dependency_of
            click.echo(json.dumps(output, indent=2))
        elif format == "table":
            click.echo(f"Task ID:     {task_id}")
            if depends_on:
                click.echo(f"Depends On:   {depends_on}")
            if dependency_of:
                click.echo(f"Dependency Of: {dependency_of}")
            click.echo("Dependency added successfully.")


@cli.command(name="delete-dependency")
@click.argument("task_id")
@click.option(
    "--depends-on",
    "depends_on",
    help="Task ID to remove from depends_on relationship.",
)
@click.option(
    "--dependency-of",
    "dependency_of",
    help="Task ID to remove from dependency_of relationship.",
)
@click.option(
    "--custom-task-ids",
    is_flag=True,
    help="Use custom task IDs instead of default task IDs.",
)
@click.option("--team-id", help="Workspace ID (required when using --custom-task-ids).")
@common_output_options
@handle_api_errors
def delete_dependency(
    task_id: str,
    depends_on: str | None,
    dependency_of: str | None,
    custom_task_ids: bool,
    team_id: str | None,
    format: str,
    raw: bool,
) -> None:
    """Delete a dependency between tasks.

    TASK_ID: The task ID to remove the dependency from.
    """
    if not depends_on and not dependency_of:
        click.echo(
            "Error: Either --depends-on or --dependency-of must be specified.",
            err=True,
        )
        raise click.Abort()

    validate_team_id_for_custom_tasks(custom_task_ids, team_id)

    with ClickUpClient() as client:
        data = client.delete_dependency(
            task_id,
            depends_on=depends_on,
            dependency_of=dependency_of,
            custom_task_ids=custom_task_ids,
            team_id=team_id,
        )

        if handle_raw_output(data, raw):
            return

        if format == "json":
            output = {"task_id": task_id}
            if depends_on:
                output["depends_on"] = depends_on
            if dependency_of:
                output["dependency_of"] = dependency_of
            click.echo(json.dumps(output, indent=2))
        elif format == "table":
            click.echo(f"Task ID:     {task_id}")
            if depends_on:
                click.echo(f"Depends On:   {depends_on}")
            if dependency_of:
                click.echo(f"Dependency Of: {dependency_of}")
            click.echo("Dependency deleted successfully.")


@cli.command(name="add-link")
@click.argument("task_id")
@click.option(
    "--links-to",
    "links_to",
    help="Task ID to link to.",
)
@click.option(
    "--custom-task-ids",
    is_flag=True,
    help="Use custom task IDs instead of default task IDs.",
)
@click.option("--team-id", help="Workspace ID (required when using --custom-task-ids).")
@common_output_options
@handle_api_errors
def add_link(
    task_id: str,
    links_to: str | None,
    custom_task_ids: bool,
    team_id: str | None,
    format: str,
    raw: bool,
) -> None:
    """Add a link between two tasks.

    TASK_ID: The task ID to initiate the link from.
    """
    if not links_to:
        click.echo(
            "Error: Either --links-to must be specified.",
            err=True,
        )
        raise click.Abort()

    validate_team_id_for_custom_tasks(custom_task_ids, team_id)

    with ClickUpClient() as client:
        data = client.add_task_link(
            task_id,
            links_to=links_to,
            custom_task_ids=custom_task_ids,
            team_id=team_id,
        )

        if handle_raw_output(data, raw):
            return

        if format == "json":
            output = {"task_id": task_id, "links_to": links_to}
            click.echo(json.dumps(output, indent=2))
        elif format == "table":
            click.echo(f"Task ID:   {task_id}")
            click.echo(f"Links To:  {links_to}")
            click.echo("Link added successfully.")


@cli.command(name="delete-link")
@click.argument("task_id")
@click.option(
    "--links-to",
    "links_to",
    help="Task ID to unlink from.",
)
@click.option(
    "--custom-task-ids",
    is_flag=True,
    help="Use custom task IDs instead of default task IDs.",
)
@click.option("--team-id", help="Workspace ID (required when using --custom-task-ids).")
@common_output_options
@handle_api_errors
def delete_link(
    task_id: str,
    links_to: str | None,
    custom_task_ids: bool,
    team_id: str | None,
    format: str,
    raw: bool,
) -> None:
    """Delete a link between two tasks.

    TASK_ID: The task ID to remove the link from.
    """
    if not links_to:
        click.echo(
            "Error: Either --links-to must be specified.",
            err=True,
        )
        raise click.Abort()

    validate_team_id_for_custom_tasks(custom_task_ids, team_id)

    with ClickUpClient() as client:
        data = client.delete_task_link(
            task_id,
            links_to=links_to,
            custom_task_ids=custom_task_ids,
            team_id=team_id,
        )

        if handle_raw_output(data, raw):
            return

        if format == "json":
            output = {"task_id": task_id, "links_to": links_to}
            click.echo(json.dumps(output, indent=2))
        elif format == "table":
            click.echo(f"Task ID:   {task_id}")
            click.echo(f"Links To:  {links_to}")
            click.echo("Link deleted successfully.")


@cli.command(name="create-attachment")
@click.argument("task_id")
@click.option(
    "--file",
    "file_path",
    required=True,
    help="Path to the file to upload (required).",
)
@click.option(
    "--custom-task-ids",
    is_flag=True,
    help="Use custom task IDs instead of default task IDs.",
)
@click.option("--team-id", help="Workspace ID (required when using --custom-task-ids).")
@common_output_options
@handle_api_errors
def create_attachment(
    task_id: str,
    file_path: str,
    custom_task_ids: bool,
    team_id: str | None,
    format: str,
    raw: bool,
) -> None:
    """Upload a file as an attachment to a task.

    TASK_ID: The task ID to attach the file to.
    """
    validate_team_id_for_custom_tasks(custom_task_ids, team_id)

    with ClickUpClient() as client:
        data = client.create_task_attachment(
            task_id,
            attachment_path=file_path,
            custom_task_ids=custom_task_ids,
            team_id=team_id,
        )

        if handle_raw_output(data, raw):
            return

        if format == "json":
            output = {
                "id": data.get("id"),
                "title": data.get("title"),
                "url": data.get("url"),
                "extension": data.get("extension"),
            }
            click.echo(json.dumps(output, indent=2))
        elif format == "table":
            click.echo(f"ID:         {data.get('id')}")
            click.echo(f"Title:      {data.get('title')}")
            click.echo(f"Extension:  {data.get('extension')}")
            click.echo(f"URL:        {data.get('url')}")
            click.echo("\nAttachment uploaded successfully.")


@cli.command(name="team-views")
@click.argument("team_id")
@common_output_options
@handle_api_errors
def team_views(team_id: str, format: str, raw: bool) -> None:
    """List views in a workspace (team).

    TEAM_ID: The ID of team/workspace.
    """
    data = with_client(lambda client: client.get_team_views(team_id))

    if handle_raw_output(data, raw):
        return

    views_list = data.get("views", [])

    if format == "json":
        output = [
            {
                "id": view.get("id"),
                "name": view.get("name"),
                "type": view.get("type"),
            }
            for view in views_list
        ]
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        format_table(
            views_list,
            [
                {"header": "ID", "key": "id", "get_value": str},
                {"header": "NAME", "key": "name"},
                {"header": "TYPE", "key": "type"},
            ],
            empty_message="No views found.",
        )


@cli.command(name="space-views")
@click.argument("space_id")
@common_output_options
@handle_api_errors
def space_views(space_id: str, format: str, raw: bool) -> None:
    """List views in a space.

    SPACE_ID: The ID of space.
    """
    data = with_client(lambda client: client.get_space_views(space_id))

    if handle_raw_output(data, raw):
        return

    views_list = data.get("views", [])

    if format == "json":
        output = [
            {
                "id": view.get("id"),
                "name": view.get("name"),
                "type": view.get("type"),
            }
            for view in views_list
        ]
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        format_table(
            views_list,
            [
                {"header": "ID", "key": "id", "get_value": str},
                {"header": "NAME", "key": "name"},
                {"header": "TYPE", "key": "type"},
            ],
            empty_message="No views found.",
        )


@cli.command(name="folder-views")
@click.argument("folder_id")
@common_output_options
@handle_api_errors
def folder_views(folder_id: str, format: str, raw: bool) -> None:
    """List views in a folder.

    FOLDER_ID: The ID of folder.
    """
    data = with_client(lambda client: client.get_folder_views(folder_id))

    if handle_raw_output(data, raw):
        return

    views_list = data.get("views", [])

    if format == "json":
        output = [
            {
                "id": view.get("id"),
                "name": view.get("name"),
                "type": view.get("type"),
            }
            for view in views_list
        ]
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        format_table(
            views_list,
            [
                {"header": "ID", "key": "id", "get_value": str},
                {"header": "NAME", "key": "name"},
                {"header": "TYPE", "key": "type"},
            ],
            empty_message="No views found.",
        )


@cli.command(name="list-views")
@click.argument("list_id")
@common_output_options
@handle_api_errors
def list_views(list_id: str, format: str, raw: bool) -> None:
    """List views in a list.

    LIST_ID: The ID of list.
    """
    data = with_client(lambda client: client.get_list_views(list_id))

    if handle_raw_output(data, raw):
        return

    views_list = data.get("views", [])

    if format == "json":
        output = [
            {
                "id": view.get("id"),
                "name": view.get("name"),
                "type": view.get("type"),
            }
            for view in views_list
        ]
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        format_table(
            views_list,
            [
                {"header": "ID", "key": "id", "get_value": str},
                {"header": "NAME", "key": "name"},
                {"header": "TYPE", "key": "type"},
            ],
            empty_message="No views found.",
        )


@cli.command(name="view")
@click.argument("view_id")
@common_output_options
@handle_api_errors
def view(view_id: str, format: str, raw: bool) -> None:
    """Get details for a specific view.

    VIEW_ID: The ID of the view to retrieve.
    """
    data = with_client(lambda client: client.get_view(view_id))

    if handle_raw_output(data, raw):
        return

    view_data = data.get("view", data)  # Some responses have view wrapped, some don't

    if format == "json":
        output = {
            "id": view_data.get("id"),
            "name": view_data.get("name"),
            "type": view_data.get("type"),
            "parent": view_data.get("parent"),
        }
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        click.echo(f"ID:     {view_data.get('id')}")
        click.echo(f"Name:   {view_data.get('name')}")
        click.echo(f"Type:   {view_data.get('type')}")
        parent = view_data.get("parent")
        if parent:
            click.echo(f"Parent: {parent}")


@cli.command(name="webhooks")
@click.argument("team_id")
@common_output_options
@handle_api_errors
def webhooks(team_id: str, format: str, raw: bool) -> None:
    """List webhooks in a workspace.

    TEAM_ID: The ID of the team/workspace.
    """
    data = with_client(lambda client: client.get_webhooks(team_id))

    if handle_raw_output(data, raw):
        return

    webhooks_list = data.get("webhooks", [])

    if format == "json":
        output = [
            {
                "id": w.get("id"),
                "endpoint": w.get("endpoint"),
                "events": len(w.get("events", [])),
                "health": w.get("health", {}).get("status"),
            }
            for w in webhooks_list
        ]
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        format_table(
            webhooks_list,
            [
                {"header": "ID", "key": "id"},
                {"header": "ENDPOINT", "key": "endpoint"},
                {"header": "HEALTH", "key": "health.status"},
            ],
            empty_message="No webhooks found.",
        )


@cli.command(name="create-webhook")
@click.argument("team_id")
@click.option(
    "--endpoint",
    required=True,
    help="The webhook endpoint URL.",
)
@click.option(
    "--event",
    multiple=True,
    help="Event to subscribe to (can be specified multiple times).",
)
@common_output_options
@handle_api_errors
def create_webhook(
    team_id: str,
    endpoint: str,
    event: tuple[str, ...],
    format: str,
    raw: bool,
) -> None:
    """Create a webhook in a workspace.

    TEAM_ID: The ID of the team/workspace.
    """
    if not event:
        click.echo("Error: At least one --event must be specified.", err=True)
        raise click.Abort()

    events = list(event)

    data = with_client(
        lambda client: client.create_webhook(team_id, endpoint=endpoint, events=events)
    )

    if handle_raw_output(data, raw):
        return

    webhook = data.get("webhook", data)

    if format == "json":
        output = {
            "id": webhook.get("id"),
            "endpoint": webhook.get("endpoint"),
            "events": webhook.get("events"),
            "health": webhook.get("health", {}).get("status"),
        }
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        click.echo("Webhook created successfully.")
        click.echo(f"ID:       {webhook.get('id')}")
        click.echo(f"Endpoint:  {webhook.get('endpoint')}")
        click.echo(f"Events:   {len(webhook.get('events', []))} event(s)")
        click.echo(f"Health:   {webhook.get('health', {}).get('status')}")


@cli.command(name="update-webhook")
@click.argument("webhook_id")
@click.option("--endpoint", help="The webhook endpoint URL.")
@click.option("--event", help="Events to subscribe to (use * for all events).")
@click.option("--status", help="The webhook status (e.g., active).")
@common_output_options
@handle_api_errors
def update_webhook_cli(
    webhook_id: str,
    endpoint: str | None,
    event: str | None,
    status: str | None,
    format: str,
    raw: bool,
) -> None:
    """Update a webhook.

    WEBHOOK_ID: The ID of the webhook to update.
    """
    with ClickUpClient() as client:
        data = client.update_webhook(
            webhook_id,
            endpoint=endpoint,
            events=event,
            status=status,
        )

        if handle_raw_output(data, raw):
            return

        if not data:
            click.echo("No updates provided.")
            return

        webhook = data.get("webhook", data)

    if format == "json":
        output = {
            "id": webhook.get("id"),
            "endpoint": webhook.get("endpoint"),
            "events": webhook.get("events"),
            "health": webhook.get("health", {}).get("status"),
        }
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        click.echo("Webhook updated successfully.")
        if webhook.get("endpoint"):
            click.echo(f"Endpoint: {webhook.get('endpoint')}")
        if webhook.get("events"):
            click.echo(f"Events:   {len(webhook.get('events', []))} event(s)")


@cli.command(name="delete-webhook")
@click.argument("webhook_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation prompt.")
@handle_api_errors
def delete_webhook(webhook_id: str, yes: bool) -> None:
    """Delete a webhook.

    WEBHOOK_ID: The ID of webhook to delete.
    """
    if not confirm_deletion("webhook", webhook_id, yes):
        return

    with_client(lambda client: client.delete_webhook(webhook_id))
    click.echo(f"Webhook {webhook_id} deleted successfully.")


def main() -> None:
    """Entry point for the CLI."""
    cli()
