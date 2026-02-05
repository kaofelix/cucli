"""Tests for the dangerous mode feature."""

from click.testing import CliRunner

from cucli.cli import cli


def test_read_command_works_without_dangerous_mode():
    """Read-only commands should work without --dangerous-mode."""
    runner = CliRunner()
    result = runner.invoke(cli, ["workspaces"])
    # Should NOT fail due to dangerous mode check
    assert "Error: 'workspaces' modifies data" not in result.output
    assert "requires --dangerous-mode flag" not in result.output


def test_delete_command_blocked_without_dangerous_mode():
    """Delete commands should be blocked without --dangerous-mode."""
    runner = CliRunner()
    result = runner.invoke(cli, ["delete-task", "123"])
    assert result.exit_code != 0
    assert "Error: 'delete-task' modifies data" in result.output
    assert "requires --dangerous-mode flag" in result.output


def test_delete_command_works_with_dangerous_mode_flag():
    """Delete commands should work with --dangerous-mode flag."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--dangerous-mode", "delete-task", "123"])
    # Should fail due to missing API key or confirmation, not due to dangerous mode
    assert "Error: 'delete-task' modifies data" not in result.output


def test_create_command_blocked_without_dangerous_mode():
    """Create commands should be blocked without --dangerous-mode."""
    runner = CliRunner()
    result = runner.invoke(cli, ["create-task", "123", "--name", "Test"])
    assert result.exit_code != 0
    assert "Error: 'create-task' modifies data" in result.output


def test_update_command_blocked_without_dangerous_mode():
    """Update commands should be blocked without --dangerous-mode."""
    runner = CliRunner()
    result = runner.invoke(cli, ["update-task", "123", "--name", "Test"])
    assert result.exit_code != 0
    assert "Error: 'update-task' modifies data" in result.output


def test_start_time_entry_blocked_without_dangerous_mode():
    """Start time entry should be blocked without --dangerous-mode."""
    runner = CliRunner()
    result = runner.invoke(cli, ["start-time-entry", "123"])
    assert result.exit_code != 0
    assert "Error: 'start-time-entry' modifies data" in result.output


def test_stop_time_entry_blocked_without_dangerous_mode():
    """Stop time entry should be blocked without --dangerous-mode."""
    runner = CliRunner()
    result = runner.invoke(cli, ["stop-time-entry", "123"])
    assert result.exit_code != 0
    assert "Error: 'stop-time-entry' modifies data" in result.output


def test_add_comment_blocked_without_dangerous_mode():
    """Add comment should be blocked without --dangerous-mode."""
    runner = CliRunner()
    result = runner.invoke(cli, ["add-comment", "123", "--text", "Test"])
    assert result.exit_code != 0
    assert "Error: 'add-comment' modifies data" in result.output


def test_running_time_entry_works_without_dangerous_mode():
    """Running time entry (read-only) should not require dangerous mode."""
    runner = CliRunner()
    result = runner.invoke(cli, ["running-time-entry", "123"])
    # Should fail due to missing API key, not dangerous mode
    assert "Error: 'running-time-entry' modifies data" not in result.output


def test_dangerous_mode_via_env_var():
    """Delete commands should work with CUCLI_DANGEROUS_MODE env var."""
    runner = CliRunner(env={"CUCLI_DANGEROUS_MODE": "1"})
    result = runner.invoke(cli, ["delete-task", "123"])
    # Should NOT fail due to dangerous mode
    assert "Error: 'delete-task' modifies data" not in result.output
