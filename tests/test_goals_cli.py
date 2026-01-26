"""Tests for goals CLI commands."""

import json

import pytest

from cucli.cli import cli


class TestGoalsCommands:
    """Test cases for goals CLI commands."""

    @pytest.fixture
    def team_id(self):
        """Provide a test team ID."""
        return "90152245421"

    @pytest.fixture
    def goal_id(self):
        """Provide a test goal ID."""
        return "e28a27f0-9571-4f9c-9f7a-4712f21b605e"

    def test_goals_json_output(self, runner, mock_api_key_env, team_id):
        """Test goals command with JSON output."""
        result = runner.invoke(cli, ["goals", team_id])

        assert result.exit_code == 0
        data = json.loads(result.output)
        assert isinstance(data, list)

    def test_goals_table_output(self, runner, mock_api_key_env, team_id):
        """Test goals command with table output."""
        result = runner.invoke(cli, ["goals", team_id, "--format", "table"])

        assert result.exit_code == 0
        # Should have headers or "No goals found" message
        assert "ID" in result.output or "No goals" in result.output

    def test_goals_raw_output(self, runner, mock_api_key_env, team_id):
        """Test goals command with raw JSON."""
        result = runner.invoke(cli, ["goals", team_id, "--raw"])

        assert result.exit_code == 0
        data = json.loads(result.output)
        assert "goals" in data

    def test_goals_with_completed(self, runner, mock_api_key_env, team_id):
        """Test goals command with include-completed flag."""
        result = runner.invoke(cli, ["goals", team_id, "--include-completed"])

        assert result.exit_code == 0

    def test_goals_missing_api_key(self, runner, monkeypatch, team_id):
        """Test goals command fails without API key."""
        monkeypatch.delenv("CLICKUP_API_KEY", raising=False)
        result = runner.invoke(cli, ["goals", team_id])

        assert result.exit_code != 0
        assert "CLICKUP_API_KEY" in result.output

    def test_goal_json_output(self, runner, mock_api_key_env, goal_id):
        """Test goal command with JSON output."""
        result = runner.invoke(cli, ["goal", goal_id])

        assert result.exit_code == 0
        data = json.loads(result.output)
        assert "id" in data
        assert data["id"] == goal_id

    def test_goal_table_output(self, runner, mock_api_key_env, goal_id):
        """Test goal command with table output."""
        result = runner.invoke(cli, ["goal", goal_id, "--format", "table"])

        assert result.exit_code == 0
        assert "ID:" in result.output

    def test_goal_raw_output(self, runner, mock_api_key_env, goal_id):
        """Test goal command with raw JSON."""
        result = runner.invoke(cli, ["goal", goal_id, "--raw"])

        assert result.exit_code == 0
        data = json.loads(result.output)
        assert "goal" in data

    def test_create_goal(self, runner, mock_api_key_env, team_id):
        """Test create-goal command."""
        due_date = 1738368000000  # Feb 1, 2025
        result = runner.invoke(
            cli,
            [
                "create-goal",
                team_id,
                "--name",
                "Test Goal CLI",
                "--due-date",
                str(due_date),
            ],
        )

        assert result.exit_code == 0
        data = json.loads(result.output)
        assert "id" in data
        assert data.get("name") == "Test Goal CLI"

    def test_create_goal_table(self, runner, mock_api_key_env, team_id):
        """Test create-goal command with table output."""
        due_date = 1738368000000  # Feb 1, 2025
        result = runner.invoke(
            cli,
            [
                "create-goal",
                team_id,
                "--name",
                "Test Goal CLI",
                "--due-date",
                str(due_date),
                "--format",
                "table",
            ],
        )

        assert result.exit_code == 0
        assert "Created successfully!" in result.output

    def test_create_goal_with_options(self, runner, mock_api_key_env, team_id):
        """Test create-goal command with options."""
        start_date = 1735689600000  # Jan 1, 2025
        due_date = 1738368000000  # Feb 1, 2025
        result = runner.invoke(
            cli,
            [
                "create-goal",
                team_id,
                "--name",
                "Test Goal Full",
                "--due-date",
                str(due_date),
                "--start-date",
                str(start_date),
                "--description",
                "Test description",
                "--color",
                "#ff5733",
                "--multiple-owners",
            ],
        )

        assert result.exit_code == 0

    def test_create_goal_missing_name(self, runner, mock_api_key_env, team_id):
        """Test create-goal command fails without name."""
        result = runner.invoke(cli, ["create-goal", team_id])

        assert result.exit_code != 0
        assert "Missing option" in result.output

    def test_update_goal(self, runner, mock_api_key_env, goal_id):
        """Test update-goal command."""
        due_date = 1738368000000  # Feb 1, 2025
        result = runner.invoke(
            cli,
            [
                "update-goal",
                goal_id,
                "--name",
                "Updated Goal CLI",
                "--due-date",
                str(due_date),
            ],
        )

        assert result.exit_code == 0
        data = json.loads(result.output)
        assert data.get("name") == "Updated Goal CLI"

    def test_update_goal_table(self, runner, mock_api_key_env, goal_id):
        """Test update-goal command with table output."""
        due_date = 1738368000000  # Feb 1, 2025
        result = runner.invoke(
            cli,
            [
                "update-goal",
                goal_id,
                "--name",
                "Updated Goal",
                "--due-date",
                str(due_date),
                "--format",
                "table",
            ],
        )

        assert result.exit_code == 0
        assert "Updated successfully!" in result.output

    def test_delete_goal(self, runner, mock_api_key_env, team_id):
        """Test delete-goal command."""
        # First create a goal to delete
        due_date = 1738368000000  # Feb 1, 2025
        create_result = runner.invoke(
            cli,
            [
                "create-goal",
                team_id,
                "--name",
                "Goal to Delete",
                "--due-date",
                str(due_date),
            ],
        )
        goal_id_to_delete = json.loads(create_result.output)["id"]

        # Delete the goal
        result = runner.invoke(cli, ["delete-goal", goal_id_to_delete, "--yes"])

        assert result.exit_code == 0
        assert "deleted successfully" in result.output

    def test_delete_goal_with_confirmation(self, runner, mock_api_key_env, team_id):
        """Test delete-goal command prompts for confirmation."""
        # First create a goal to delete
        due_date = 1738368000000  # Feb 1, 2025
        create_result = runner.invoke(
            cli,
            [
                "create-goal",
                team_id,
                "--name",
                "Goal to Delete 2",
                "--due-date",
                str(due_date),
            ],
        )
        goal_id_to_delete = json.loads(create_result.output)["id"]

        # Delete with confirmation
        result = runner.invoke(cli, ["delete-goal", goal_id_to_delete], input="y")

        assert result.exit_code == 0
        assert "deleted successfully" in result.output


class TestKeyResultCommands:
    """Test cases for key result CLI commands."""

    @pytest.fixture
    def goal_id(self):
        """Provide a test goal ID."""
        return "e28a27f0-9571-4f9c-9f7a-4712f21b605e"

    def test_create_key_result(self, runner, mock_api_key_env, goal_id):
        """Test create-key-result command."""
        result = runner.invoke(
            cli,
            [
                "create-key-result",
                goal_id,
                "--name",
                "Test Key Result CLI",
            ],
        )

        assert result.exit_code == 0
        data = json.loads(result.output)
        assert "id" in data
        assert data.get("name") == "Test Key Result CLI"

    def test_create_key_result_table(self, runner, mock_api_key_env, goal_id):
        """Test create-key-result command with table output."""
        result = runner.invoke(
            cli,
            [
                "create-key-result",
                goal_id,
                "--name",
                "Test Key Result",
                "--format",
                "table",
            ],
        )

        assert result.exit_code == 0
        assert "Created successfully!" in result.output

    def test_create_key_result_with_options(self, runner, mock_api_key_env, goal_id):
        """Test create-key-result command with options."""
        result = runner.invoke(
            cli,
            [
                "create-key-result",
                goal_id,
                "--name",
                "Test Key Result Full",
                "--type",
                "percentage",
                "--unit",
                "%",
                "--steps-start",
                "0",
                "--steps-end",
                "100",
            ],
        )

        assert result.exit_code == 0

    def test_create_key_result_with_task(self, runner, mock_api_key_env, goal_id):
        """Test create-key-result command with task link."""
        task_id = "86c7mc19h"
        result = runner.invoke(
            cli,
            [
                "create-key-result",
                goal_id,
                "--name",
                "Key Result with Task",
                "--task",
                task_id,
            ],
        )

        assert result.exit_code == 0

    def test_create_key_result_missing_name(self, runner, mock_api_key_env, goal_id):
        """Test create-key-result command fails without name."""
        result = runner.invoke(cli, ["create-key-result", goal_id])

        assert result.exit_code != 0
        assert "Missing option" in result.output

    def test_update_key_result(self, runner, mock_api_key_env, goal_id):
        """Test update-key-result command."""
        # First create a key result
        create_result = runner.invoke(
            cli,
            [
                "create-key-result",
                goal_id,
                "--name",
                "Key Result to Update",
            ],
        )
        key_result_id = json.loads(create_result.output)["id"]

        # Update the key result
        result = runner.invoke(
            cli,
            [
                "update-key-result",
                key_result_id,
                "--steps-current",
                "50",
                "--note",
                "Progress made",
            ],
        )

        assert result.exit_code == 0

    def test_update_key_result_table(self, runner, mock_api_key_env, goal_id):
        """Test update-key-result command with table output."""
        # First create a key result
        create_result = runner.invoke(
            cli,
            [
                "create-key-result",
                goal_id,
                "--name",
                "Key Result to Update 2",
            ],
        )
        key_result_id = json.loads(create_result.output)["id"]

        # Update the key result
        result = runner.invoke(
            cli,
            [
                "update-key-result",
                key_result_id,
                "--steps-current",
                "75",
                "--format",
                "table",
            ],
        )

        assert result.exit_code == 0
        assert "Updated successfully!" in result.output

    def test_delete_key_result(self, runner, mock_api_key_env, goal_id):
        """Test delete-key-result command."""
        # First create a key result
        create_result = runner.invoke(
            cli,
            [
                "create-key-result",
                goal_id,
                "--name",
                "Key Result to Delete",
            ],
        )
        key_result_id = json.loads(create_result.output)["id"]

        # Delete the key result
        result = runner.invoke(cli, ["delete-key-result", key_result_id, "--yes"])

        assert result.exit_code == 0
        assert "deleted successfully" in result.output

    def test_delete_key_result_with_confirmation(
        self, runner, mock_api_key_env, goal_id
    ):
        """Test delete-key-result command prompts for confirmation."""
        # First create a key result
        create_result = runner.invoke(
            cli,
            [
                "create-key-result",
                goal_id,
                "--name",
                "Key Result to Delete 2",
            ],
        )
        key_result_id = json.loads(create_result.output)["id"]

        # Delete with confirmation
        result = runner.invoke(cli, ["delete-key-result", key_result_id], input="y")

        assert result.exit_code == 0
        assert "deleted successfully" in result.output

    def test_create_key_result_missing_goal_id(self, runner):
        """Test create-key-result command fails without goal_id."""
        result = runner.invoke(cli, ["create-key-result"])

        assert result.exit_code != 0
        assert "Missing argument" in result.output
