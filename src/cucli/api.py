"""ClickUp API client."""

import os
from typing import Any

import httpx


class ClickUpClient:
    """Client for the ClickUp API."""

    def __init__(self, api_key: str | None = None) -> None:
        """Initialize the client.

        Args:
            api_key: ClickUp API key. If not provided, reads from CLICKUP_API_KEY env var.
        """
        self.api_key = api_key or os.environ.get("CLICKUP_API_KEY")
        if not self.api_key:
            raise ValueError(
                "CLICKUP_API_KEY not set. Set it as an environment variable or pass it to the client."
            )

        self.base_url = "https://api.clickup.com/api/v2"
        self._client = httpx.Client(
            headers={"Authorization": self.api_key},
            timeout=30.0,
        )

    def get_teams(self) -> dict[str, Any]:
        """Get all authorized workspaces (teams).

        Returns:
            The response from the /team endpoint.
        """
        response = self._client.get(f"{self.base_url}/team")
        response.raise_for_status()
        return response.json()

    def get_spaces(
        self, team_id: str, *, archived: bool | None = None
    ) -> dict[str, Any]:
        """Get spaces in a workspace.

        Args:
            team_id: The team/workspace ID.
            archived: Include archived spaces.

        Returns:
            The response from the /team/{team_id}/space endpoint.
        """
        params: dict[str, Any] = {}
        if archived is not None:
            params["archived"] = str(archived).lower()

        response = self._client.get(
            f"{self.base_url}/team/{team_id}/space", params=params
        )
        response.raise_for_status()
        return response.json()

    def get_folders(
        self, space_id: str, *, archived: bool | None = None
    ) -> dict[str, Any]:
        """Get folders in a space.

        Args:
            space_id: The space ID.
            archived: Include archived folders.

        Returns:
            The response from the /space/{space_id}/folder endpoint.
        """
        params: dict[str, Any] = {}
        if archived is not None:
            params["archived"] = str(archived).lower()

        response = self._client.get(
            f"{self.base_url}/space/{space_id}/folder", params=params
        )
        response.raise_for_status()
        return response.json()

    def get_lists(
        self, folder_id: str, *, archived: bool | None = None
    ) -> dict[str, Any]:
        """Get lists in a folder.

        Args:
            folder_id: The folder ID.
            archived: Include archived lists.

        Returns:
            The response from the /folder/{folder_id}/list endpoint.
        """
        params: dict[str, Any] = {}
        if archived is not None:
            params["archived"] = str(archived).lower()

        response = self._client.get(
            f"{self.base_url}/folder/{folder_id}/list", params=params
        )
        response.raise_for_status()
        return response.json()

    def get_task(self, task_id: str) -> dict[str, Any]:
        """Get a task by ID.

        Args:
            task_id: The task ID.

        Returns:
            The response from the /task/{task_id} endpoint.
        """
        response = self._client.get(
            f"{self.base_url}/task/{task_id}",
            params={"include_markdown_description": "true"},
        )
        response.raise_for_status()
        return response.json()

    def get_team_tasks(
        self,
        team_id: str,
        *,
        page: int | None = None,
        order_by: str | None = None,
        reverse: bool | None = None,
        subtasks: bool | None = None,
        space_ids: list[str] | None = None,
        project_ids: list[str] | None = None,
        list_ids: list[str] | None = None,
        statuses: list[str] | None = None,
        include_closed: bool | None = None,
        assignees: list[str] | None = None,
        tags: list[str] | None = None,
        due_date_gt: int | None = None,
        due_date_lt: int | None = None,
        date_created_gt: int | None = None,
        date_created_lt: int | None = None,
        date_updated_gt: int | None = None,
        date_updated_lt: int | None = None,
        include_markdown_description: bool | None = None,
    ) -> dict[str, Any]:
        """Get filtered tasks from a team/workspace.

        Args:
            team_id: The team/workspace ID.
            page: Page to fetch (starts at 0).
            order_by: Order by field (id, created, updated, due_date).
            reverse: Reverse the order.
            subtasks: Include subtasks.
            space_ids: Filter by space IDs.
            project_ids: Filter by folder (project) IDs.
            list_ids: Filter by list IDs.
            statuses: Filter by statuses.
            include_closed: Include closed tasks.
            assignees: Filter by assignee IDs.
            tags: Filter by tags.
            due_date_gt: Filter by due date greater than (unix ms).
            due_date_lt: Filter by due date less than (unix ms).
            date_created_gt: Filter by date created greater than (unix ms).
            date_created_lt: Filter by date created less than (unix ms).
            date_updated_gt: Filter by date updated greater than (unix ms).
            date_updated_lt: Filter by date updated less than (unix ms).
            include_markdown_description: Include markdown descriptions.

        Returns:
            The response from the /team/{team_id}/task endpoint.
        """
        params: dict[str, Any] = {}

        if page is not None:
            params["page"] = page
        if order_by is not None:
            params["order_by"] = order_by
        if reverse is not None:
            params["reverse"] = str(reverse).lower()
        if subtasks is not None:
            params["subtasks"] = str(subtasks).lower()
        if include_markdown_description is not None:
            params["include_markdown_description"] = str(
                include_markdown_description
            ).lower()
        if include_closed is not None:
            params["include_closed"] = str(include_closed).lower()

        if space_ids:
            params["space_ids[]"] = space_ids
        if project_ids:
            params["project_ids[]"] = project_ids
        if list_ids:
            params["list_ids[]"] = list_ids
        if statuses:
            params["statuses[]"] = statuses
        if assignees:
            params["assignees[]"] = assignees
        if tags:
            params["tags[]"] = tags

        if due_date_gt is not None:
            params["due_date_gt"] = due_date_gt
        if due_date_lt is not None:
            params["due_date_lt"] = due_date_lt
        if date_created_gt is not None:
            params["date_created_gt"] = date_created_gt
        if date_created_lt is not None:
            params["date_created_lt"] = date_created_lt
        if date_updated_gt is not None:
            params["date_updated_gt"] = date_updated_gt
        if date_updated_lt is not None:
            params["date_updated_lt"] = date_updated_lt

        response = self._client.get(
            f"{self.base_url}/team/{team_id}/task", params=params
        )
        response.raise_for_status()
        return response.json()

    def create_task(
        self,
        list_id: str,
        *,
        name: str,
        description: str | None = None,
        markdown_description: str | None = None,
        status: str | None = None,
        priority: int | None = None,
        assignees: list[int] | None = None,
        tags: list[str] | None = None,
        due_date: int | None = None,
        start_date: int | None = None,
        time_estimate: int | None = None,
        points: int | None = None,
        parent: str | None = None,
    ) -> dict[str, Any]:
        """Create a new task in a list.

        Args:
            list_id: The list ID to create the task in.
            name: The task name (required).
            description: The task description (text content).
            markdown_description: The task description (markdown content).
            status: The task status.
            priority: The task priority (0: Urgent, 1: High, 2: Normal, 3: Low, 4: None).
            assignees: List of assignee user IDs.
            tags: List of tag names.
            due_date: Due date as Unix timestamp in milliseconds.
            start_date: Start date as Unix timestamp in milliseconds.
            time_estimate: Time estimate in milliseconds.
            points: Sprint points.
            parent: Parent task ID (for subtasks).

        Returns:
            The response from the /list/{list_id}/task endpoint.
        """
        data: dict[str, Any] = {"name": name}

        if description is not None:
            data["description"] = description
        if markdown_description is not None:
            data["markdown_content"] = markdown_description
        if status is not None:
            data["status"] = status
        if priority is not None:
            data["priority"] = priority
        if assignees:
            data["assignees"] = assignees
        if tags:
            data["tags"] = tags
        if due_date is not None:
            data["due_date"] = due_date
        if start_date is not None:
            data["start_date"] = start_date
        if time_estimate is not None:
            data["time_estimate"] = time_estimate
        if points is not None:
            data["points"] = points
        if parent is not None:
            data["parent"] = parent

        response = self._client.post(f"{self.base_url}/list/{list_id}/task", json=data)
        response.raise_for_status()
        return response.json()

    def update_task(
        self,
        task_id: str,
        *,
        name: str | None = None,
        description: str | None = None,
        markdown_description: str | None = None,
        status: str | None = None,
        priority: int | None = None,
        due_date: int | None = None,
        start_date: int | None = None,
        time_estimate: int | None = None,
        points: int | None = None,
        parent: str | None = None,
        assignees_add: list[int] | None = None,
        assignees_remove: list[int] | None = None,
    ) -> dict[str, Any]:
        """Update a task.

        Args:
            task_id: The task ID to update.
            name: The task name.
            description: The task description (text content).
            markdown_description: The task description (markdown content).
            status: The task status.
            priority: The task priority (0: Urgent, 1: High, 2: Normal, 3: Low, 4: None).
            due_date: Due date as Unix timestamp in milliseconds.
            start_date: Start date as Unix timestamp in milliseconds.
            time_estimate: Time estimate in milliseconds.
            points: Sprint points.
            parent: Parent task ID (for subtasks).
            assignees_add: List of assignee user IDs to add.
            assignees_remove: List of assignee user IDs to remove.

        Returns:
            The response from the /task/{task_id} endpoint.
        """
        data: dict[str, Any] = {}

        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if markdown_description is not None:
            data["markdown_content"] = markdown_description
        if status is not None:
            data["status"] = status
        if priority is not None:
            data["priority"] = priority
        if due_date is not None:
            data["due_date"] = due_date
        if start_date is not None:
            data["start_date"] = start_date
        if time_estimate is not None:
            data["time_estimate"] = time_estimate
        if points is not None:
            data["points"] = points
        if parent is not None:
            data["parent"] = parent

        if assignees_add or assignees_remove:
            assignees_dict: dict[str, list[int]] = {}
            if assignees_add:
                assignees_dict["add"] = assignees_add
            if assignees_remove:
                assignees_dict["rem"] = assignees_remove
            data["assignees"] = assignees_dict

        if data:
            response = self._client.put(f"{self.base_url}/task/{task_id}", json=data)
            response.raise_for_status()
            return response.json()

        return {}

    def delete_task(self, task_id: str) -> dict[str, Any] | None:
        """Delete a task.

        Args:
            task_id: The task ID to delete.

        Returns:
            None (204 No Content) or response dict.
        """
        response = self._client.delete(f"{self.base_url}/task/{task_id}")
        if response.status_code == 204:
            return None
        response.raise_for_status()
        return response.json()

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def __enter__(self) -> "ClickUpClient":
        """Context manager entry."""
        return self

    def __exit__(self, *_: Any) -> None:
        """Context manager exit."""
        self.close()
