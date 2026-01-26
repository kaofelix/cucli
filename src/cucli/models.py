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
    avatar: str | None = None
    members: list[Member] = Field(default_factory=list)


class TeamsResponse(BaseModel):
    """Response from the /team endpoint."""

    teams: list[Team] = Field(default_factory=list)


class Task(BaseModel):
    """A ClickUp task."""

    id: str
    name: str
    description: str | None = None
    markdown_description: str | None = None
    status: dict[str, Any] | None = None
    priority: dict[str, Any] | None = None
    assignees: list[dict[str, Any]] = Field(default_factory=list)
    tags: list[dict[str, Any]] = Field(default_factory=list)
    due_date: str | None = None
    start_date: str | None = None
    time_estimate: str | None = None
    time_spent: int | None = None


class TaskResponse(BaseModel):
    """Response from the /task/{task_id} endpoint."""

    task: Task | None = None


class Space(BaseModel):
    """A ClickUp space."""

    id: str
    name: str
    private: bool
    statuses: list[dict[str, Any]] = Field(default_factory=list)
    multiple_assignees: bool | None = None
    features: dict[str, Any] | None = None
    archived: bool | None = None


class SpacesResponse(BaseModel):
    """Response from the /team/{team_id}/space endpoint."""

    spaces: list[Space] = Field(default_factory=list)


class FolderSpaceReference(BaseModel):
    """A space reference within a folder."""

    id: str
    name: str
    access: bool


class Folder(BaseModel):
    """A ClickUp folder."""

    id: str
    name: str
    orderindex: int
    override_statuses: bool
    hidden: bool
    space: FolderSpaceReference
    task_count: str
    lists: list[str] = Field(default_factory=list)


class FoldersResponse(BaseModel):
    """Response from the /space/{space_id}/folder endpoint."""

    folders: list[Folder] = Field(default_factory=list)


class FolderReference(BaseModel):
    """A folder reference within a list."""

    id: str
    name: str
    hidden: bool
    access: bool


class SpaceReference(BaseModel):
    """A space reference within a list."""

    id: str
    name: str
    access: bool


class ListStatus(BaseModel):
    """A list status."""

    status: str | None = None
    color: str | None = None
    hide_label: bool | None = None


class ListPriority(BaseModel):
    """A list priority."""

    priority: str | None = None
    color: str | None = None


class ClickUpList(BaseModel):
    """A ClickUp list (named List to avoid conflict with Python's built-in list)."""

    id: str
    name: str
    orderindex: int
    content: str | None = None
    status: ListStatus | None = None
    priority: ListPriority | None = None
    assignee: str | None = None
    task_count: str | int | None = None
    due_date: str | None = None
    start_date: str | None = None
    folder: FolderReference
    space: SpaceReference
    archived: bool
    override_statuses: bool
    permission_level: str


class ListsResponse(BaseModel):
    """Response from the /folder/{folder_id}/list endpoint."""

    lists: list[ClickUpList] = Field(default_factory=list)


class CommentUser(BaseModel):
    """A user associated with a comment."""

    id: int
    username: str
    email: str
    color: str
    initials: str
    profilePicture: str | None = None


class Comment(BaseModel):
    """A ClickUp comment."""

    id: str
    comment: list[dict[str, str]] = Field(default_factory=list)
    comment_text: str
    user: CommentUser
    resolved: bool = False
    assignee: CommentUser | None = None
    assigned_by: CommentUser | None = None
    reactions: list[str] = Field(default_factory=list)
    date: str
    reply_count: str | int | None = None


class CommentsResponse(BaseModel):
    """Response from comment endpoints."""

    comments: list[Comment] = Field(default_factory=list)


class ChecklistItemAssignee(BaseModel):
    """Assignee for a checklist item."""

    id: int
    username: str
    email: str
    color: str
    initials: str
    profilePicture: str | None = None


class ChecklistItem(BaseModel):
    """A checklist item."""

    id: str
    name: str
    orderindex: int | None = None
    assignee: ChecklistItemAssignee | None = None
    resolved: bool
    parent: str | None = None
    date_created: str
    children: list[str] = Field(default_factory=list)


class Checklist(BaseModel):
    """A ClickUp checklist."""

    id: str
    task_id: str
    name: str
    orderindex: int
    resolved: int
    unresolved: int
    items: list[ChecklistItem] = Field(default_factory=list)
    date_created: str | None = None


class ChecklistResponse(BaseModel):
    """Response from checklist endpoints."""

    checklist: Checklist


class ProfileInfo(BaseModel):
    """Profile information for a member."""

    display_profile: str | None = None
    verified_ambassador: str | None = None
    verified_consultant: str | None = None
    top_tier_user: str | None = None
    ai_expert: str | None = None
    viewed_verified_ambassador: str | None = None
    viewed_verified_consultant: str | None = None
    viewed_top_tier_user: str | None = None
    viewed_ai_expert: str | None = None


class TaskMember(BaseModel):
    """A member with explicit access to a task."""

    id: int
    username: str
    email: str
    color: str | None = None
    initials: str
    profilePicture: str | None = None
    profileInfo: ProfileInfo


class TaskMembersResponse(BaseModel):
    """Response from the /task/{task_id}/member endpoint."""

    members: list[TaskMember] = Field(default_factory=list)


class ListMember(BaseModel):
    """A member with explicit access to a list."""

    id: int
    username: str
    email: str
    color: str | None = None
    initials: str
    profilePicture: str | None = None
    profileInfo: ProfileInfo


class ListMembersResponse(BaseModel):
    """Response from the /list/{list_id}/member endpoint."""

    members: list[ListMember] = Field(default_factory=list)


class Tag(BaseModel):
    """A ClickUp tag."""

    name: str
    tag_fg: str
    tag_bg: str


class TagsResponse(BaseModel):
    """Response from tag endpoints."""

    tags: list[Tag] = Field(default_factory=list)


# For raw output when models don't match
RawResponse = dict[str, Any]
