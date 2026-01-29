"""Helper functions for cucli CLI commands."""

import json
from typing import Any, TypeVar

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
