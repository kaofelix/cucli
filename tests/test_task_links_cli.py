"""Tests for task links CLI commands."""

import json
import pytest
from cucli.cli import cli


class TestTaskLinksCLI:
    """Test cases for task links CLI commands."""

    def test_add_link_requires_links_to_option(self, runner, mock_api_key_env):
        """Test that add-link command requires --links-to option."""
        result = runner.invoke(
            cli,
            ["add-link", "86c7mc19h"],
            env={"CLICKUP_API_KEY": mock_api_key_env},
        )
        assert result.exit_code != 0
        assert "Error: Either --links-to must be specified" in result.output

    def test_add_link_with_both_options_error(self, runner, mock_api_key_env):
        """Test that add-link command handles invalid parameters correctly."""
        # This is just to verify the command exists and handles missing required params
        result = runner.invoke(
            cli,
            ["add-link", "86c7mc19h"],
            env={"CLICKUP_API_KEY": mock_api_key_env},
        )
        # Should fail because --links-to is required
        assert result.exit_code != 0

    def test_delete_link_requires_links_to_option(self, runner, mock_api_key_env):
        """Test that delete-link command requires --links-to option."""
        result = runner.invoke(
            cli,
            ["delete-link", "86c7mc19h"],
            env={"CLICKUP_API_KEY": mock_api_key_env},
        )
        assert result.exit_code != 0
        assert "Error: Either --links-to must be specified" in result.output

    def test_add_link_custom_ids_requires_team_id(self, runner, mock_api_key_env):
        """Test that add-link command requires --team-id when using --custom-task-ids."""
        result = runner.invoke(
            cli,
            ["add-link", "86c7mc19h", "--links-to", "86c7ujp8z", "--custom-task-ids"],
            env={"CLICKUP_API_KEY": mock_api_key_env},
        )
        assert result.exit_code != 0
        assert (
            "Error: --team-id is required when using --custom-task-ids" in result.output
        )

    def test_delete_link_custom_ids_requires_team_id(self, runner, mock_api_key_env):
        """Test that delete-link command requires --team-id when using --custom-task-ids."""
        result = runner.invoke(
            cli,
            [
                "delete-link",
                "86c7mc19h",
                "--links-to",
                "86c7ujp8z",
                "--custom-task-ids",
            ],
            env={"CLICKUP_API_KEY": mock_api_key_env},
        )
        assert result.exit_code != 0
        assert (
            "Error: --team-id is required when using --custom-task-ids" in result.output
        )

    @pytest.mark.vcr
    def test_add_link_json_format(self, runner, mock_api_key_env):
        """Test adding a task link with JSON output format."""
        result = runner.invoke(
            cli,
            ["add-link", "86c7mc19h", "--links-to", "86c7ujp8z"],
            env={"CLICKUP_API_KEY": mock_api_key_env},
        )
        assert result.exit_code == 0

        # Verify JSON output
        output = json.loads(result.output)
        assert "task_id" in output
        assert output["task_id"] == "86c7mc19h"
        assert "links_to" in output
        assert output["links_to"] == "86c7ujp8z"

    @pytest.mark.vcr
    def test_add_link_table_format(self, runner, mock_api_key_env):
        """Test adding a task link with table output format."""
        result = runner.invoke(
            cli,
            ["add-link", "86c7mc19h", "--links-to", "86c7ujp8z", "--format", "table"],
            env={"CLICKUP_API_KEY": mock_api_key_env},
        )
        assert result.exit_code == 0
        assert "Task ID:" in result.output
        assert "Links To:" in result.output
        assert "Link added successfully" in result.output

    @pytest.mark.vcr
    def test_delete_link_json_format(self, runner, mock_api_key_env):
        """Test deleting a task link with JSON output format."""
        result = runner.invoke(
            cli,
            ["delete-link", "86c7mc19h", "--links-to", "86c7ujp8z"],
            env={"CLICKUP_API_KEY": mock_api_key_env},
        )
        assert result.exit_code == 0

        # Verify JSON output
        output = json.loads(result.output)
        assert "task_id" in output
        assert output["task_id"] == "86c7mc19h"
        assert "links_to" in output
        assert output["links_to"] == "86c7ujp8z"

    @pytest.mark.vcr
    def test_delete_link_table_format(self, runner, mock_api_key_env):
        """Test deleting a task link with table output format."""
        result = runner.invoke(
            cli,
            [
                "delete-link",
                "86c7mc19h",
                "--links-to",
                "86c7ujp8z",
                "--format",
                "table",
            ],
            env={"CLICKUP_API_KEY": mock_api_key_env},
        )
        assert result.exit_code == 0
        assert "Task ID:" in result.output
        assert "Links To:" in result.output
        assert "Link deleted successfully" in result.output
