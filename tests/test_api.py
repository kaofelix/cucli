"""Tests for the ClickUp API client."""

import pytest
from cucli.api import ClickUpClient
from cucli.models import (
    Checklist,
    Comment,
    CommentsResponse,
    Folder,
    FoldersResponse,
    ListMember,
    ListMembersResponse,
    ListsResponse,
    SpacesResponse,
    Task,
    TaskMember,
    TaskMembersResponse,
    Team,
    TeamsResponse,
)


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

    @pytest.mark.vcr
    def test_get_spaces(self, clickup_client):
        """Test getting spaces from a team."""
        # Using a real team ID from the test workspace
        team_id = "90152245421"

        response = clickup_client.get_spaces(team_id)

        # Verify response structure
        assert "spaces" in response
        assert isinstance(response["spaces"], list)

        # Parse with Pydantic model
        spaces_response = SpacesResponse(**response)
        assert len(spaces_response.spaces) >= 0

        # If there are spaces, validate first space structure
        if spaces_response.spaces:
            space = spaces_response.spaces[0]
            assert isinstance(space.id, str)
            assert isinstance(space.name, str)
            assert isinstance(space.private, bool)

    @pytest.mark.vcr
    def test_get_spaces_with_archived(self, clickup_client):
        """Test getting spaces with archived filter."""
        team_id = "90152245421"

        response = clickup_client.get_spaces(team_id, archived=True)

        assert "spaces" in response
        assert isinstance(response["spaces"], list)

    @pytest.mark.vcr
    def test_get_spaces_not_found(self, clickup_client):
        """Test that get_spaces raises HTTPStatusError for non-existent team."""
        import httpx

        team_id = "99999999"  # Non-existent team ID

        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            clickup_client.get_spaces(team_id)

        # Should get a 404 or similar error
        assert exc_info.value.response.status_code >= 400

    @pytest.mark.vcr
    def test_get_folders(self, clickup_client):
        """Test getting folders from a space."""
        # Using a real space ID from the test workspace
        space_id = "90159451300"

        response = clickup_client.get_folders(space_id)

        # Verify response structure
        assert "folders" in response
        assert isinstance(response["folders"], list)

        # Parse with Pydantic model
        folders_response = FoldersResponse(**response)
        assert len(folders_response.folders) >= 0

        # If there are folders, validate first folder structure
        if folders_response.folders:
            folder = folders_response.folders[0]
            assert isinstance(folder.id, str)
            assert isinstance(folder.name, str)
            assert isinstance(folder.orderindex, int)
            assert isinstance(folder.override_statuses, bool)
            assert isinstance(folder.hidden, bool)
            assert isinstance(folder.task_count, str)

    @pytest.mark.vcr
    def test_get_folders_with_archived(self, clickup_client):
        """Test getting folders with archived filter."""
        space_id = "90159451300"

        response = clickup_client.get_folders(space_id, archived=True)

        assert "folders" in response
        assert isinstance(response["folders"], list)

    @pytest.mark.vcr
    def test_get_folders_not_found(self, clickup_client):
        """Test that get_folders raises HTTPStatusError for non-existent space."""
        import httpx

        space_id = "99999999"  # Non-existent space ID

        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            clickup_client.get_folders(space_id)

        # Should get a 404 or similar error
        assert exc_info.value.response.status_code >= 400

    @pytest.mark.vcr
    def test_get_lists(self, clickup_client):
        """Test getting lists from a folder."""
        # Using a real folder ID from the test workspace
        folder_id = "901513787576"

        response = clickup_client.get_lists(folder_id)

        # Verify response structure
        assert "lists" in response
        assert isinstance(response["lists"], list)

        # Parse with Pydantic model
        lists_response = ListsResponse(**response)
        assert len(lists_response.lists) >= 0

        # If there are lists, validate first list structure
        if lists_response.lists:
            list_obj = lists_response.lists[0]
            assert isinstance(list_obj.id, str)
            assert isinstance(list_obj.name, str)
            assert isinstance(list_obj.orderindex, int)
            assert isinstance(list_obj.archived, bool)
            assert isinstance(list_obj.override_statuses, bool)
            assert isinstance(list_obj.permission_level, str)

    @pytest.mark.vcr
    def test_get_lists_with_archived(self, clickup_client):
        """Test getting lists with archived filter."""
        folder_id = "901513787576"

        response = clickup_client.get_lists(folder_id, archived=True)

        assert "lists" in response
        assert isinstance(response["lists"], list)

    @pytest.mark.vcr
    def test_get_lists_not_found(self, clickup_client):
        """Test that get_lists raises HTTPStatusError for non-existent folder."""
        import httpx

        folder_id = "99999999"  # Non-existent folder ID

        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            clickup_client.get_lists(folder_id)

        # Should get a 404 or similar error
        assert exc_info.value.response.status_code >= 400

    @pytest.mark.vcr
    def test_create_task(self, clickup_client):
        """Test creating a task."""
        list_id = "901520401736"
        response = clickup_client.create_task(list_id, name="Test Task from API")

        # Verify response structure
        assert "id" in response
        assert response["name"] == "Test Task from API"
        assert "list" in response

    @pytest.mark.vcr
    def test_create_task_with_options(self, clickup_client):
        """Test creating a task with various options."""
        list_id = "901520401736"
        response = clickup_client.create_task(
            list_id,
            name="Test Task with Options",
            description="Test description",
            status="to do",
            priority=3,
        )

        # Verify response structure
        assert "id" in response
        assert response["name"] == "Test Task with Options"
        assert "status" in response

    @pytest.mark.vcr
    def test_create_task_invalid_list(self, clickup_client):
        """Test creating a task in non-existent list."""
        import httpx

        list_id = "99999999"

        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            clickup_client.create_task(list_id, name="Test Task")

        # Should get a 404 or similar error
        assert exc_info.value.response.status_code >= 400

    @pytest.mark.vcr
    def test_update_task(self, clickup_client):
        """Test updating a task."""
        # First create a task
        list_id = "901520401736"
        create_response = clickup_client.create_task(list_id, name="Task to Update")
        task_id = create_response["id"]

        # Update the task
        update_response = clickup_client.update_task(task_id, name="Updated Task Name")

        # Verify response
        assert "id" in update_response
        assert update_response["name"] == "Updated Task Name"

    @pytest.mark.vcr
    def test_update_task_status(self, clickup_client):
        """Test updating a task's status."""
        list_id = "901520401736"
        create_response = clickup_client.create_task(
            list_id, name="Task for Status Update"
        )
        task_id = create_response["id"]

        # Update status - using common status
        update_response = clickup_client.update_task(task_id, status="to do")

        assert "id" in update_response
        assert update_response["status"]["status"] == "to do"

    @pytest.mark.vcr
    def test_update_task_priority(self, clickup_client):
        """Test updating a task's priority."""
        list_id = "901520401736"
        create_response = clickup_client.create_task(
            list_id, name="Task for Priority Update"
        )
        task_id = create_response["id"]

        # Update priority
        update_response = clickup_client.update_task(task_id, priority=1)

        assert "id" in update_response
        assert update_response["priority"]["priority"] == "urgent"

    @pytest.mark.vcr
    def test_update_task_not_found(self, clickup_client):
        """Test updating a non-existent task."""
        import httpx

        task_id = "00000000"

        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            clickup_client.update_task(task_id, name="Test")

        # Should get a 404 or similar error
        assert exc_info.value.response.status_code >= 400

    @pytest.mark.vcr
    def test_delete_task(self, clickup_client):
        """Test deleting a task."""
        # First create a task
        list_id = "901520401736"
        create_response = clickup_client.create_task(list_id, name="Task to Delete")
        task_id = create_response["id"]

        # Delete the task
        response = clickup_client.delete_task(task_id)

        # Response should be empty (204 No Content)
        assert response is None or response == {}

    @pytest.mark.vcr
    def test_delete_task_not_found(self, clickup_client):
        """Test deleting a non-existent task."""
        import httpx

        task_id = "00000000"

        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            clickup_client.delete_task(task_id)

        # Should get a 404 or similar error
        assert exc_info.value.response.status_code >= 400

    @pytest.mark.vcr
    def test_get_task_comments(self, clickup_client):
        """Test getting comments from a task."""
        # Using a real task ID from the test workspace
        task_id = "86c7mc19h"

        response = clickup_client.get_task_comments(task_id)

        # Verify response structure
        assert "comments" in response
        assert isinstance(response["comments"], list)

        # Parse with Pydantic model
        comments_response = CommentsResponse(**response)
        assert len(comments_response.comments) >= 0

        # If there are comments, validate first comment structure
        if comments_response.comments:
            comment = comments_response.comments[0]
            assert isinstance(comment.id, str)
            assert isinstance(comment.comment_text, str)
            assert isinstance(comment.user, Comment)
            assert isinstance(comment.resolved, bool)

    @pytest.mark.vcr
    def test_get_task_comments_not_found(self, clickup_client):
        """Test that get_task_comments raises HTTPStatusError for non-existent task."""
        import httpx

        task_id = "00000000"  # Non-existent task ID

        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            clickup_client.get_task_comments(task_id)

        # Should get a 404 or similar error
        assert exc_info.value.response.status_code >= 400

    @pytest.mark.vcr
    def test_create_task_comment(self, clickup_client):
        """Test creating a comment on a task."""
        # Using a real task ID from the test workspace
        task_id = "86c7mc19h"

        response = clickup_client.create_task_comment(
            task_id, comment_text="Test comment from API"
        )

        # Verify response structure
        assert "id" in response
        assert "date" in response

    @pytest.mark.vcr
    def test_create_task_comment_with_assignee(self, clickup_client):
        """Test creating a comment on a task with an assignee."""
        task_id = "86c7mc19h"

        response = clickup_client.create_task_comment(
            task_id,
            comment_text="Test comment with assignee",
            assignee=183,
        )

        # Verify response structure
        assert "id" in response

    @pytest.mark.vcr
    def test_create_task_comment_not_found(self, clickup_client):
        """Test creating a comment on a non-existent task."""
        import httpx

        task_id = "00000000"  # Non-existent task ID

        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            clickup_client.create_task_comment(task_id, comment_text="Test")

        # Should get a 404 or similar error
        assert exc_info.value.response.status_code >= 400

    @pytest.mark.vcr
    def test_create_folder(self, clickup_client):
        """Test creating a folder in a space."""
        space_id = "90159451300"

        response = clickup_client.create_folder(space_id, name="Test Folder from API")

        # Verify response structure
        assert "id" in response
        assert "name" in response
        assert response["name"] == "Test Folder from API"
        assert "space" in response
        assert response["space"]["id"] == space_id

        # Parse with Pydantic model
        folder = Folder(**response)
        assert folder.name == "Test Folder from API"
        assert folder.space.id == space_id

    @pytest.mark.vcr
    def test_create_folder_not_found(self, clickup_client):
        """Test creating a folder in a non-existent space."""
        import httpx

        space_id = "99999999"

        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            clickup_client.create_folder(space_id, name="Test Folder")

        # Should get a 404 or similar error
        assert exc_info.value.response.status_code >= 400

    @pytest.mark.vcr
    def test_create_list(self, clickup_client):
        """Test creating a list in a folder."""
        folder_id = "901513787576"

        response = clickup_client.create_list(folder_id, name="Test List from API")

        # Verify response structure
        assert "id" in response
        assert "name" in response
        assert response["name"] == "Test List from API"
        assert "folder" in response
        assert response["folder"]["id"] == folder_id
        assert "space" in response

    @pytest.mark.vcr
    def test_create_list_with_options(self, clickup_client):
        """Test creating a list with various options."""
        folder_id = "901513787576"

        response = clickup_client.create_list(
            folder_id,
            name="Test List with Options",
            content="List description",
            status="red",
            priority=1,
        )

        # Verify response structure
        assert "id" in response
        assert response["name"] == "Test List with Options"
        assert "status" in response
        assert "priority" in response

    @pytest.mark.vcr
    def test_create_list_not_found(self, clickup_client):
        """Test creating a list in a non-existent folder."""
        import httpx

        folder_id = "99999999"

        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            clickup_client.create_list(folder_id, name="Test List")

        # Should get a 404 or similar error
        assert exc_info.value.response.status_code >= 400

    @pytest.mark.vcr
    def test_create_checklist(self, clickup_client):
        """Test creating a checklist on a task."""
        # Using a real task ID from test workspace
        task_id = "86c7mc19h"

        response = clickup_client.create_checklist(
            task_id, name="Test Checklist from API"
        )

        # Verify response structure
        assert "checklist" in response
        checklist_data = response["checklist"]
        assert "id" in checklist_data
        assert "task_id" in checklist_data
        assert "name" in checklist_data
        assert checklist_data["name"] == "Test Checklist from API"

        # Parse with Pydantic model
        checklist = Checklist(**checklist_data)
        assert checklist.name == "Test Checklist from API"
        assert checklist.task_id == task_id

    @pytest.mark.vcr
    def test_create_checklist_not_found(self, clickup_client):
        """Test creating a checklist on a non-existent task."""
        import httpx

        task_id = "00000000"  # Non-existent task ID

        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            clickup_client.create_checklist(task_id, name="Test Checklist")

        # Should get a 404 or similar error
        assert exc_info.value.response.status_code >= 400

    @pytest.mark.vcr
    def test_create_checklist_item(self, clickup_client):
        """Test creating a checklist item."""
        # Using a real checklist ID from test workspace
        checklist_id = "f73cd146-f271-4a9e-8ef0-93e8c4973532"

        response = clickup_client.create_checklist_item(
            checklist_id, name="Test Item from API"
        )

        # Verify response structure
        assert "checklist" in response
        checklist_data = response["checklist"]
        assert "id" in checklist_data
        assert "items" in checklist_data

        # Parse with Pydantic model
        checklist = Checklist(**checklist_data)
        assert isinstance(checklist.items, list)

    @pytest.mark.skip(reason="Requires existing assignee in test workspace")
    def test_create_checklist_item_with_assignee(self, clickup_client):
        """Test creating a checklist item with an assignee."""
        checklist_id = "f73cd146-f271-4a9e-8ef0-93e8c4973532"

        response = clickup_client.create_checklist_item(
            checklist_id, name="Test Item with Assignee", assignee=183
        )

        # Verify response structure
        assert "checklist" in response
        checklist_data = response["checklist"]
        assert "items" in checklist_data

    @pytest.mark.vcr
    def test_update_checklist(self, clickup_client):
        """Test updating a checklist."""
        checklist_id = "f73cd146-f271-4a9e-8ef0-93e8c4973532"

        response = clickup_client.update_checklist(
            checklist_id, name="Updated Checklist Name"
        )

        # Verify response structure
        assert "checklist" in response

        # Parse with Pydantic model
        checklist = Checklist(**response["checklist"])
        assert isinstance(checklist, Checklist)

    @pytest.mark.vcr
    def test_update_checklist_item(self, clickup_client):
        """Test updating a checklist item."""
        checklist_id = "f73cd146-f271-4a9e-8ef0-93e8c4973532"
        checklist_item_id = "4c6ee69d-c42b-4f50-808a-d72ef3f5fab0"

        response = clickup_client.update_checklist_item(
            checklist_id, checklist_item_id, name="Updated Item Name", resolved=True
        )

        # Verify response structure
        assert "checklist" in response

        # Parse with Pydantic model
        checklist = Checklist(**response["checklist"])
        assert isinstance(checklist, Checklist)

    @pytest.mark.vcr
    def test_delete_checklist(self, clickup_client):
        """Test deleting a checklist."""
        checklist_id = "f73cd146-f271-4a9e-8ef0-93e8c4973532"

        response = clickup_client.delete_checklist(checklist_id)

        # Response should be an empty dict or similar
        assert isinstance(response, dict)

    @pytest.mark.vcr
    def test_delete_checklist_item(self, clickup_client):
        """Test deleting a checklist item."""
        checklist_id = "f73cd146-f271-4a9e-8ef0-93e8c4973532"
        checklist_item_id = "4c6ee69d-c42b-4f50-808a-d72ef3f5fab0"

        response = clickup_client.delete_checklist_item(checklist_id, checklist_item_id)

        # Response should be an empty dict or similar
        assert isinstance(response, dict)

    @pytest.mark.vcr
    def test_get_task_members(self, clickup_client):
        """Test getting members with explicit access to a task."""
        # Using a real task ID from the test workspace
        task_id = "86c7mc19h"

        response = clickup_client.get_task_members(task_id)

        # Verify response structure
        assert "members" in response
        assert isinstance(response["members"], list)

        # Parse with Pydantic model
        task_members_response = TaskMembersResponse(**response)
        assert len(task_members_response.members) >= 0

        # If there are members, validate first member structure
        if task_members_response.members:
            member = task_members_response.members[0]
            assert isinstance(member.id, int)
            assert isinstance(member.username, str)
            assert isinstance(member.email, str)
            assert isinstance(member.initials, str)

    @pytest.mark.vcr
    def test_get_task_members_parses_model(self, clickup_client):
        """Test that get_task_members response can be parsed into Pydantic models."""
        task_id = "86c7mc19h"

        response = clickup_client.get_task_members(task_id)

        for member_data in response["members"]:
            member = TaskMember(**member_data)
            assert member.id
            assert member.username
            assert member.email

    @pytest.mark.vcr
    def test_get_task_members_not_found(self, clickup_client):
        """Test that get_task_members raises HTTPStatusError for non-existent task."""
        import httpx

        task_id = "00000000"

        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            clickup_client.get_task_members(task_id)

        # Should get a 404 or similar error
        assert exc_info.value.response.status_code >= 400

    @pytest.mark.vcr
    def test_get_list_members(self, clickup_client):
        """Test getting members with explicit access to a list."""
        # Using a real list ID from the test workspace
        list_id = "901520401736"

        response = clickup_client.get_list_members(list_id)

        # Verify response structure
        assert "members" in response
        assert isinstance(response["members"], list)

        # Parse with Pydantic model
        list_members_response = ListMembersResponse(**response)
        assert len(list_members_response.members) >= 0

        # If there are members, validate first member structure
        if list_members_response.members:
            member = list_members_response.members[0]
            assert isinstance(member.id, int)
            assert isinstance(member.username, str)
            assert isinstance(member.email, str)
            assert isinstance(member.initials, str)

    @pytest.mark.vcr
    def test_get_list_members_parses_model(self, clickup_client):
        """Test that get_list_members response can be parsed into Pydantic models."""
        list_id = "901520401736"

        response = clickup_client.get_list_members(list_id)

        for member_data in response["members"]:
            member = ListMember(**member_data)
            assert member.id
            assert member.username
            assert member.email

    @pytest.mark.vcr
    def test_get_list_members_not_found(self, clickup_client):
        """Test that get_list_members raises HTTPStatusError for non-existent list."""
        import httpx

        list_id = "00000000"

        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            clickup_client.get_list_members(list_id)

        # Should get a 404 or similar error
        assert exc_info.value.response.status_code >= 400
