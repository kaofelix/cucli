"""Common decorators for cucli CLI commands."""

import functools
from typing import Callable

import click
import httpx


def handle_api_errors(func: Callable) -> Callable:
    """Decorator to handle common API errors in CLI commands.

    This decorator wraps CLI command functions to handle:
    - httpx.HTTPStatusError: HTTP errors from the API
    - ValueError: Validation errors
    - Exception: Any other unexpected errors

    All errors are printed to stderr and the command is aborted.

    Args:
        func: The CLI command function to wrap.

    Returns:
        The wrapped function with error handling.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except httpx.HTTPStatusError as e:
            click.echo(f"HTTP Error: {e.response.status_code} - {e}", err=True)
            raise click.Abort()
        except ValueError as e:
            click.echo(f"Error: {e}", err=True)
            raise click.Abort()
        except Exception as e:
            click.echo(f"Unexpected error: {e}", err=True)
            raise click.Abort()

    return wrapper


def common_output_options(func: Callable) -> Callable:
    """Decorator to add common output options to CLI commands.

    This decorator adds two options to a command:
    - --format: Output format (json or table), defaults to json
    - --raw: Output raw JSON without model validation

    Args:
        func: The CLI command function to wrap.

    Returns:
        The wrapped function with output options added.

    Example:
        @click.command()
        @common_output_options
        @handle_api_errors
        def my_command(format: str, raw: bool):
            ...
    """
    func = click.option(
        "--format",
        type=click.Choice(["json", "table"], case_sensitive=False),
        default="json",
        help="Output format.",
    )(func)
    func = click.option(
        "--raw", is_flag=True, help="Output raw JSON without model validation."
    )(func)
    return func
