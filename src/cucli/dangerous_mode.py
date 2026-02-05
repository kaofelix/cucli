"""Dangerous mode decorator for cucli CLI commands.

This module provides functionality to require explicit opt-in for commands
that modify data (create, update, delete operations).
"""

import functools
from typing import Callable

import click


def require_dangerous_mode(func: Callable) -> Callable:
    """Decorator to require dangerous mode for data-modifying commands.

    This decorator ensures that commands which create, update, or delete data
    require explicit opt-in via --dangerous-mode flag or CUCLI_DANGEROUS_MODE
    environment variable.

    Args:
        func: The CLI command function to wrap.

    Returns:
        The wrapped function that checks for dangerous mode before executing.

    Example:
        @cli.command(name="delete-task")
        @click.argument("task_id")
        @require_dangerous_mode
        def delete_task(task_id: str) -> None:
            # This command will be blocked unless --dangerous-mode is used
            ...
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ctx = click.get_current_context()

        # Check if dangerous mode is enabled via the flag
        # The flag is stored in the parent context's obj
        dangerous_mode_enabled = False
        if ctx.obj and ctx.obj.get("dangerous_mode"):
            dangerous_mode_enabled = True

        if not dangerous_mode_enabled:
            command_name = ctx.command.name if ctx.command else "this command"
            click.echo(
                f"Error: '{command_name}' modifies data and requires --dangerous-mode flag "
                f"or CUCLI_DANGEROUS_MODE=1 environment variable.",
                err=True,
            )
            raise click.Abort()

        return func(*args, **kwargs)

    return wrapper
