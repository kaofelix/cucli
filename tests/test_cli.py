"""Tests for the CLI commands."""

import json

import pytest
from click.testing import CliRunner
from cucli.cli import cli


class TestWorkspacesCommand:
    """Test cases for the workspaces command."""

    @pytest.fixture
    def runner(self):
        """Provide a Click CliRunner for testing CLI commands."""
        return CliRunner()

    @pytest.mark.vcr
    def test_workspaces_json_output(self, runner, mock_api_key_env):
        """Test workspaces command with JSON output (default)."""
        result = runner.invoke(cli, ["workspaces"])

        assert result.exit_code == 0
        output = json.loads(result.output)

        assert isinstance(output, list)
        # Validate structure if there are workspaces
        if output:
            workspace = output[0]
            assert "id" in workspace
            assert "name" in workspace
            assert "color" in workspace

    @pytest.mark.vcr
    def test_workspaces_table_output(self, runner, mock_api_key_env):
        """Test workspaces command with table output."""
        result = runner.invoke(cli, ["workspaces", "--format", "table"])

        assert result.exit_code == 0
        # Table format should have headers
        assert "ID" in result.output
        assert "NAME" in result.output
        assert "COLOR" in result.output

    @pytest.mark.vcr
    def test_workspaces_raw_output(self, runner, mock_api_key_env):
        """Test workspaces command with raw JSON output."""
        result = runner.invoke(cli, ["workspaces", "--raw"])

        assert result.exit_code == 0
        output = json.loads(result.output)

        # Raw output should include all fields from API
        assert "teams" in output
        assert isinstance(output["teams"], list)

    def test_workspaces_missing_api_key(self, runner, monkeypatch):
        """Test workspaces command fails gracefully without API key."""
        monkeypatch.delenv("CLICKUP_API_KEY", raising=False)
        result = runner.invoke(cli, ["workspaces"])

        assert result.exit_code != 0
        assert "Error:" in result.output or "CLICKUP_API_KEY" in result.output


class TestSpacesCommand:
    """Test cases for the spaces command."""

    @pytest.fixture
    def runner(self):
        """Provide a Click CliRunner for testing CLI commands."""
        return CliRunner()

    @pytest.mark.vcr
    def test_spaces_json_output(self, runner, mock_api_key_env):
        """Test spaces command with JSON output (default)."""
        team_id = "90152245421"
        result = runner.invoke(cli, ["spaces", team_id])

        assert result.exit_code == 0
        output = json.loads(result.output)

        assert isinstance(output, list)
        # Validate structure if there are spaces
        if output:
            space = output[0]
            assert "id" in space
            assert "name" in space
            assert "private" in space

    @pytest.mark.vcr
    def test_spaces_table_output(self, runner, mock_api_key_env):
        """Test spaces command with table output."""
        team_id = "90152245421"
        result = runner.invoke(cli, ["spaces", team_id, "--format", "table"])

        assert result.exit_code == 0
        # Table format should have headers
        assert "ID" in result.output
        assert "NAME" in result.output
        assert "PRIVATE" in result.output

    @pytest.mark.vcr
    def test_spaces_raw_output(self, runner, mock_api_key_env):
        """Test spaces command with raw JSON output."""
        team_id = "90152245421"
        result = runner.invoke(cli, ["spaces", team_id, "--raw"])

        assert result.exit_code == 0
        output = json.loads(result.output)

        # Raw output should include all fields from API
        assert "spaces" in output
        assert isinstance(output["spaces"], list)

    @pytest.mark.vcr
    def test_spaces_with_archived(self, runner, mock_api_key_env):
        """Test spaces command with archived flag."""
        team_id = "90152245421"
        result = runner.invoke(cli, ["spaces", team_id, "--archived"])

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert isinstance(output, list)

    @pytest.mark.vcr
    def test_spaces_not_found(self, runner, mock_api_key_env):
        """Test spaces command with non-existent team ID."""
        team_id = "99999999"
        result = runner.invoke(cli, ["spaces", team_id])

        assert result.exit_code != 0
        assert "Error" in result.output or "HTTP Error" in result.output

    def test_spaces_missing_api_key(self, runner, monkeypatch):
        """Test spaces command fails gracefully without API key."""
        monkeypatch.delenv("CLICKUP_API_KEY", raising=False)
        team_id = "90152245421"
        result = runner.invoke(cli, ["spaces", team_id])

        assert result.exit_code != 0
        assert "Error:" in result.output or "CLICKUP_API_KEY" in result.output


class TestFoldersCommand:
    """Test cases for the folders command."""

    @pytest.fixture
    def runner(self):
        """Provide a Click CliRunner for testing CLI commands."""
        return CliRunner()

    @pytest.mark.vcr
    def test_folders_json_output(self, runner, mock_api_key_env):
        """Test folders command with JSON output (default)."""
        space_id = "90159451300"
        result = runner.invoke(cli, ["folders", space_id])

        assert result.exit_code == 0
        output = json.loads(result.output)

        assert isinstance(output, list)
        # Validate structure if there are folders
        if output:
            folder = output[0]
            assert "id" in folder
            assert "name" in folder
            assert "hidden" in folder
            assert "task_count" in folder

    @pytest.mark.vcr
    def test_folders_table_output(self, runner, mock_api_key_env):
        """Test folders command with table output."""
        space_id = "90159451300"
        result = runner.invoke(cli, ["folders", space_id, "--format", "table"])

        assert result.exit_code == 0
        # Either show headers if there are folders, or "No folders found"
        if "No folders found" in result.output:
            return
        # Table format should have headers
        assert "ID" in result.output
        assert "NAME" in result.output
        assert "TASKS" in result.output
        assert "HIDDEN" in result.output

    @pytest.mark.vcr
    def test_folders_raw_output(self, runner, mock_api_key_env):
        """Test folders command with raw JSON output."""
        space_id = "90159451300"
        result = runner.invoke(cli, ["folders", space_id, "--raw"])

        assert result.exit_code == 0
        output = json.loads(result.output)

        # Raw output should include all fields from API
        assert "folders" in output
        assert isinstance(output["folders"], list)

    @pytest.mark.vcr
    def test_folders_with_archived(self, runner, mock_api_key_env):
        """Test folders command with archived flag."""
        space_id = "90159451300"
        result = runner.invoke(cli, ["folders", space_id, "--archived"])

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert isinstance(output, list)

    @pytest.mark.vcr
    def test_folders_not_found(self, runner, mock_api_key_env):
        """Test folders command with non-existent space ID."""
        space_id = "99999999"
        result = runner.invoke(cli, ["folders", space_id])

        assert result.exit_code != 0
        assert "Error" in result.output or "HTTP Error" in result.output

    def test_folders_missing_api_key(self, runner, monkeypatch):
        """Test folders command fails gracefully without API key."""
        monkeypatch.delenv("CLICKUP_API_KEY", raising=False)
        space_id = "90159451300"
        result = runner.invoke(cli, ["folders", space_id])

        assert result.exit_code != 0
        assert "Error:" in result.output or "CLICKUP_API_KEY" in result.output


class TestTaskCommand:
    """Test cases for the task command."""

    @pytest.fixture
    def runner(self):
        """Provide a Click CliRunner for testing CLI commands."""
        return CliRunner()

    @pytest.mark.vcr
    def test_task_json_output(self, runner, mock_api_key_env):
        """Test task command with JSON output (default)."""
        task_id = "86c7mc19h"
        result = runner.invoke(cli, ["task", task_id])

        assert result.exit_code == 0
        output = json.loads(result.output)

        assert "id" in output
        assert "name" in output

    @pytest.mark.vcr
    def test_task_table_output(self, runner, mock_api_key_env):
        """Test task command with table output."""
        task_id = "86c7mc19h"
        result = runner.invoke(cli, ["task", task_id, "--format", "table"])

        assert result.exit_code == 0
        assert "ID:" in result.output
        assert "Name:" in result.output

    @pytest.mark.vcr
    def test_task_markdown_output(self, runner, mock_api_key_env):
        """Test task command with markdown format."""
        task_id = "86c7mc19h"
        result = runner.invoke(cli, ["task", task_id, "--format", "markdown"])

        assert result.exit_code == 0

    @pytest.mark.vcr
    def test_task_md_only_output(self, runner, mock_api_key_env):
        """Test task command with md-only flag."""
        task_id = "86c7mc19h"
        result = runner.invoke(cli, ["task", task_id, "--md-only"])

        assert result.exit_code == 0

    @pytest.mark.vcr
    def test_task_raw_output(self, runner, mock_api_key_env):
        """Test task command with raw JSON output."""
        task_id = "86c7mc19h"
        result = runner.invoke(cli, ["task", task_id, "--raw"])

        assert result.exit_code == 0
        output = json.loads(result.output)

        # Raw output should include all fields from API
        assert "id" in output
        assert "name" in output

    @pytest.mark.vcr
    def test_task_not_found(self, runner, mock_api_key_env):
        """Test task command with non-existent task ID."""
        task_id = "00000000"
        result = runner.invoke(cli, ["task", task_id])

        assert result.exit_code != 0
        assert "Error" in result.output or "HTTP Error" in result.output

    def test_task_missing_api_key(self, runner):
        """Test task command fails gracefully without API key."""
        task_id = "86abc123def456"
        result = runner.invoke(cli, ["task", task_id])

        assert result.exit_code != 0
        assert "Error:" in result.output or "CLICKUP_API_KEY" in result.output


class TestTasksCommand:
    """Test cases for the tasks command."""

    @pytest.fixture
    def runner(self):
        """Provide a Click CliRunner for testing CLI commands."""
        return CliRunner()

    @pytest.mark.vcr
    def test_tasks_json_output(self, runner, mock_api_key_env):
        """Test tasks command with JSON output (default)."""
        team_id = "90152245421"
        result = runner.invoke(cli, ["tasks", team_id])

        if result.exit_code != 0:
            print(f"Output: {result.output}")
            print(f"Exception: {result.exception}")

        assert result.exit_code == 0
        output = json.loads(result.output)

        assert isinstance(output, list)
        # Validate structure if there are tasks
        if output:
            task = output[0]
            assert "id" in task
            assert "name" in task
            assert "status" in task

    @pytest.mark.vcr
    def test_tasks_with_filters(self, runner, mock_api_key_env):
        """Test tasks command with filters."""
        team_id = "90152245421"
        result = runner.invoke(cli, ["tasks", team_id, "--status", "todo"])

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert isinstance(output, list)

    @pytest.mark.vcr
    def test_tasks_raw_output(self, runner, mock_api_key_env):
        """Test tasks command with raw JSON output."""
        team_id = "90152245421"
        result = runner.invoke(cli, ["tasks", team_id, "--raw"])

        assert result.exit_code == 0
        output = json.loads(result.output)

        # Raw output should include all fields from API
        assert "tasks" in output
        assert isinstance(output["tasks"], list)

    @pytest.mark.vcr
    def test_tasks_not_found(self, runner, mock_api_key_env):
        """Test tasks command with non-existent team ID."""
        team_id = "99999999"
        result = runner.invoke(cli, ["tasks", team_id])

        assert result.exit_code != 0
        assert "Error" in result.output or "HTTP Error" in result.output

    def test_tasks_missing_api_key(self, runner, monkeypatch):
        """Test tasks command fails gracefully without API key."""
        monkeypatch.delenv("CLICKUP_API_KEY", raising=False)
        team_id = "90152245421"
        result = runner.invoke(cli, ["tasks", team_id])

        assert result.exit_code != 0
        assert "Error:" in result.output or "CLICKUP_API_KEY" in result.output


class TestCLI:
    """Test cases for general CLI behavior."""

    @pytest.fixture
    def runner(self):
        """Provide a Click CliRunner for testing CLI commands."""
        return CliRunner()

    def test_cli_version(self, runner):
        """Test that the CLI has a version command."""
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert "version" in result.output.lower()

    def test_cli_help(self, runner):
        """Test that the CLI has a help command."""
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "workspaces" in result.output
        assert "task" in result.output
        assert "tasks" in result.output
        assert "spaces" in result.output
        assert "folders" in result.output

    def test_workspaces_help(self, runner):
        """Test workspaces command help."""
        result = runner.invoke(cli, ["workspaces", "--help"])
        assert result.exit_code == 0
        assert "--format" in result.output
        assert "--raw" in result.output

    def test_task_help(self, runner):
        """Test task command help."""
        result = runner.invoke(cli, ["task", "--help"])
        assert result.exit_code == 0
        assert "--format" in result.output
        assert "--raw" in result.output
        assert "--md-only" in result.output

    def test_spaces_help(self, runner):
        """Test spaces command help."""
        result = runner.invoke(cli, ["spaces", "--help"])
        assert result.exit_code == 0
        assert "--format" in result.output
        assert "--raw" in result.output
        assert "--archived" in result.output

    def test_folders_help(self, runner):
        """Test folders command help."""
        result = runner.invoke(cli, ["folders", "--help"])
        assert result.exit_code == 0
        assert "--format" in result.output
        assert "--raw" in result.output
        assert "--archived" in result.output
