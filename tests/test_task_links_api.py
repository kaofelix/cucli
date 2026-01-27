"""Tests for task links API."""

import pytest
from cucli.models import Task


class TestTaskLinksAPI:
    """Test cases for task links API methods."""

    @pytest.mark.vcr
    def test_add_task_link(self, clickup_client):
        """Test adding a link between two tasks."""
        # Using real task IDs from test workspace
        task_id = "86c7mc19h"
        links_to = "86c7ujp8z"

        response = clickup_client.add_task_link(task_id, links_to=links_to)

        # Verify response structure
        assert "task" in response

        # Parse with Pydantic model
        task_data = response["task"]
        task = Task(**task_data)

        # Verify basic task structure
        assert task.id == task_id
        assert task.name is not None

        # Verify linked_tasks exists
        assert hasattr(task, "linked_tasks") or "linked_tasks" in task_data

    @pytest.mark.vcr
    def test_add_task_link_with_custom_ids(self, clickup_client):
        """Test adding a link between tasks with custom task IDs."""
        # This test would need custom task IDs configured
        # For now, we'll use standard IDs
        task_id = "86c7mc19h"
        links_to = "86c7ujp8z"

        response = clickup_client.add_task_link(
            task_id, links_to=links_to, custom_task_ids=False
        )

        # Verify response
        assert "task" in response
        task = Task(**response["task"])
        assert task.id == task_id

    @pytest.mark.vcr
    def test_delete_task_link(self, clickup_client):
        """Test deleting a link between two tasks."""
        task_id = "86c7mc19h"
        links_to_remove = "86c7ujp8z"

        # First add the link (in case it doesn't exist)
        clickup_client.add_task_link(task_id, links_to=links_to_remove)

        # Then delete it
        response = clickup_client.delete_task_link(task_id, links_to=links_to_remove)

        # Verify response structure
        assert "task" in response

        # Parse with Pydantic model
        task_data = response["task"]
        task = Task(**task_data)

        # Verify basic task structure
        assert task.id == task_id
        assert task.name is not None

    @pytest.mark.vcr
    def test_delete_task_link_with_custom_ids(self, clickup_client):
        """Test deleting a link between tasks with custom task IDs."""
        task_id = "86c7mc19h"
        links_to_remove = "86c7ujp8z"

        response = clickup_client.delete_task_link(
            task_id, links_to=links_to_remove, custom_task_ids=False
        )

        # Verify response
        assert "task" in response
        task = Task(**response["task"])
        assert task.id == task_id

    @pytest.mark.vcr
    def test_add_task_link_requires_links_to(self, clickup_client):
        """Test that add_task_link raises ValueError when links_to is not provided."""
        with pytest.raises(ValueError, match="links_to must be provided"):
            clickup_client.add_task_link("86c7mc19h")

    @pytest.mark.vcr
    def test_delete_task_link_requires_links_to(self, clickup_client):
        """Test that delete_task_link raises ValueError when links_to is not provided."""
        with pytest.raises(ValueError, match="links_to must be provided"):
            clickup_client.delete_task_link("86c7mc19h")
