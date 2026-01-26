"""Tests for the goals API client methods."""

import pytest


class TestGoalsAPI:
    """Test cases for goals API methods."""

    @pytest.fixture
    def team_id(self):
        """Provide a test team ID."""
        return "90152245421"

    @pytest.fixture
    def goal_id(self):
        """Provide a test goal ID."""
        return "e28a27f0-9571-4f9c-9f7a-4712f21b605e"

    @pytest.mark.vcr
    def test_get_goals(self, clickup_client, team_id):
        """Test getting goals."""
        response = clickup_client.get_goals(team_id)

        # Verify response structure
        assert "goals" in response
        assert "folders" in response
        goals = response["goals"]

        assert isinstance(goals, list)

    @pytest.mark.vcr
    def test_get_goals_with_completed(self, clickup_client, team_id):
        """Test getting goals including completed."""
        response = clickup_client.get_goals(team_id, include_completed=True)

        # Verify response structure
        assert "goals" in response
        assert isinstance(response["goals"], list)

    @pytest.mark.vcr
    def test_get_goal(self, clickup_client, goal_id):
        """Test getting a goal by ID."""
        response = clickup_client.get_goal(goal_id)

        # Verify response structure
        assert "goal" in response
        goal = response["goal"]

        assert "id" in goal
        assert "name" in goal
        assert "team_id" in goal
        assert "due_date" in goal
        assert goal["id"] == goal_id

    @pytest.mark.vcr
    def test_create_goal(self, clickup_client, team_id):
        """Test creating a goal."""
        due_date = 1738368000000  # Feb 1, 2025
        data = clickup_client.create_goal(
            team_id,
            name="Test Goal from API",
            due_date=due_date,
            description="Test goal description",
            multiple_owners=False,
            owners=[],
            color="#32a852",
        )

        # Verify response structure
        assert "goal" in data
        goal = data["goal"]

        assert "id" in goal
        assert "name" in goal
        assert goal["name"] == "Test Goal from API"
        assert goal["due_date"] == str(due_date)

    @pytest.mark.vcr
    def test_create_goal_with_start_date(self, clickup_client, team_id):
        """Test creating a goal with start date."""
        start_date = 1735689600000  # Jan 1, 2025
        due_date = 1738368000000  # Feb 1, 2025
        data = clickup_client.create_goal(
            team_id,
            name="Test Goal with Start Date",
            due_date=due_date,
            start_date=start_date,
        )

        # Verify response structure
        assert "goal" in data
        goal = data["goal"]

        assert "start_date" in goal
        assert goal["start_date"] is not None

    @pytest.mark.vcr
    def test_update_goal(self, clickup_client, goal_id):
        """Test updating a goal."""
        due_date = 1738368000000  # Feb 1, 2025
        data = clickup_client.update_goal(
            goal_id,
            name="Updated Goal Name",
            due_date=due_date,
            description="Updated description",
            color="#ff5733",
        )

        # Verify response structure
        assert "goal" in data
        goal = data["goal"]

        assert "id" in goal
        assert goal["name"] == "Updated Goal Name"
        assert goal["description"] == "Updated description"

    @pytest.mark.vcr
    def test_update_goal_owners(self, clickup_client, goal_id):
        """Test updating goal owners."""
        data = clickup_client.update_goal(
            goal_id,
            add_owners=[],
            rem_owners=[],
        )

        # Verify response structure
        assert "goal" in data

    @pytest.mark.vcr
    def test_delete_goal(self, clickup_client, team_id):
        """Test deleting a goal."""
        # First create a goal to delete
        due_date = 1738368000000  # Feb 1, 2025
        created = clickup_client.create_goal(
            team_id,
            name="Goal to Delete",
            due_date=due_date,
        )
        goal_id_to_delete = created["goal"]["id"]

        # Delete the goal
        response = clickup_client.delete_goal(goal_id_to_delete)

        # Verify response structure - returns empty object
        assert isinstance(response, dict)


class TestKeyResultsAPI:
    """Test cases for key results API methods."""

    @pytest.fixture
    def goal_id(self):
        """Provide a test goal ID."""
        return "e28a27f0-9571-4f9c-9f7a-4712f21b605e"

    @pytest.mark.vcr
    def test_create_key_result(self, clickup_client, goal_id):
        """Test creating a key result."""
        data = clickup_client.create_key_result(
            goal_id,
            name="Test Key Result",
            owners=[],
            type="number",
            steps_start=0,
            steps_end=100,
            unit="",
        )

        # Verify response structure
        assert "key_result" in data
        key_result = data["key_result"]

        assert "id" in key_result
        assert "name" in key_result
        assert key_result["name"] == "Test Key Result"
        assert key_result["type"] == "number"

    @pytest.mark.vcr
    def test_create_key_result_with_task_ids(self, clickup_client, goal_id):
        """Test creating a key result with linked tasks."""
        task_id = "86c7mc19h"
        data = clickup_client.create_key_result(
            goal_id,
            name="Key Result with Tasks",
            owners=[],
            type="percentage",
            steps_start=0,
            steps_end=100,
            unit="%",
            task_ids=[task_id],
        )

        # Verify response structure
        assert "key_result" in data
        key_result = data["key_result"]

        assert "task_ids" in key_result
        assert task_id in key_result["task_ids"]

    @pytest.mark.vcr
    def test_update_key_result(self, clickup_client, goal_id):
        """Test updating a key result."""
        # First create a key result
        created = clickup_client.create_key_result(
            goal_id,
            name="Key Result to Update",
            owners=[],
            type="number",
            steps_start=0,
            steps_end=100,
        )
        key_result_id = created["key_result"]["id"]

        # Update the key result
        data = clickup_client.update_key_result(
            key_result_id,
            steps_current=50,
            note="Progress made",
        )

        # Verify response structure
        assert "key_result" in data
        key_result = data["key_result"]

        assert "id" in key_result
        assert key_result["id"] == key_result_id

    @pytest.mark.vcr
    def test_delete_key_result(self, clickup_client, goal_id):
        """Test deleting a key result."""
        # First create a key result to delete
        created = clickup_client.create_key_result(
            goal_id,
            name="Key Result to Delete",
            owners=[],
            type="number",
            steps_start=0,
            steps_end=100,
        )
        key_result_id = created["key_result"]["id"]

        # Delete the key result
        response = clickup_client.delete_key_result(key_result_id)

        # Verify response structure - returns empty object
        assert isinstance(response, dict)
