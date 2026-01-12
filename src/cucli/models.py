"""Pydantic models for ClickUp API responses."""
from typing import Any

from pydantic import BaseModel, Field


class InvitedBy(BaseModel):
    """User who invited a member."""

    id: int
    username: str
    color: str
    email: str
    initials: str
    profilePicture: str | None = None
    banned_date: str | None = None
    status: str | None = None


class User(BaseModel):
    """A ClickUp user."""

    id: int
    username: str
    email: str
    color: str
    profilePicture: str | None = None
    initials: str
    role: int
    role_subtype: int
    role_key: str
    custom_role: str | None = None
    last_active: str | None = None
    date_joined: str | None = None
    date_invited: str | None = None


class Member(BaseModel):
    """A team member."""

    user: User
    invited_by: InvitedBy | None = None
    can_see_time_spent: bool | None = None
    can_see_time_estimated: bool | None = None
    can_see_points_estimated: bool | None = None
    can_edit_tags: bool | None = None
    can_create_views: bool | None = None


class Team(BaseModel):
    """A ClickUp workspace/team."""

    id: str
    name: str
    color: str
    avatar: str
    members: list[Member] = Field(default_factory=list)


class TeamsResponse(BaseModel):
    """Response from the /team endpoint."""

    teams: list[Team] = Field(default_factory=list)


# For raw output when models don't match
RawResponse = dict[str, Any]
