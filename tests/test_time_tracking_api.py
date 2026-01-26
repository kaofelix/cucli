"""Tests for the time tracking API client methods."""

import pytest


class TestTimeTrackingAPI:
    """Test cases for time tracking API methods."""

    @pytest.fixture
    def team_id(self):
        """Provide a test team ID."""
        return "90152245421"

    @pytest.mark.vcr
    def test_get_running_time_entry(self, clickup_client, team_id):
        """Test getting the running time entry."""
        response = clickup_client.get_running_time_entry(team_id)

        # Verify response structure
        assert "data" in response
        data = response["data"]

        # If there's a running timer, verify its structure
        if data is not None:
            assert "id" in data
            assert "wid" in data
            assert "start" in data
            assert "duration" in data
            assert "user" in data

    @pytest.mark.vcr
    def test_start_time_entry(self, clickup_client, team_id):
        """Test starting a time entry."""
        # Start a timer with a task (required for basic plan)
        task_id = "86c7mc19h"
        data = clickup_client.start_time_entry(team_id, task_id=task_id)

        # Verify response structure
        assert "data" in data
        entry = data["data"]

        assert "id" in entry
        assert "wid" in entry
        assert "start" in entry
        assert "duration" in entry
        # Negative duration means timer is running
        assert entry["duration"] < 0
        assert "task" in entry
        assert entry["task"]["id"] == task_id

    @pytest.mark.vcr
    def test_start_time_entry_with_task(self, clickup_client, team_id):
        """Test starting a time entry for a specific task."""
        task_id = "86c7mc19h"
        data = clickup_client.start_time_entry(team_id, task_id=task_id)

        # Verify response structure
        assert "data" in data
        entry = data["data"]

        assert "id" in entry
        assert "task" in entry
        assert entry["task"]["id"] == task_id

    @pytest.mark.vcr
    def test_stop_time_entry(self, clickup_client, team_id):
        """Test stopping the current time entry."""
        data = clickup_client.stop_time_entry(team_id)

        # Verify response structure
        assert "data" in data
        entry = data["data"]

        assert "id" in entry
        assert "wid" in entry
        assert "start" in entry
        assert "end" in entry
        assert "duration" in entry
        # Stopped entry should have positive duration
        assert entry["duration"] >= 0

    @pytest.mark.vcr
    def test_get_time_entries(self, clickup_client, team_id):
        """Test getting time entries within a date range."""
        # Use fixed timestamps to match cassette
        start_date = 1736904000000
        end_date = 1737766400000

        response = clickup_client.get_time_entries(
            team_id,
            start_date=start_date,
            end_date=end_date,
        )

        # Verify response structure
        assert "data" in response
        data = response["data"]

        assert isinstance(data, list)

    @pytest.mark.vcr
    def test_create_time_entry(self, clickup_client, team_id):
        """Test creating a manual time entry."""
        start = 1737925200000
        duration = 1800000  # 30 minutes in milliseconds (basic plan limit)
        task_id = "86c7mc19h"

        data = clickup_client.create_time_entry(
            team_id,
            start=start,
            duration=duration,
            task_id=task_id,
            billable=False,
        )

        # Verify response structure
        assert "data" in data
        entry = data["data"]

        assert "id" in entry
        assert "start" in entry
        assert "duration" in entry
        assert entry.get("billable") is False
        assert "task" in entry
        assert entry["task"]["id"] == task_id

    @pytest.mark.vcr
    def test_create_time_entry_with_task(self, clickup_client, team_id):
        """Test creating a time entry associated with a task."""
        start = 1737925200000
        duration = 1800000  # 30 minutes in milliseconds
        task_id = "86c7mc19h"

        data = clickup_client.create_time_entry(
            team_id,
            start=start,
            duration=duration,
            task_id=task_id,
        )

        # Verify response structure
        assert "data" in data
        entry = data["data"]

        assert "task" in entry
        assert entry["task"]["id"] == task_id

    @pytest.mark.vcr
    @pytest.mark.skip(reason="Update operation requires Advanced Time Tracking plan")
    def test_update_time_entry(self, clickup_client, team_id):
        """Test updating a time entry."""
        # First create a time entry with a task (required for basic plan)
        start = 1737925200000
        duration = 1800000  # 30 minutes (basic plan limit)
        task_id = "86c7mc19h"

        created = clickup_client.create_time_entry(
            team_id,
            start=start,
            duration=duration,
            task_id=task_id,
        )
        timer_id = created["data"]["id"]

        # Update the time entry
        data = clickup_client.update_time_entry(
            team_id,
            timer_id,
            billable=True,
        )

        # Verify response structure
        assert "data" in data
        entry = data["data"]

        assert entry["id"] == timer_id
        assert entry.get("billable") is True

    @pytest.mark.vcr
    def test_delete_time_entry(self, clickup_client, team_id):
        """Test deleting a time entry."""
        # First create a time entry with a task (required for basic plan)
        start = 1737925200000
        duration = 1800000  # 30 minutes (basic plan limit)
        task_id = "86c7mc19h"

        created = clickup_client.create_time_entry(
            team_id,
            start=start,
            duration=duration,
            task_id=task_id,
        )
        timer_id = created["data"]["id"]

        # Delete the time entry
        data = clickup_client.delete_time_entry(team_id, timer_id)

        # Verify response structure - DELETE returns an array
        assert "data" in data
        entries = data["data"]
        assert isinstance(entries, list)
        # Find the deleted entry in the response
        deleted_entry = next((e for e in entries if e.get("id") == timer_id), None)
        assert deleted_entry is not None
