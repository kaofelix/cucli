"""Tests for task attachments CLI commands."""

import json
import pytest
from cucli.cli import cli


class TestTaskAttachmentsCLI:
    """Test cases for task attachments CLI commands."""

    def test_create_attachment_requires_file(self, runner, mock_api_key_env):
        """Test that create-attachment command requires --file option."""
        result = runner.invoke(
            cli,
            ["create-attachment", "86c7mc19h"],
            env={"CLICKUP_API_KEY": mock_api_key_env},
        )
        assert result.exit_code != 0
        assert "Missing option '--file'" in result.output

    def test_create_attachment_custom_ids_requires_team_id(
        self, runner, mock_api_key_env
    ):
        """Test that create-attachment command requires --team-id when using --custom-task-ids."""
        result = runner.invoke(
            cli,
            [
                "create-attachment",
                "86c7mc19h",
                "--file",
                "/tmp/test.txt",
                "--custom-task-ids",
            ],
            env={"CLICKUP_API_KEY": mock_api_key_env},
        )
        assert result.exit_code != 0
        assert (
            "Error: --team-id is required when using --custom-task-ids" in result.output
        )

    @pytest.mark.vcr
    def test_create_attachment_json_format(self, runner, mock_api_key_env, tmp_path):
        """Test creating an attachment with JSON output format."""
        # Create a test file
        test_file = tmp_path / "test.txt"
        test_file.write_text("Test content")

        result = runner.invoke(
            cli,
            ["create-attachment", "86c7mc19h", "--file", str(test_file)],
            env={"CLICKUP_API_KEY": mock_api_key_env},
        )
        assert result.exit_code == 0

        # Verify JSON output
        output = json.loads(result.output)
        assert "id" in output
        assert "title" in output
        assert "url" in output

    @pytest.mark.vcr
    def test_create_attachment_table_format(self, runner, mock_api_key_env, tmp_path):
        """Test creating an attachment with table output format."""
        # Create a test file
        test_file = tmp_path / "test.txt"
        test_file.write_text("Test content")

        result = runner.invoke(
            cli,
            [
                "create-attachment",
                "86c7mc19h",
                "--file",
                str(test_file),
                "--format",
                "table",
            ],
            env={"CLICKUP_API_KEY": mock_api_key_env},
        )
        assert result.exit_code == 0
        assert "ID:" in result.output
        assert "Title:" in result.output
        assert "URL:" in result.output
        assert "Attachment uploaded successfully" in result.output

    @pytest.mark.vcr
    def test_create_attachment_raw(self, runner, mock_api_key_env, tmp_path):
        """Test creating an attachment with raw output."""
        # Create a test file
        test_file = tmp_path / "test.txt"
        test_file.write_text("Test content")

        result = runner.invoke(
            cli,
            ["create-attachment", "86c7mc19h", "--file", str(test_file), "--raw"],
            env={"CLICKUP_API_KEY": mock_api_key_env},
        )
        assert result.exit_code == 0

        # Verify raw JSON output
        output = json.loads(result.output)
        assert "id" in output
        assert "title" in output
