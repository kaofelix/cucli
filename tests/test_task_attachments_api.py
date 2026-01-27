"""Tests for task attachments API."""

import pytest
from cucli.models import Task


class TestTaskAttachmentsAPI:
    """Test cases for task attachments API methods."""

    @pytest.mark.vcr
    def test_create_task_attachment(self, clickup_client, tmp_path):
        """Test creating an attachment on a task."""
        # Create a test file
        test_file = tmp_path / "test.txt"
        test_file.write_text("Test content")

        # Using real task ID from test workspace
        task_id = "86c7mc19h"

        response = clickup_client.create_task_attachment(
            task_id, attachment_path=str(test_file)
        )

        # Verify response structure
        assert "id" in response
        assert "title" in response
        assert "url" in response
        assert "thumbnail_small" in response
        assert "thumbnail_large" in response
        assert "date" in response
        assert "version" in response
        assert "extension" in response

    @pytest.mark.vcr
    def test_create_task_attachment_with_custom_ids(self, clickup_client, tmp_path):
        """Test creating an attachment with custom task IDs."""
        # Create a test file
        test_file = tmp_path / "test.txt"
        test_file.write_text("Test content")

        task_id = "86c7mc19h"

        response = clickup_client.create_task_attachment(
            task_id,
            attachment_path=str(test_file),
            custom_task_ids=False,
        )

        # Verify response structure
        assert "id" in response
        assert "title" in response
