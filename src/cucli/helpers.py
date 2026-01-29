"""Helper functions for cucli CLI commands."""

import json
from typing import Any, Callable, TypeVar

import click

T = TypeVar("T")


def format_table(
    data: list[Any],
    columns: list[dict[str, Any]],
    empty_message: str = "No items found.",
) -> None:
    """Format and display a table of data.

    This function handles common table formatting logic including:
    - Empty collection handling
    - Dynamic column width calculation
    - Header and separator printing
    - Row formatting with value transformation

    Args:
        data: List of data items to display.
        columns: List of column definitions. Each column is a dict with:
            - header: Column header text.
            - key: Attribute key or item key to extract value.
            - get_value: Optional callable to transform the value.
            - width: Optional fixed width (if not specified, calculated dynamically).
        empty_message: Message to display if data is empty.

    Example:
        format_table(
            teams,
            [
                {"header": "ID", "key": "id"},
                {"header": "NAME", "key": "name"},
                {"header": "COLOR", "key": "color"},
            ],
            empty_message="No workspaces found.",
        )

    Example with value transformation:
        format_table(
            lists,
            [
                {"header": "ID", "key": "id"},
                {"header": "NAME", "key": "name"},
                {"header": "TASKS", "key": "task_count", "get_value": str},
                {"header": "ARCHIVED", "key": "archived", "get_value": lambda x: "Yes" if x else "No"},
            ],
            empty_message="No lists found.",
        )

    Example with fixed width:
        format_table(
            tags,
            [
                {"header": "NAME", "key": "name"},
                {"header": "FG COLOR", "key": "tag_fg", "width": 10},
                {"header": "BG COLOR", "key": "tag_bg"},
            ],
            empty_message="No tags found.",
        )
    """
    if not data:
        click.echo(empty_message)
        return

    # Calculate column widths
    col_widths = []
    for col in columns:
        if "width" in col:
            col_widths.append(col["width"])
        else:
            # Calculate width based on header and all values
            header_len = len(col["header"])
            if "get_value" in col:
                max_value_len = max(
                    len(str(col["get_value"](_get_value(item, col["key"]))))
                    for item in data
                )
            else:
                max_value_len = max(
                    len(str(_get_value(item, col["key"]))) for item in data
                )
            col_widths.append(max(header_len, max_value_len))

    # Print header
    header_parts = []
    for col, width in zip(columns, col_widths):
        header_parts.append(col["header"].ljust(width))
    click.echo("  ".join(header_parts))

    # Calculate separator line length (sum of widths + spaces between)
    separator_len = sum(col_widths) + (2 * (len(columns) - 1))
    click.echo("-" * separator_len)

    # Print rows
    for item in data:
        row_parts = []
        for col, width in zip(columns, col_widths):
            if "get_value" in col:
                value = col["get_value"](_get_value(item, col["key"]))
            else:
                value = _get_value(item, col["key"])
            row_parts.append(str(value).ljust(width))
        click.echo("  ".join(row_parts))


def confirm_deletion(resource_type: str, resource_id: str, yes: bool = False) -> bool:
    """Confirm deletion of a resource.

    Args:
        resource_type: The type of resource being deleted (e.g., "folder", "task").
        resource_id: The ID of the resource to delete.
        yes: If True, skip the confirmation prompt.

    Returns:
        True if deletion should proceed, False otherwise.
    """
    if not yes:
        if not click.confirm(
            f"Are you sure you want to delete {resource_type} {resource_id}?"
        ):
            click.echo("Deletion cancelled.")
            return False
    return True


def _get_value(item: Any, key: str) -> Any:
    """Get a value from an item by key (supports both dict and object access).

    Args:
        item: The data item (dict or object).
        key: The key or attribute name.

    Returns:
        The value at the given key/attribute.
    """
    if isinstance(item, dict):
        return item.get(key, "")
    return getattr(item, key, "")


def parse_models_with_raw(
    data: dict[str, Any],
    key: str,
    model_class: type[T],
    raw: bool,
) -> list[T] | None:
    """Parse API response data into Pydantic models with raw JSON fallback.

    This helper eliminates the repeated pattern of:
        if raw:
            click.echo(json.dumps(data, indent=2))
            return
        items = [Model(**item) for item in data["items"]]

    Args:
        data: The raw API response data.
        key: The key in data that contains the list of items (e.g., "teams", "spaces").
        model_class: The Pydantic model class to parse each item into.
        raw: If True, output raw JSON and return None.

    Returns:
        List of parsed model instances if raw is False, None if raw is True.

    Example:
        teams = parse_models_with_raw(data, "teams", Team, raw)
        if teams is None:
            return
        # Continue with teams processing...
    """
    if raw:
        click.echo(json.dumps(data, indent=2))
        return None

    items_list = data.get(key, [])
    return [model_class(**item) for item in items_list]


def validate_team_id_for_custom_tasks(
    custom_task_ids: bool,
    team_id: str | int | None,
) -> None:
    """Validate that team_id is provided when using custom_task_ids.

    This helper eliminates the repeated pattern of:
        if custom_task_ids and not team_id:
            click.echo(
                "Error: --team-id is required when using --custom-task-ids.",
                err=True,
            )
            raise click.Abort()

    Args:
        custom_task_ids: Whether custom task IDs are being used.
        team_id: The team/workspace ID.

    Raises:
        click.Abort: If validation fails.

    Example:
        validate_team_id_for_custom_tasks(custom_task_ids, team_id)
    """
    if custom_task_ids and not team_id:
        click.echo(
            "Error: --team-id is required when using --custom-task-ids.",
            err=True,
        )
        raise click.Abort()


def handle_raw_output(data: dict[str, Any] | None, raw: bool) -> bool:
    """Handle raw JSON output for API responses.

    This helper eliminates the repeated pattern of:
        if raw:
            click.echo(json.dumps(data, indent=2))
            return

    Args:
        data: The raw API response data (can be None or empty dict).
        raw: If True, output raw JSON and return True.

    Returns:
        True if raw output was handled (function should return), False otherwise.

    Example:
        data = with_client(lambda client: client.get_folder(folder_id))
        if handle_raw_output(data, raw):
            return
        # Continue with data processing...
    """
    if raw:
        if data:
            click.echo(json.dumps(data, indent=2))
        else:
            click.echo("{}")
        return True
    return False


def handle_empty_collection(
    items: list[Any],
    format: str,
    empty_message: str = "No items found.",
) -> bool:
    """Handle empty collection output for API responses.

    This helper eliminates the repeated pattern of:
        if not items:
            if format == "json":
                click.echo(json.dumps([]))
            else:
                click.echo("No items found.")
            return

    Args:
        items: The collection of items to check.
        format: The output format ("json" or "table").
        empty_message: The message to display for table format when empty.

    Returns:
        True if collection was empty and output was handled (function should return),
        False otherwise.

    Example:
        entries = data.get("data", [])
        if handle_empty_collection(entries, format, "No time entries found."):
            return
        # Continue with entries processing...
    """
    if not items:
        if format == "json":
            click.echo(json.dumps([]))
        else:
            click.echo(empty_message)
        return True
    return False


def format_time_entry_json(entry: dict[str, Any]) -> None:
    """Format and display a single time entry as JSON.

    This helper eliminates the repeated pattern of:
        output = {
            "id": entry.get("id"),
            "wid": entry.get("wid"),
            "start": entry.get("start"),
            "duration": entry.get("duration"),
            "description": entry.get("description"),
            "task_id": entry.get("task", {}).get("id") if entry.get("task") else None,
        }
        click.echo(json.dumps(output, indent=2))

    Args:
        entry: The time entry data from the API response (extracted from "data" key).

    Example:
        entry = data.get("data", {})
        format_time_entry_json(entry)
    """
    output = {
        "id": entry.get("id"),
        "wid": entry.get("wid"),
        "start": entry.get("start"),
        "end": entry.get("end"),
        "duration": entry.get("duration"),
        "description": entry.get("description"),
        "task_id": entry.get("task", {}).get("id") if entry.get("task") else None,
        "billable": entry.get("billable"),
    }
    click.echo(json.dumps(output, indent=2))


def format_time_entry_table(
    entry: dict[str, Any], success_message: str | None = None
) -> None:
    """Format and display a single time entry as a table.

    This helper eliminates the repeated pattern of:
        click.echo(f"ID:          {entry.get('id')}")
        click.echo(f"Start:       {entry.get('start')}")
        click.echo(f"Duration:    {entry.get('duration')}")
        if entry.get("description"):
            click.echo(f"Description: {entry.get('description')}")
        if entry.get("task"):
            click.echo(f"Task ID:     {entry.get('task', {}).get('id')}")

    Args:
        entry: The time entry data from the API response (extracted from "data" key).
        success_message: Optional success message to display at the end.

    Example:
        entry = data.get("data", {})
        format_time_entry_table(entry, "Timer started successfully.")
    """
    click.echo(f"ID:          {entry.get('id')}")
    click.echo(f"Start:       {entry.get('start')}")
    if entry.get("end"):
        click.echo(f"End:         {entry.get('end')}")
    click.echo(f"Duration:    {entry.get('duration')}")
    if entry.get("description"):
        click.echo(f"Description: {entry.get('description')}")
    if entry.get("task"):
        click.echo(f"Task ID:     {entry.get('task', {}).get('id')}")
    if success_message:
        click.echo(success_message)


def format_list_output(
    items: list[Any],
    format: str,
    columns: list[dict[str, Any]],
    json_formatter: Callable[[list[Any]], list[dict[str, Any]]] | None = None,
    empty_message: str = "No items found.",
) -> None:
    """Format and display a list of items in JSON or table format.

    This helper eliminates the repeated pattern of:
        if format == "json":
            output = [{"id": item.id, "name": item.name, ...} for item in items]
            click.echo(json.dumps(output, indent=2))
        elif format == "table":
            format_table(items, columns, empty_message=...)

    Args:
        items: List of data items to display.
        format: Output format ("json" or "table").
        columns: List of column definitions for table format.
        json_formatter: Optional callable that transforms items into JSON-serializable dicts.
            If not provided, uses columns to build the output.
        empty_message: Message to display if items is empty (for table format).

    Example:
        format_list_output(
            teams,
            format,
            [
                {"header": "ID", "key": "id"},
                {"header": "NAME", "key": "name"},
                {"header": "COLOR", "key": "color"},
            ],
            empty_message="No workspaces found.",
        )

    Example with custom JSON formatter:
        format_list_output(
            spaces_list,
            format,
            [
                {"header": "ID", "key": "id"},
                {"header": "NAME", "key": "name"},
                {"header": "PRIVATE", "key": "private", "get_value": lambda x: "Yes" if x else "No"},
            ],
            json_formatter=lambda spaces: [
                {"id": s.id, "name": s.name, "private": s.private} for s in spaces
            ],
            empty_message="No spaces found.",
        )
    """
    if format == "json":
        if json_formatter is not None:
            output = json_formatter(items)
        else:
            # Build output from columns
            output = []
            for item in items:
                item_dict = {}
                for col in columns:
                    value = _get_value(item, col["key"])
                    if "get_value" in col:
                        value = col["get_value"](value)
                    item_dict[col["key"]] = value
                output.append(item_dict)
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        format_table(items, columns, empty_message=empty_message)


def format_single_output(
    data: dict[str, Any],
    format: str,
    json_formatter: Callable[[dict[str, Any]], dict[str, Any]],
    table_formatter: Callable[[dict[str, Any]], None],
) -> None:
    """Format and display a single item in JSON or table format.

    This helper eliminates the repeated pattern of:
        if format == "json":
            output = {
                "id": data.get("id"),
                "name": data.get("name"),
                ...
            }
            click.echo(json.dumps(output, indent=2))
        elif format == "table":
            click.echo(f"ID:   {data.get('id')}")
            click.echo(f"Name: {data.get('name')}")

    Args:
        data: The data item to display.
        format: Output format ("json" or "table").
        json_formatter: Callable that transforms data into a JSON-serializable dict.
        table_formatter: Callable that formats and displays data as a table.

    Example:
        format_single_output(
            data,
            format,
            json_formatter=lambda d: {
                "id": d.get("id"),
                "name": d.get("name"),
                "space_id": d.get("space", {}).get("id"),
            },
            table_formatter=lambda d: (
                click.echo(f"ID:       {d.get('id')}"),
                click.echo(f"Name:     {d.get('name')}"),
                click.echo(f"Space ID: {d.get('space', {}).get('id')}"),
            )[-1],  # Return the last expression
        )
    """
    if format == "json":
        output = json_formatter(data)
        click.echo(json.dumps(output, indent=2))
    elif format == "table":
        table_formatter(data)
