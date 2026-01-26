"""Tests for Pydantic models."""

from cucli.models import (
    InvitedBy,
    Member,
    Task,
    Team,
    TeamsResponse,
    TaskResponse,
    User,
)


class TestUser:
    """Test cases for User model."""

    def test_user_creation(self):
        """Test creating a User instance."""
        user_data = {
            "id": 123,
            "username": "testuser",
            "email": "test@example.com",
            "color": "#ff0000",
            "profilePicture": "https://example.com/pic.jpg",
            "initials": "TU",
            "role": 1,
            "role_subtype": 0,
            "role_key": "member",
        }
        user = User(**user_data)
        assert user.id == 123
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.color == "#ff0000"

    def test_user_without_optional_fields(self):
        """Test creating a User with minimal required fields."""
        user_data = {
            "id": 123,
            "username": "testuser",
            "email": "test@example.com",
            "color": "#ff0000",
            "initials": "TU",
            "role": 1,
            "role_subtype": 0,
            "role_key": "member",
        }
        user = User(**user_data)
        assert user.profilePicture is None
        assert user.custom_role is None


class TestTeam:
    """Test cases for Team model."""

    def test_team_creation(self):
        """Test creating a Team instance."""
        team_data = {
            "id": "12345678",
            "name": "Test Workspace",
            "color": "#00ff00",
            "avatar": "https://example.com/avatar.png",
        }
        team = Team(**team_data)
        assert team.id == "12345678"
        assert team.name == "Test Workspace"
        assert team.color == "#00ff00"
        assert team.avatar == "https://example.com/avatar.png"
        assert team.members == []

    def test_team_with_members(self):
        """Test creating a Team with members."""
        user_data = {
            "id": 123,
            "username": "testuser",
            "email": "test@example.com",
            "color": "#ff0000",
            "initials": "TU",
            "role": 1,
            "role_subtype": 0,
            "role_key": "member",
        }
        member_data = {"user": user_data}
        team_data = {
            "id": "12345678",
            "name": "Test Workspace",
            "color": "#00ff00",
            "avatar": "https://example.com/avatar.png",
            "members": [member_data],
        }
        team = Team(**team_data)
        assert len(team.members) == 1
        assert team.members[0].user.username == "testuser"


class TestTeamsResponse:
    """Test cases for TeamsResponse model."""

    def test_teams_response_creation(self):
        """Test creating a TeamsResponse instance."""
        response_data = {
            "teams": [
                {
                    "id": "12345678",
                    "name": "Test Workspace",
                    "color": "#00ff00",
                    "avatar": "https://example.com/avatar.png",
                }
            ]
        }
        response = TeamsResponse(**response_data)
        assert len(response.teams) == 1
        assert response.teams[0].name == "Test Workspace"

    def test_teams_response_empty(self):
        """Test creating a TeamsResponse with empty teams list."""
        response = TeamsResponse()
        assert response.teams == []
        response2 = TeamsResponse(teams=[])
        assert response2.teams == []


class TestTask:
    """Test cases for Task model."""

    def test_task_creation_minimal(self):
        """Test creating a Task with minimal required fields."""
        task_data = {
            "id": "86abc123",
            "name": "Test Task",
        }
        task = Task(**task_data)
        assert task.id == "86abc123"
        assert task.name == "Test Task"
        assert task.description is None
        assert task.markdown_description is None
        assert task.status is None
        assert task.priority is None
        assert task.assignees == []
        assert task.tags == []

    def test_task_creation_full(self):
        """Test creating a Task with all fields."""
        task_data = {
            "id": "86abc123",
            "name": "Test Task",
            "description": "Task description",
            "markdown_description": "## Markdown Description",
            "status": {"status": "In Progress", "color": "#ffff00"},
            "priority": {"priority": "urgent", "color": "#ff0000"},
            "assignees": [
                {"id": 123, "username": "user1"},
                {"id": 456, "username": "user2"},
            ],
            "tags": [{"name": "frontend", "color": "#00ff00"}],
            "due_date": "1634567890000",
            "start_date": "1634567890000",
            "time_estimate": "3600000",
            "time_spent": 1800000,
        }
        task = Task(**task_data)
        assert task.id == "86abc123"
        assert task.name == "Test Task"
        assert task.description == "Task description"
        assert task.markdown_description == "## Markdown Description"
        assert task.status["status"] == "In Progress"
        assert task.priority["priority"] == "urgent"
        assert len(task.assignees) == 2
        assert task.assignees[0]["username"] == "user1"
        assert len(task.tags) == 1
        assert task.tags[0]["name"] == "frontend"
        assert task.due_date == "1634567890000"

    def test_task_without_markdown(self):
        """Test creating a Task with description but no markdown_description."""
        task_data = {
            "id": "86abc123",
            "name": "Test Task",
            "description": "Plain description",
        }
        task = Task(**task_data)
        assert task.description == "Plain description"
        assert task.markdown_description is None


class TestTaskResponse:
    """Test cases for TaskResponse model."""

    def test_task_response_creation(self):
        """Test creating a TaskResponse instance."""
        response_data = {
            "task": {
                "id": "86abc123",
                "name": "Test Task",
            }
        }
        response = TaskResponse(**response_data)
        assert response.task is not None
        assert response.task.id == "86abc123"

    def test_task_response_null_task(self):
        """Test creating a TaskResponse with null task."""
        response = TaskResponse()
        assert response.task is None
        response2 = TaskResponse(task=None)
        assert response2.task is None


class TestMember:
    """Test cases for Member model."""

    def test_member_creation(self):
        """Test creating a Member instance."""
        user_data = {
            "id": 123,
            "username": "testuser",
            "email": "test@example.com",
            "color": "#ff0000",
            "initials": "TU",
            "role": 1,
            "role_subtype": 0,
            "role_key": "member",
        }
        member_data = {
            "user": user_data,
            "can_see_time_spent": True,
            "can_see_time_estimated": False,
        }
        member = Member(**member_data)
        assert member.user.username == "testuser"
        assert member.can_see_time_spent is True
        assert member.can_see_time_estimated is False
        assert member.invited_by is None


class TestInvitedBy:
    """Test cases for InvitedBy model."""

    def test_invited_by_creation(self):
        """Test creating an InvitedBy instance."""
        invited_by_data = {
            "id": 456,
            "username": "inviter",
            "email": "inviter@example.com",
            "color": "#00ff00",
            "initials": "IN",
            "profilePicture": "https://example.com/inviter.jpg",
        }
        invited_by = InvitedBy(**invited_by_data)
        assert invited_by.id == 456
        assert invited_by.username == "inviter"
        assert invited_by.email == "inviter@example.com"
