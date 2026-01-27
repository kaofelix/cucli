"""Tests for list comments CLI commands."""

import pytest
from cucli.cli import cli


@pytest.mark.vcr()
def test_list_comments(runner):
    """Test listing comments on a list."""
    result = runner.invoke(cli, ["list-comments", "901520401736"])

    assert result.exit_code == 0
    # Output should contain comments data
    assert result.output


@pytest.mark.vcr()
def test_list_comments_table_format(runner):
    """Test listing comments on a list in table format."""
    result = runner.invoke(cli, ["list-comments", "901520401736", "--format", "table"])

    assert result.exit_code == 0
    # Table output should have header
    assert "USER" in result.output


@pytest.mark.vcr()
def test_list_comments_raw(runner):
    """Test listing comments on a list with raw output."""
    result = runner.invoke(cli, ["list-comments", "901520401736", "--raw"])

    assert result.exit_code == 0
    # Raw output should be JSON
    assert '"comments"' in result.output


@pytest.mark.vcr()
def test_add_list_comment(runner):
    """Test adding a comment to a list."""
    result = runner.invoke(
        cli, ["add-list-comment", "901520401736", "--text", "Test list comment"]
    )

    assert result.exit_code == 0
    # Output should show comment was created
    assert "id" in result.output


@pytest.mark.vcr()
def test_add_list_comment_with_notify_false(runner):
    """Test adding a comment to a list without notifying all."""
    result = runner.invoke(
        cli,
        [
            "add-list-comment",
            "901520401736",
            "--text",
            "Test list comment",
            "--no-notify",
        ],
    )

    assert result.exit_code == 0
    # Output should show comment was created
    assert "id" in result.output


@pytest.mark.vcr()
def test_add_list_comment_with_assignee(runner):
    """Test adding a comment to a list with an assignee."""
    result = runner.invoke(
        cli,
        [
            "add-list-comment",
            "901520401736",
            "--text",
            "Test list comment",
            "--assignee",
            "272627274",
        ],
    )

    assert result.exit_code == 0
    # Output should show comment was created
    assert "id" in result.output


@pytest.mark.vcr()
def test_add_list_comment_table_format(runner):
    """Test adding a comment to a list in table format."""
    result = runner.invoke(
        cli,
        [
            "add-list-comment",
            "901520401736",
            "--text",
            "Test list comment",
            "--format",
            "table",
        ],
    )

    assert result.exit_code == 0
    # Table output should show ID
    assert "ID:" in result.output


@pytest.mark.vcr()
def test_add_list_comment_raw(runner):
    """Test adding a comment to a list with raw output."""
    result = runner.invoke(
        cli,
        ["add-list-comment", "901520401736", "--text", "Test list comment", "--raw"],
    )

    assert result.exit_code == 0
    # Raw output should be JSON
    assert '"id"' in result.output
    assert '"date"' in result.output


@pytest.mark.vcr()
def test_add_list_comment_missing_text(runner, mock_api_key_env):
    """Test adding a comment to a list without text raises error."""
    result = runner.invoke(cli, ["add-list-comment", "901520401736"])

    assert result.exit_code == 2
    assert "--text" in result.output or "Missing option" in result.output
