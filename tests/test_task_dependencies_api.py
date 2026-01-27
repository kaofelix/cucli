"""Tests for the task dependencies API client methods."""

import pytest


class TestTaskDependenciesAPI:
    """Test cases for task dependencies API methods."""

    @pytest.fixture
    def task_id(self):
        """Provide a test task ID."""
        return "86c7ujp8z"

    @pytest.fixture
    def dependent_task_id(self):
        """Provide a test dependent task ID."""
        return "86c7ujp3t"

    @pytest.mark.vcr
    def test_add_dependency_depends_on(
        self, clickup_client, task_id, dependent_task_id
    ):
        """Test adding a dependency where task depends on another task."""
        data = clickup_client.add_dependency(task_id, depends_on=dependent_task_id)

        # Verify response structure
        assert data is not None
        assert isinstance(data, dict)

    @pytest.mark.vcr
    def test_add_dependency_dependency_of(
        self, clickup_client, task_id, dependent_task_id
    ):
        """Test adding a dependency where task is blocking another task."""
        data = clickup_client.add_dependency(task_id, dependency_of=dependent_task_id)

        # Verify response structure
        assert data is not None
        assert isinstance(data, dict)

    @pytest.mark.vcr
    def test_delete_dependency_depends_on(
        self, clickup_client, task_id, dependent_task_id
    ):
        """Test deleting a dependency (depends_on relationship)."""
        data = clickup_client.delete_dependency(task_id, depends_on=dependent_task_id)

        # Verify response structure
        assert data is not None
        assert isinstance(data, dict)

    @pytest.mark.vcr
    def test_delete_dependency_dependency_of(
        self, clickup_client, task_id, dependent_task_id
    ):
        """Test deleting a dependency (dependency_of relationship)."""
        data = clickup_client.delete_dependency(
            task_id, dependency_of=dependent_task_id
        )

        # Verify response structure
        assert data is not None
        assert isinstance(data, dict)
