"""Tests for task dependencies CLI commands."""

import pytest
from cucli.cli import cli


class TestTaskDependenciesCLI:
    """Test cases for task dependencies CLI commands."""

    @pytest.fixture
    def task_id(self):
        """Provide a test task ID."""
        return "86c7ujp8z"

    @pytest.fixture
    def dependent_task_id(self):
        """Provide a test dependent task ID."""
        return "86c7ujp3t"

    def test_add_dependency_requires_option(self, runner):
        """Test that add-dependency requires either --depends-on or --dependency-of."""
        result = runner.invoke(cli, ["--dangerous-mode", "add-dependency", "86c7ujp8z"])
        assert result.exit_code != 0
        assert (
            "Either --depends-on or --dependency-of must be specified" in result.output
        )

    def test_add_dependency_with_custom_task_ids_requires_team_id(self, runner):
        """Test that add-dependency with --custom-task-ids requires --team-id."""
        result = runner.invoke(
            cli,
            [
                "--dangerous-mode",
                "add-dependency",
                "86c7ujp8z",
                "--depends-on",
                "86c7ujp3t",
                "--custom-task-ids",
            ],
        )
        assert result.exit_code != 0
        assert "--team-id is required when using --custom-task-ids" in result.output

    @pytest.mark.vcr
    def test_add_dependency_depends_on_json(self, runner, task_id, dependent_task_id):
        """Test adding a dependency with --depends-on in JSON format."""
        result = runner.invoke(
            cli,
            [
                "--dangerous-mode",
                "add-dependency",
                task_id,
                "--depends-on",
                dependent_task_id,
            ],
        )
        assert result.exit_code == 0
        assert task_id in result.output
        assert dependent_task_id in result.output

    @pytest.mark.vcr
    def test_add_dependency_dependency_of_table(
        self, runner, task_id, dependent_task_id
    ):
        """Test adding a dependency with --dependency-of in table format."""
        result = runner.invoke(
            cli,
            [
                "--dangerous-mode",
                "add-dependency",
                task_id,
                "--dependency-of",
                dependent_task_id,
                "--format",
                "table",
            ],
        )
        assert result.exit_code == 0
        assert "Dependency Of:" in result.output
        assert "Dependency added successfully." in result.output

    def test_delete_dependency_requires_option(self, runner):
        """Test that delete-dependency requires either --depends-on or --dependency-of."""
        result = runner.invoke(
            cli, ["--dangerous-mode", "delete-dependency", "86c7ujp8z"]
        )
        assert result.exit_code != 0
        assert (
            "Either --depends-on or --dependency-of must be specified" in result.output
        )

    def test_delete_dependency_with_custom_task_ids_requires_team_id(self, runner):
        """Test that delete-dependency with --custom-task-ids requires --team-id."""
        result = runner.invoke(
            cli,
            [
                "--dangerous-mode",
                "delete-dependency",
                "86c7ujp8z",
                "--depends-on",
                "86c7ujp3t",
                "--custom-task-ids",
            ],
        )
        assert result.exit_code != 0
        assert "--team-id is required when using --custom-task-ids" in result.output

    @pytest.mark.vcr
    def test_delete_dependency_depends_on_json(
        self, runner, task_id, dependent_task_id
    ):
        """Test deleting a dependency with --depends-on in JSON format."""
        result = runner.invoke(
            cli,
            [
                "--dangerous-mode",
                "delete-dependency",
                task_id,
                "--depends-on",
                dependent_task_id,
            ],
        )
        assert result.exit_code == 0
        assert task_id in result.output
        assert dependent_task_id in result.output

    @pytest.mark.vcr
    def test_delete_dependency_dependency_of_table(
        self, runner, task_id, dependent_task_id
    ):
        """Test deleting a dependency with --dependency-of in table format."""
        result = runner.invoke(
            cli,
            [
                "--dangerous-mode",
                "delete-dependency",
                task_id,
                "--dependency-of",
                dependent_task_id,
                "--format",
                "table",
            ],
        )
        assert result.exit_code == 0
        assert "Dependency Of:" in result.output
        assert "Dependency deleted successfully." in result.output
