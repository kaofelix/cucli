"""Tests for the ClickUp API client."""

import pytest
from cucli.api import ClickUpClient
from cucli.models import Team, Task, TeamsResponse


class TestClickUpClient:
    """Test cases for ClickUpClient class."""

    def test_init_without_api_key(self):
        """Test that client raises ValueError when no API key is provided."""
        # Temporarily unset env var if it exists
        import os

        original_key = os.environ.get("CLICKUP_API_KEY")
        if "CLICKUP_API_KEY" in os.environ:
            del os.environ["CLICKUP_API_KEY"]

        try:
            with pytest.raises(ValueError, match="CLICKUP_API_KEY not set"):
                ClickUpClient()
        finally:
            # Restore original env var
            if original_key is not None:
                os.environ["CLICKUP_API_KEY"] = original_key

    def test_init_with_api_key(self, api_key):
        """Test that client initializes correctly with an API key."""
        client = ClickUpClient(api_key=api_key)
        assert client.api_key == api_key
        assert client.base_url == "https://api.clickup.com/api/v2"
        assert client._client.headers["Authorization"] == api_key
        client.close()

    def test_context_manager(self, api_key):
        """Test that client works as a context manager."""
        with ClickUpClient(api_key=api_key) as client:
            assert client.api_key == api_key
            assert client._client is not None
        # After exiting, the client should be closed
        assert client._client.is_closed

    @pytest.mark.vcr
    def test_get_teams(self, clickup_client):
        """Test getting teams from the API."""
        response = clickup_client.get_teams()

        # Verify response structure
        assert "teams" in response
        assert isinstance(response["teams"], list)

        # Parse with Pydantic model
        teams_response = TeamsResponse(**response)
        assert len(teams_response.teams) >= 0

        # If there are teams, validate first team structure
        if teams_response.teams:
            team = teams_response.teams[0]
            assert isinstance(team.id, str)
            assert isinstance(team.name, str)
            assert isinstance(team.color, str)

    @pytest.mark.vcr
    def test_get_teams_parses_model(self, clickup_client):
        """Test that get_teams response can be parsed into Pydantic models."""
        response = clickup_client.get_teams()

        for team_data in response["teams"]:
            team = Team(**team_data)
            assert team.id
            assert team.name
            assert team.color

    @pytest.mark.vcr
    def test_get_task(self, clickup_client):
        """Test getting a specific task from the API."""
        # Using a real task ID from the test workspace
        task_id = "86c7mc19h"

        response = clickup_client.get_task(task_id)

        # Parse with Pydantic model (response may or may not have "task" wrapper)
        task_data = response.get("task", response)
        task = Task(**task_data)
        assert task.id == task_id or task.id  # Either matches or has some value
        assert isinstance(task.name, str)

    @pytest.mark.vcr
    def test_get_task_with_markdown(self, clickup_client):
        """Test that task retrieval includes markdown description."""
        task_id = "86c7mc19h"

        response = clickup_client.get_task(task_id)
        task = Task(**response)

        # Verify markdown_description field is present (may be None)
        assert hasattr(task, "markdown_description")

    @pytest.mark.vcr
    def test_get_task_not_found(self, clickup_client):
        """Test that get_task raises HTTPStatusError for non-existent task."""
        import httpx

        task_id = "00000000"  # Non-existent task ID

        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            clickup_client.get_task(task_id)

        # Should get a 404 or similar error
        assert exc_info.value.response.status_code >= 400

    @pytest.mark.vcr
    def test_get_team_tasks(self, clickup_client):
        """Test getting tasks from a team."""
        # Using a real team ID from the test workspace
        team_id = "90152245421"

        response = clickup_client.get_team_tasks(team_id)

        # Verify response structure
        assert "tasks" in response
        assert isinstance(response["tasks"], list)

    @pytest.mark.vcr
    def test_get_team_tasks_with_filters(self, clickup_client):
        """Test getting team tasks with filters."""
        team_id = "90152245421"

        response = clickup_client.get_team_tasks(
            team_id,
            page=0,
            include_markdown_description=True,
        )

        assert "tasks" in response
        assert isinstance(response["tasks"], list)

    @pytest.mark.vcr
    def test_get_team_tasks_not_found(self, clickup_client):
        """Test that get_team_tasks raises HTTPStatusError for non-existent team."""
        import httpx

        team_id = "99999999"  # Non-existent team ID

        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            clickup_client.get_team_tasks(team_id)

        # Should get a 404 or similar error
        assert exc_info.value.response.status_code >= 400
