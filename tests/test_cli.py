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


class TestListsCommand:
    """Test cases for lists command."""

    @pytest.fixture
    def runner(self):
        """Provide a Click CliRunner for testing CLI commands."""
        return CliRunner()

    @pytest.mark.vcr
    def test_lists_json_output(self, runner, mock_api_key_env):
        """Test lists command with JSON output (default)."""
        folder_id = "901513787576"
        result = runner.invoke(cli, ["lists", folder_id])

        assert result.exit_code == 0
        output = json.loads(result.output)

        assert isinstance(output, list)
        # Validate structure if there are lists
        if output:
            lst = output[0]
            assert "id" in lst
            assert "name" in lst
            assert "archived" in lst
            assert "task_count" in lst

    @pytest.mark.vcr
    def test_lists_table_output(self, runner, mock_api_key_env):
        """Test lists command with table output."""
        folder_id = "901513787576"
        result = runner.invoke(cli, ["lists", folder_id, "--format", "table"])

        assert result.exit_code == 0
        # Either show headers if there are lists, or "No lists found"
        if "No lists found" in result.output:
            return
        # Table format should have headers
        assert "ID" in result.output
        assert "NAME" in result.output
        assert "TASKS" in result.output
        assert "ARCHIVED" in result.output

    @pytest.mark.vcr
    def test_lists_raw_output(self, runner, mock_api_key_env):
        """Test lists command with raw JSON output."""
        folder_id = "901513787576"
        result = runner.invoke(cli, ["lists", folder_id, "--raw"])

        assert result.exit_code == 0
        output = json.loads(result.output)

        # Raw output should include all fields from API
        assert "lists" in output
        assert isinstance(output["lists"], list)

    @pytest.mark.vcr
    def test_lists_with_archived(self, runner, mock_api_key_env):
        """Test lists command with archived flag."""
        folder_id = "901513787576"
        result = runner.invoke(cli, ["lists", folder_id, "--archived"])

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert isinstance(output, list)

    @pytest.mark.vcr
    def test_lists_not_found(self, runner, mock_api_key_env):
        """Test lists command with non-existent folder ID."""
        folder_id = "99999999"
        result = runner.invoke(cli, ["lists", folder_id])

        assert result.exit_code != 0
        assert "Error" in result.output or "HTTP Error" in result.output

    def test_lists_missing_api_key(self, runner, monkeypatch):
        """Test lists command fails gracefully without API key."""
        monkeypatch.delenv("CLICKUP_API_KEY", raising=False)
        folder_id = "901513787576"
        result = runner.invoke(cli, ["lists", folder_id])

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
        assert "lists" in result.output
        assert "create-task" in result.output
        assert "create-folder" in result.output
        assert "update-task" in result.output
        assert "delete-task" in result.output

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

    def test_lists_help(self, runner):
        """Test lists command help."""
        result = runner.invoke(cli, ["lists", "--help"])
        assert result.exit_code == 0
        assert "--format" in result.output
        assert "--raw" in result.output
        assert "--archived" in result.output


class TestCreateTaskCommand:
    """Test cases for the create-task command."""

    @pytest.fixture
    def runner(self):
        """Provide a Click CliRunner for testing CLI commands."""
        return CliRunner()

    @pytest.mark.vcr
    def test_create_task_basic(self, runner, mock_api_key_env):
        """Test create-task command with minimal options."""
        list_id = "901520401736"
        result = runner.invoke(
            cli, ["create-task", list_id, "--name", "Test Task from CLI"]
        )

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert "id" in output
        assert output["name"] == "Test Task from CLI"

    @pytest.mark.vcr
    def test_create_task_with_description(self, runner, mock_api_key_env):
        """Test create-task command with description."""
        list_id = "901520401736"
        result = runner.invoke(
            cli,
            [
                "create-task",
                list_id,
                "--name",
                "Test Task with Description",
                "--description",
                "This is a test description",
            ],
        )

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert "id" in output
        assert output["name"] == "Test Task with Description"

    @pytest.mark.vcr
    def test_create_task_with_status(self, runner, mock_api_key_env):
        """Test create-task command with status."""
        list_id = "901520401736"
        result = runner.invoke(
            cli,
            [
                "create-task",
                list_id,
                "--name",
                "Test Task with Status",
                "--status",
                "to do",
            ],
        )

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert "id" in output

    @pytest.mark.vcr
    def test_create_task_with_priority(self, runner, mock_api_key_env):
        """Test create-task command with priority."""
        list_id = "901520401736"
        result = runner.invoke(
            cli,
            [
                "create-task",
                list_id,
                "--name",
                "Test Task with Priority",
                "--priority",
                "3",
            ],
        )

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert "id" in output

    @pytest.mark.vcr
    def test_create_task_with_assignees(self, runner, mock_api_key_env):
        """Test create-task command with assignees."""
        list_id = "901520401736"
        result = runner.invoke(
            cli,
            [
                "create-task",
                list_id,
                "--name",
                "Test Task with Assignee",
                "--assignee",
                "123",
            ],
        )

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert "id" in output

    @pytest.mark.vcr
    def test_create_task_with_tags(self, runner, mock_api_key_env):
        """Test create-task command with tags."""
        list_id = "901520401736"
        result = runner.invoke(
            cli,
            [
                "create-task",
                list_id,
                "--name",
                "Test Task with Tag",
                "--tag",
                "test-tag",
            ],
        )

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert "id" in output

    @pytest.mark.vcr
    def test_create_task_raw_output(self, runner, mock_api_key_env):
        """Test create-task command with raw output."""
        list_id = "901520401736"
        result = runner.invoke(
            cli,
            ["create-task", list_id, "--name", "Test Task Raw", "--raw"],
        )

        assert result.exit_code == 0
        output = json.loads(result.output)
        # Raw output includes all fields from API
        assert "id" in output
        assert "name" in output

    @pytest.mark.vcr
    def test_create_task_invalid_list(self, runner, mock_api_key_env):
        """Test create-task command with invalid list ID."""
        list_id = "99999999"
        result = runner.invoke(cli, ["create-task", list_id, "--name", "Test Task"])

        assert result.exit_code != 0
        assert "Error" in result.output or "HTTP Error" in result.output

    def test_create_task_missing_name(self, runner, mock_api_key_env):
        """Test create-task command fails without required name."""
        list_id = "901520401736"
        result = runner.invoke(cli, ["create-task", list_id])

        assert result.exit_code != 0
        assert "name" in result.output.lower() or "missing" in result.output.lower()

    def test_create_task_help(self, runner):
        """Test create-task command help."""
        result = runner.invoke(cli, ["create-task", "--help"])
        assert result.exit_code == 0
        assert "--name" in result.output
        assert "--description" in result.output
        assert "--status" in result.output
        assert "--priority" in result.output


class TestUpdateTaskCommand:
    """Test cases for the update-task command."""

    @pytest.fixture
    def runner(self):
        """Provide a Click CliRunner for testing CLI commands."""
        return CliRunner()

    @pytest.mark.vcr
    def test_update_task_name(self, runner, mock_api_key_env):
        """Test update-task command with name change."""
        # First create a task
        list_id = "901520401736"
        create_result = runner.invoke(
            cli, ["create-task", list_id, "--name", "Task to Update"]
        )
        task_id = json.loads(create_result.output)["id"]

        # Update the task
        result = runner.invoke(
            cli, ["update-task", task_id, "--name", "Updated Task Name"]
        )

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert output["name"] == "Updated Task Name"

    @pytest.mark.vcr
    def test_update_task_status(self, runner, mock_api_key_env):
        """Test update-task command with status change."""
        list_id = "901520401736"
        create_result = runner.invoke(
            cli, ["create-task", list_id, "--name", "Task for Status"]
        )
        task_id = json.loads(create_result.output)["id"]

        # Update status
        result = runner.invoke(cli, ["update-task", task_id, "--status", "to do"])

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert output["status"] == "to do"

    @pytest.mark.vcr
    def test_update_task_priority(self, runner, mock_api_key_env):
        """Test update-task command with priority change."""
        list_id = "901520401736"
        create_result = runner.invoke(
            cli, ["create-task", list_id, "--name", "Task for Priority"]
        )
        task_id = json.loads(create_result.output)["id"]

        # Update priority
        result = runner.invoke(cli, ["update-task", task_id, "--priority", "1"])

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert output["priority"] == "urgent"

    @pytest.mark.vcr
    def test_update_task_raw_output(self, runner, mock_api_key_env):
        """Test update-task command with raw output."""
        list_id = "901520401736"
        create_result = runner.invoke(
            cli, ["create-task", list_id, "--name", "Task for Raw"]
        )
        task_id = json.loads(create_result.output)["id"]

        result = runner.invoke(
            cli, ["update-task", task_id, "--name", "Updated", "--raw"]
        )

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert "id" in output
        assert "name" in output

    @pytest.mark.vcr
    def test_update_task_not_found(self, runner, mock_api_key_env):
        """Test update-task command with invalid task ID."""
        task_id = "00000000"
        result = runner.invoke(cli, ["update-task", task_id, "--name", "New Name"])

        assert result.exit_code != 0
        assert "Error" in result.output or "HTTP Error" in result.output

    def test_update_task_help(self, runner):
        """Test update-task command help."""
        result = runner.invoke(cli, ["update-task", "--help"])
        assert result.exit_code == 0
        assert "--name" in result.output
        assert "--status" in result.output
        assert "--priority" in result.output


class TestDeleteTaskCommand:
    """Test cases for the delete-task command."""

    @pytest.fixture
    def runner(self):
        """Provide a Click CliRunner for testing CLI commands."""
        return CliRunner()

    @pytest.mark.vcr
    def test_delete_task(self, runner, mock_api_key_env):
        """Test delete-task command."""
        # First create a task
        list_id = "901520401736"
        create_result = runner.invoke(
            cli, ["create-task", list_id, "--name", "Task to Delete"]
        )
        task_id = json.loads(create_result.output)["id"]

        # Delete the task
        result = runner.invoke(cli, ["delete-task", task_id, "--yes"])

        assert result.exit_code == 0

    @pytest.mark.vcr
    def test_delete_task_not_found(self, runner, mock_api_key_env):
        """Test delete-task command with invalid task ID."""
        task_id = "00000000"
        result = runner.invoke(cli, ["delete-task", task_id, "--yes"])

        assert result.exit_code != 0
        assert "Error" in result.output or "HTTP Error" in result.output

    def test_delete_task_help(self, runner):
        """Test delete-task command help."""
        result = runner.invoke(cli, ["delete-task", "--help"])
        assert result.exit_code == 0


class TestTaskCommentsCommand:
    """Test cases for the task-comments command."""

    @pytest.fixture
    def runner(self):
        """Provide a Click CliRunner for testing CLI commands."""
        return CliRunner()

    @pytest.mark.vcr
    def test_task_comments_json_output(self, runner, mock_api_key_env):
        """Test task-comments command with JSON output (default)."""
        task_id = "86c7mc19h"
        result = runner.invoke(cli, ["task-comments", task_id])

        assert result.exit_code == 0
        output = json.loads(result.output)

        assert isinstance(output, list)
        # Validate structure if there are comments
        if output:
            comment = output[0]
            assert "id" in comment
            assert "text" in comment
            assert "user" in comment
            assert "resolved" in comment
            assert "date" in comment

    @pytest.mark.vcr
    def test_task_comments_table_output(self, runner, mock_api_key_env):
        """Test task-comments command with table output."""
        task_id = "86c7mc19h"
        result = runner.invoke(cli, ["task-comments", task_id, "--format", "table"])

        assert result.exit_code == 0
        # Table format should have headers
        assert "ID" in result.output
        assert "USER" in result.output
        assert "TEXT" in result.output

    @pytest.mark.vcr
    def test_task_comments_raw_output(self, runner, mock_api_key_env):
        """Test task-comments command with raw JSON output."""
        task_id = "86c7mc19h"
        result = runner.invoke(cli, ["task-comments", task_id, "--raw"])

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert "comments" in output

    @pytest.mark.vcr
    def test_task_comments_not_found(self, runner, mock_api_key_env):
        """Test task-comments command with invalid task ID."""
        task_id = "00000000"
        result = runner.invoke(cli, ["task-comments", task_id])

        assert result.exit_code != 0
        assert "Error" in result.output or "HTTP Error" in result.output

    def test_task_comments_help(self, runner):
        """Test task-comments command help."""
        result = runner.invoke(cli, ["task-comments", "--help"])
        assert result.exit_code == 0


class TestAddCommentCommand:
    """Test cases for the add-comment command."""

    @pytest.fixture
    def runner(self):
        """Provide a Click CliRunner for testing CLI commands."""
        return CliRunner()

    @pytest.mark.vcr
    def test_add_comment_json_output(self, runner, mock_api_key_env):
        """Test add-comment command with JSON output (default)."""
        task_id = "86c7mc19h"
        result = runner.invoke(cli, ["add-comment", task_id, "--text", "Test comment"])

        assert result.exit_code == 0
        output = json.loads(result.output)

        assert "id" in output
        assert "date" in output

    @pytest.mark.vcr
    def test_add_comment_table_output(self, runner, mock_api_key_env):
        """Test add-comment command with table output."""
        task_id = "86c7mc19h"
        result = runner.invoke(
            cli, ["add-comment", task_id, "--text", "Test comment", "--format", "table"]
        )

        assert result.exit_code == 0
        assert "ID:" in result.output

    @pytest.mark.vcr
    def test_add_comment_with_assignee(self, runner, mock_api_key_env):
        """Test add-comment command with assignee."""
        task_id = "86c7mc19h"
        result = runner.invoke(
            cli, ["add-comment", task_id, "--text", "Test comment", "--assignee", "183"]
        )

        assert result.exit_code == 0

    @pytest.mark.vcr
    def test_add_comment_no_notify(self, runner, mock_api_key_env):
        """Test add-comment command with no-notify flag."""
        task_id = "86c7mc19h"
        result = runner.invoke(
            cli, ["add-comment", task_id, "--text", "Test comment", "--no-notify"]
        )

        assert result.exit_code == 0

    @pytest.mark.vcr
    def test_add_comment_not_found(self, runner, mock_api_key_env):
        """Test add-comment command with invalid task ID."""
        task_id = "00000000"
        result = runner.invoke(cli, ["add-comment", task_id, "--text", "Test"])

        assert result.exit_code != 0
        assert "Error" in result.output or "HTTP Error" in result.output

    def test_add_comment_help(self, runner):
        """Test add-comment command help."""
        result = runner.invoke(cli, ["add-comment", "--help"])
        assert result.exit_code == 0


class TestCreateFolderCommand:
    """Test cases for the create-folder command."""

    @pytest.fixture
    def runner(self):
        """Provide a Click CliRunner for testing CLI commands."""
        return CliRunner()

    @pytest.mark.vcr
    def test_create_folder_basic(self, runner, mock_api_key_env):
        """Test create-folder command with minimal options."""
        space_id = "90159451300"
        result = runner.invoke(
            cli, ["create-folder", space_id, "--name", "Test Folder from CLI"]
        )

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert "id" in output
        assert output["name"] == "Test Folder from CLI"

    @pytest.mark.vcr
    def test_create_folder_table_output(self, runner, mock_api_key_env):
        """Test create-folder command with table output."""
        space_id = "90159451300"
        result = runner.invoke(
            cli,
            [
                "create-folder",
                space_id,
                "--name",
                "Test Folder Table",
                "--format",
                "table",
            ],
        )

        assert result.exit_code == 0
        assert "ID:" in result.output
        assert "Name:" in result.output

    @pytest.mark.vcr
    def test_create_folder_raw_output(self, runner, mock_api_key_env):
        """Test create-folder command with raw output."""
        space_id = "90159451300"
        result = runner.invoke(
            cli, ["create-folder", space_id, "--name", "Test Folder Raw", "--raw"]
        )

        assert result.exit_code == 0
        output = json.loads(result.output)
        # Raw output includes all fields from API
        assert "id" in output
        assert "name" in output

    @pytest.mark.vcr
    def test_create_folder_invalid_space(self, runner, mock_api_key_env):
        """Test create-folder command with invalid space ID."""
        space_id = "99999999"
        result = runner.invoke(
            cli, ["create-folder", space_id, "--name", "Test Folder"]
        )

        assert result.exit_code != 0
        assert "Error" in result.output or "HTTP Error" in result.output

    def test_create_folder_missing_name(self, runner, mock_api_key_env):
        """Test create-folder command fails without required name."""
        space_id = "90159451300"
        result = runner.invoke(cli, ["create-folder", space_id])

        assert result.exit_code != 0
        assert "name" in result.output.lower() or "missing" in result.output.lower()

    def test_create_folder_help(self, runner):
        """Test create-folder command help."""
        result = runner.invoke(cli, ["create-folder", "--help"])
        assert result.exit_code == 0
        assert "--name" in result.output


class TestCreateListCommand:
    """Test cases for the create-list command."""

    @pytest.fixture
    def runner(self):
        """Provide a Click CliRunner for testing CLI commands."""
        return CliRunner()

    @pytest.mark.vcr
    def test_create_list_basic(self, runner, mock_api_key_env):
        """Test create-list command with minimal options."""
        folder_id = "901513787576"
        result = runner.invoke(
            cli, ["create-list", folder_id, "--name", "Test List from CLI"]
        )

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert "id" in output
        assert output["name"] == "Test List from CLI"

    @pytest.mark.vcr
    def test_create_list_with_description(self, runner, mock_api_key_env):
        """Test create-list command with description."""
        folder_id = "901513787576"
        result = runner.invoke(
            cli,
            [
                "create-list",
                folder_id,
                "--name",
                "Test List with Description",
                "--description",
                "Test description",
            ],
        )

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert "id" in output
        assert output["name"] == "Test List with Description"

    @pytest.mark.vcr
    def test_create_list_with_options(self, runner, mock_api_key_env):
        """Test create-list command with various options."""
        folder_id = "901513787576"
        result = runner.invoke(
            cli,
            [
                "create-list",
                folder_id,
                "--name",
                "Test List with Options",
                "--description",
                "Test description",
                "--status",
                "red",
                "--priority",
                "1",
            ],
        )

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert "id" in output
        assert output["name"] == "Test List with Options"

    @pytest.mark.vcr
    def test_create_list_table_output(self, runner, mock_api_key_env):
        """Test create-list command with table output."""
        folder_id = "901513787576"
        result = runner.invoke(
            cli,
            [
                "create-list",
                folder_id,
                "--name",
                "Test List Table",
                "--format",
                "table",
            ],
        )

        assert result.exit_code == 0
        assert "ID:" in result.output
        assert "Name:" in result.output

    @pytest.mark.vcr
    def test_create_list_raw_output(self, runner, mock_api_key_env):
        """Test create-list command with raw output."""
        folder_id = "901513787576"
        result = runner.invoke(
            cli, ["create-list", folder_id, "--name", "Test List Raw", "--raw"]
        )

        assert result.exit_code == 0
        output = json.loads(result.output)
        # Raw output includes all fields from API
        assert "id" in output
        assert "name" in output

    @pytest.mark.vcr
    def test_create_list_invalid_folder(self, runner, mock_api_key_env):
        """Test create-list command with invalid folder ID."""
        folder_id = "99999999"
        result = runner.invoke(cli, ["create-list", folder_id, "--name", "Test List"])

        assert result.exit_code != 0
        assert "Error" in result.output or "HTTP Error" in result.output

    def test_create_list_missing_name(self, runner, mock_api_key_env):
        """Test create-list command fails without required name."""
        folder_id = "901513787576"
        result = runner.invoke(cli, ["create-list", folder_id])

        assert result.exit_code != 0
        assert "name" in result.output.lower() or "missing" in result.output.lower()

    def test_create_list_help(self, runner):
        """Test create-list command help."""
        result = runner.invoke(cli, ["create-list", "--help"])
        assert result.exit_code == 0
        assert "--name" in result.output
