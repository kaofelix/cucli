"""ClickUp API client."""

import os
from typing import Any, Callable

import httpx


def with_client(func: Callable[[Any], Any]) -> Any:
    """Execute a function with a ClickUpClient instance.

    This helper function eliminates the need for repeated
    `with ClickUpClient() as client:` patterns in CLI commands.

    Args:
        func: A callable that takes a ClickUpClient as its only argument.

    Returns:
        The result of calling func with the client.

    Example:
        data = with_client(lambda client: client.get_teams())
    """
    with ClickUpClient() as client:
        return func(client)


class ClickUpClient:
    """Client for the ClickUp API."""

    @staticmethod
    def _to_bool_str(value: bool | None) -> str | None:
        """Convert a boolean value to a lowercase string for API parameters.

        Args:
            value: The boolean value to convert.

        Returns:
            "true" or "false" as lowercase string, or None if value is None.
        """
        if value is None:
            return None
        return str(value).lower()

    def _delete_with_204_handling(
        self, url: str, *, headers: dict[str, str] | None = None
    ) -> dict[str, Any] | None:
        """Perform a DELETE request with special handling for 204 No Content responses.

        This helper eliminates the repeated pattern of:
            response = self._client.delete(url)
            if response.status_code == 204:
                return None
            response.raise_for_status()
            return response.json()

        Args:
            url: The full URL to send the DELETE request to.
            headers: Optional headers to include in the request.

        Returns:
            None (204 No Content) or response dict.

        Example:
            result = self._delete_with_204_handling(f"{self.base_url}/folder/{folder_id}")
        """
        kwargs = {}
        if headers:
            kwargs["headers"] = headers
        response = self._client.delete(url, **kwargs)
        if response.status_code == 204:
            return None
        response.raise_for_status()
        return response.json()

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
            params["archived"] = self._to_bool_str(archived)

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
            params["archived"] = self._to_bool_str(archived)

        response = self._client.get(
            f"{self.base_url}/space/{space_id}/folder", params=params
        )
        response.raise_for_status()
        return response.json()

    def create_folder(self, space_id: str, *, name: str) -> dict[str, Any]:
        """Create a new folder in a space.

        Args:
            space_id: The space ID to create the folder in.
            name: The folder name.

        Returns:
            The response from the /space/{space_id}/folder endpoint.
        """
        data: dict[str, Any] = {"name": name}

        response = self._client.post(
            f"{self.base_url}/space/{space_id}/folder", json=data
        )
        response.raise_for_status()
        return response.json()

    def get_folder(self, folder_id: str | int) -> dict[str, Any]:
        """Get a folder by ID.

        Args:
            folder_id: The folder ID.

        Returns:
            The response from the /folder/{folder_id} endpoint.
        """
        response = self._client.get(f"{self.base_url}/folder/{folder_id}")
        response.raise_for_status()
        return response.json()

    def update_folder(self, folder_id: str | int, *, name: str) -> dict[str, Any]:
        """Update a folder.

        Args:
            folder_id: The folder ID to update.
            name: The new folder name.

        Returns:
            The response from the /folder/{folder_id} endpoint.
        """
        data: dict[str, Any] = {"name": name}

        response = self._client.put(f"{self.base_url}/folder/{folder_id}", json=data)
        response.raise_for_status()
        return response.json()

    def delete_folder(self, folder_id: str | int) -> dict[str, Any] | None:
        """Delete a folder.

        Args:
            folder_id: The folder ID to delete.

        Returns:
            None (204 No Content) or response dict.
        """
        return self._delete_with_204_handling(f"{self.base_url}/folder/{folder_id}")

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
            params["archived"] = self._to_bool_str(archived)

        response = self._client.get(
            f"{self.base_url}/folder/{folder_id}/list", params=params
        )
        response.raise_for_status()
        return response.json()

    def create_list(
        self,
        folder_id: str,
        *,
        name: str,
        content: str | None = None,
        markdown_content: str | None = None,
        due_date: int | None = None,
        due_date_time: bool | None = None,
        priority: int | None = None,
        assignee: int | None = None,
        status: str | None = None,
    ) -> dict[str, Any]:
        """Create a new list in a folder.

        Args:
            folder_id: The folder ID to create the list in.
            name: The list name (required).
            content: The list description (text content).
            markdown_content: The list description (markdown content).
            due_date: Due date as Unix timestamp in milliseconds.
            due_date_time: Whether the due date includes a time.
            priority: The list priority (0: Urgent, 1: High, 2: Normal, 3: Low, 4: None).
            assignee: Assignee user ID.
            status: The list status (color).

        Returns:
            The response from the /folder/{folder_id}/list endpoint.
        """
        data: dict[str, Any] = {"name": name}

        if content is not None:
            data["content"] = content
        if markdown_content is not None:
            data["markdown_content"] = markdown_content
        if due_date is not None:
            data["due_date"] = due_date
        if due_date_time is not None:
            data["due_date_time"] = due_date_time
        if priority is not None:
            data["priority"] = priority
        if assignee is not None:
            data["assignee"] = assignee
        if status is not None:
            data["status"] = status

        response = self._client.post(
            f"{self.base_url}/folder/{folder_id}/list", json=data
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
            params["reverse"] = self._to_bool_str(reverse)
        if subtasks is not None:
            params["subtasks"] = self._to_bool_str(subtasks)
        if include_markdown_description is not None:
            params["include_markdown_description"] = self._to_bool_str(
                include_markdown_description
            )
        if include_closed is not None:
            params["include_closed"] = self._to_bool_str(include_closed)

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
        return self._delete_with_204_handling(f"{self.base_url}/task/{task_id}")

    def get_task_comments(
        self,
        task_id: str,
        *,
        start: int | None = None,
        start_id: str | None = None,
    ) -> dict[str, Any]:
        """Get comments from a task.

        Args:
            task_id: The task ID.
            start: The Unix timestamp (in milliseconds) of the reference comment for pagination.
            start_id: The unique ID of the reference comment for pagination.

        Returns:
            The response from the /task/{task_id}/comment endpoint.
        """
        params: dict[str, Any] = {}

        if start is not None:
            params["start"] = start
        if start_id is not None:
            params["start_id"] = start_id

        response = self._client.get(
            f"{self.base_url}/task/{task_id}/comment", params=params
        )
        response.raise_for_status()
        return response.json()

    def create_task_comment(
        self,
        task_id: str,
        comment_text: str,
        *,
        assignee: int | None = None,
        notify_all: bool = True,
    ) -> dict[str, Any]:
        """Create a comment on a task.

        Args:
            task_id: The task ID.
            comment_text: The comment text (required).
            assignee: Assignee user ID to assign the comment to.
            notify_all: Whether to notify everyone including the creator.

        Returns:
            The response from the /task/{task_id}/comment endpoint.
        """
        data: dict[str, Any] = {
            "comment_text": comment_text,
            "notify_all": notify_all,
        }

        if assignee is not None:
            data["assignee"] = assignee

        response = self._client.post(
            f"{self.base_url}/task/{task_id}/comment", json=data
        )
        response.raise_for_status()
        return response.json()

    def get_list_comments(
        self,
        list_id: str | int,
        *,
        start: int | None = None,
        start_id: str | None = None,
    ) -> dict[str, Any]:
        """Get comments from a list.

        Args:
            list_id: The list ID.
            start: The Unix timestamp (in milliseconds) of the reference comment for pagination.
            start_id: The unique ID of the reference comment for pagination.

        Returns:
            The response from the /list/{list_id}/comment endpoint.
        """
        params: dict[str, Any] = {}

        if start is not None:
            params["start"] = start
        if start_id is not None:
            params["start_id"] = start_id

        response = self._client.get(
            f"{self.base_url}/list/{list_id}/comment", params=params
        )
        response.raise_for_status()
        return response.json()

    def create_list_comment(
        self,
        list_id: str | int,
        comment_text: str,
        *,
        assignee: int | None = None,
        notify_all: bool = True,
    ) -> dict[str, Any]:
        """Create a comment on a list.

        Args:
            list_id: The list ID.
            comment_text: The comment text (required).
            assignee: Assignee user ID to assign the comment to.
            notify_all: Whether to notify everyone including the creator.

        Returns:
            The response from the /list/{list_id}/comment endpoint.
        """
        data: dict[str, Any] = {
            "comment_text": comment_text,
            "assignee": assignee,
            "notify_all": notify_all,
        }

        response = self._client.post(
            f"{self.base_url}/list/{list_id}/comment", json=data
        )
        response.raise_for_status()
        return response.json()

    def create_checklist(self, task_id: str, *, name: str) -> dict[str, Any]:
        """Create a new checklist on a task.

        Args:
            task_id: The task ID to create the checklist on.
            name: The checklist name.

        Returns:
            The response from the /task/{task_id}/checklist endpoint.
        """
        data: dict[str, Any] = {"name": name}

        response = self._client.post(
            f"{self.base_url}/task/{task_id}/checklist", json=data
        )
        response.raise_for_status()
        return response.json()

    def create_checklist_item(
        self,
        checklist_id: str,
        *,
        name: str,
        assignee: int | None = None,
    ) -> dict[str, Any]:
        """Create a new item in a checklist.

        Args:
            checklist_id: The checklist ID to add the item to.
            name: The checklist item name.
            assignee: Assignee user ID.

        Returns:
            The response from the /checklist/{checklist_id}/checklist_item endpoint.
        """
        data: dict[str, Any] = {"name": name}

        if assignee is not None:
            data["assignee"] = assignee

        response = self._client.post(
            f"{self.base_url}/checklist/{checklist_id}/checklist_item", json=data
        )
        response.raise_for_status()
        return response.json()

    def update_checklist(
        self,
        checklist_id: str,
        *,
        name: str | None = None,
        position: int | None = None,
    ) -> dict[str, Any]:
        """Update a checklist.

        Args:
            checklist_id: The checklist ID to update.
            name: The new checklist name.
            position: The position (order) of the checklist.

        Returns:
            The response from the /checklist/{checklist_id} endpoint.
        """
        data: dict[str, Any] = {}

        if name is not None:
            data["name"] = name
        if position is not None:
            data["position"] = position

        if data:
            response = self._client.put(
                f"{self.base_url}/checklist/{checklist_id}", json=data
            )
            response.raise_for_status()
            return response.json()

        return {}

    def update_checklist_item(
        self,
        checklist_id: str,
        checklist_item_id: str,
        *,
        name: str | None = None,
        assignee: int | None = None,
        resolved: bool | None = None,
        parent: str | None = None,
    ) -> dict[str, Any]:
        """Update a checklist item.

        Args:
            checklist_id: The checklist ID.
            checklist_item_id: The checklist item ID to update.
            name: The new checklist item name.
            assignee: Assignee user ID.
            resolved: Whether the item is resolved (completed).
            parent: Parent checklist item ID (for nesting).

        Returns:
            The response from the /checklist/{checklist_id}/checklist_item/{checklist_item_id} endpoint.
        """
        data: dict[str, Any] = {}

        if name is not None:
            data["name"] = name
        if assignee is not None:
            data["assignee"] = assignee
        if resolved is not None:
            data["resolved"] = resolved
        if parent is not None:
            data["parent"] = parent

        if data:
            response = self._client.put(
                f"{self.base_url}/checklist/{checklist_id}/checklist_item/{checklist_item_id}",
                json=data,
            )
            response.raise_for_status()
            return response.json()

        return {}

    def delete_checklist(self, checklist_id: str) -> dict[str, Any]:
        """Delete a checklist.

        Args:
            checklist_id: The checklist ID to delete.

        Returns:
            The response from the /checklist/{checklist_id} endpoint.
        """
        response = self._client.delete(f"{self.base_url}/checklist/{checklist_id}")
        response.raise_for_status()
        return response.json()

    def delete_checklist_item(
        self, checklist_id: str, checklist_item_id: str
    ) -> dict[str, Any]:
        """Delete a checklist item.

        Args:
            checklist_id: The checklist ID.
            checklist_item_id: The checklist item ID to delete.

        Returns:
            The response from the /checklist/{checklist_id}/checklist_item/{checklist_item_id} endpoint.
        """
        response = self._client.delete(
            f"{self.base_url}/checklist/{checklist_id}/checklist_item/{checklist_item_id}"
        )
        response.raise_for_status()
        return response.json()

    def get_task_members(self, task_id: str) -> dict[str, Any]:
        """Get members with explicit access to a task.

        Args:
            task_id: The task ID.

        Returns:
            The response from the /task/{task_id}/member endpoint.
        """
        response = self._client.get(f"{self.base_url}/task/{task_id}/member")
        response.raise_for_status()
        return response.json()

    def get_list_members(self, list_id: str | int) -> dict[str, Any]:
        """Get members with explicit access to a list.

        Args:
            list_id: The list ID (string or integer).

        Returns:
            The response from the /list/{list_id}/member endpoint.
        """
        response = self._client.get(f"{self.base_url}/list/{list_id}/member")
        response.raise_for_status()
        return response.json()

    def get_space_tags(self, space_id: str | int) -> dict[str, Any]:
        """Get tags in a space.

        Args:
            space_id: The space ID.

        Returns:
            The response from the /space/{space_id}/tag endpoint.
        """
        response = self._client.get(f"{self.base_url}/space/{space_id}/tag")
        response.raise_for_status()
        return response.json()

    def create_space_tag(
        self, space_id: str | int, *, name: str, tag_fg: str, tag_bg: str
    ) -> dict[str, Any]:
        """Create a new tag in a space.

        Args:
            space_id: The space ID to create the tag in.
            name: The tag name.
            tag_fg: The tag foreground color (hex color).
            tag_bg: The tag background color (hex color).

        Returns:
            The response from the /space/{space_id}/tag endpoint.
        """
        data: dict[str, Any] = {
            "tag": {
                "name": name,
                "tag_fg": tag_fg,
                "tag_bg": tag_bg,
            }
        }

        response = self._client.post(f"{self.base_url}/space/{space_id}/tag", json=data)
        response.raise_for_status()
        return response.json()

    def add_tag_to_task(
        self, task_id: str, tag_name: str, *, custom_task_ids: bool = False
    ) -> dict[str, Any]:
        """Add a tag to a task.

        Args:
            task_id: The task ID.
            tag_name: The tag name to add.
            custom_task_ids: Whether to use custom task IDs.

        Returns:
            The response from the /task/{task_id}/tag/{tag_name} endpoint.
        """
        params: dict[str, Any] = {}
        if custom_task_ids:
            params["custom_task_ids"] = "true"

        response = self._client.post(
            f"{self.base_url}/task/{task_id}/tag/{tag_name}", params=params
        )
        response.raise_for_status()
        return response.json()

    def remove_tag_from_task(
        self, task_id: str, tag_name: str, *, custom_task_ids: bool = False
    ) -> dict[str, Any]:
        """Remove a tag from a task.

        Args:
            task_id: The task ID.
            tag_name: The tag name to remove.
            custom_task_ids: Whether to use custom task IDs.

        Returns:
            The response from the /task/{task_id}/tag/{tag_name} endpoint.
        """
        params: dict[str, Any] = {}
        if custom_task_ids:
            params["custom_task_ids"] = "true"

        response = self._client.delete(
            f"{self.base_url}/task/{task_id}/tag/{tag_name}", params=params
        )
        response.raise_for_status()
        return response.json()

    def get_running_time_entry(self, team_id: str | int) -> dict[str, Any]:
        """Get the currently running time entry.

        Args:
            team_id: The team/workspace ID.

        Returns:
            The response from the /team/{team_id}/time_entries/current endpoint.
        """
        response = self._client.get(
            f"{self.base_url}/team/{team_id}/time_entries/current"
        )
        response.raise_for_status()
        return response.json()

    def start_time_entry(
        self,
        team_id: str | int,
        *,
        task_id: str | None = None,
        description: str | None = None,
        billable: bool = False,
        tags: list[dict[str, str]] | None = None,
    ) -> dict[str, Any]:
        """Start a time entry.

        Args:
            team_id: The team/workspace ID.
            task_id: The task ID to associate with the time entry.
            description: The time entry description.
            billable: Whether the time entry is billable.
            tags: List of tags (name, tag_fg, tag_bg).

        Returns:
            The response from the /team/{team_id}/time_entries/start endpoint.
        """
        data: dict[str, Any] = {
            "billable": billable,
        }

        if task_id is not None:
            data["tid"] = task_id
        if description is not None:
            data["description"] = description
        if tags is not None:
            data["tags"] = tags

        response = self._client.post(
            f"{self.base_url}/team/{team_id}/time_entries/start", json=data
        )
        response.raise_for_status()
        return response.json()

    def stop_time_entry(self, team_id: str | int) -> dict[str, Any]:
        """Stop the currently running time entry.

        Args:
            team_id: The team/workspace ID.

        Returns:
            The response from the /team/{team_id}/time_entries/stop endpoint.
        """
        response = self._client.post(
            f"{self.base_url}/team/{team_id}/time_entries/stop"
        )
        response.raise_for_status()
        return response.json()

    def get_time_entries(
        self,
        team_id: str | int,
        *,
        start_date: int | None = None,
        end_date: int | None = None,
        assignee: int | None = None,
        space_id: int | None = None,
        folder_id: int | None = None,
        list_id: int | None = None,
        task_id: str | None = None,
        is_billable: bool | None = None,
        include_task_tags: bool = False,
        include_location_names: bool = False,
        include_approval_history: bool = False,
        include_approval_details: bool = False,
    ) -> dict[str, Any]:
        """Get time entries within a date range.

        Args:
            team_id: The team/workspace ID.
            start_date: Start date as Unix timestamp in milliseconds.
            end_date: End date as Unix timestamp in milliseconds.
            assignee: Filter by assignee user ID.
            space_id: Filter by space ID.
            folder_id: Filter by folder ID.
            list_id: Filter by list ID.
            task_id: Filter by task ID.
            is_billable: Filter by billable status.
            include_task_tags: Include task tags in response.
            include_location_names: Include space/folder/list names.
            include_approval_history: Include approval history.
            include_approval_details: Include approval details.

        Returns:
            The response from the /team/{team_id}/time_entries endpoint.
        """
        params: dict[str, Any] = {}

        if start_date is not None:
            params["start_date"] = start_date
        if end_date is not None:
            params["end_date"] = end_date
        if assignee is not None:
            params["assignee"] = assignee
        if space_id is not None:
            params["space_id"] = space_id
        if folder_id is not None:
            params["folder_id"] = folder_id
        if list_id is not None:
            params["list_id"] = list_id
        if task_id is not None:
            params["task_id"] = task_id
        if is_billable is not None:
            params["is_billable"] = "true" if is_billable else "false"
        if include_task_tags:
            params["include_task_tags"] = "true"
        if include_location_names:
            params["include_location_names"] = "true"
        if include_approval_history:
            params["include_approval_history"] = "true"
        if include_approval_details:
            params["include_approval_details"] = "true"

        response = self._client.get(
            f"{self.base_url}/team/{team_id}/time_entries", params=params
        )
        response.raise_for_status()
        return response.json()

    def create_time_entry(
        self,
        team_id: str | int,
        *,
        start: int,
        duration: int,
        task_id: str | None = None,
        description: str | None = None,
        billable: bool = False,
        tags: list[dict[str, str]] | None = None,
    ) -> dict[str, Any]:
        """Create a manual time entry.

        Args:
            team_id: The team/workspace ID.
            start: Start time as Unix timestamp in milliseconds.
            duration: Duration in milliseconds.
            task_id: The task ID to associate with the time entry.
            description: The time entry description.
            billable: Whether the time entry is billable.
            tags: List of tags (name, tag_fg, tag_bg).

        Returns:
            The response from the /team/{team_id}/time_entries endpoint.
        """
        data: dict[str, Any] = {
            "start": start,
            "duration": duration,
            "billable": billable,
        }

        if task_id is not None:
            data["tid"] = task_id
        if description is not None:
            data["description"] = description
        if tags is not None:
            data["tags"] = tags

        response = self._client.post(
            f"{self.base_url}/team/{team_id}/time_entries", json=data
        )
        response.raise_for_status()
        return response.json()

    def update_time_entry(
        self,
        team_id: str | int,
        timer_id: str | int,
        *,
        description: str | None = None,
        start: int | None = None,
        end: int | None = None,
        duration: int | None = None,
        task_id: str | None = None,
        billable: bool | None = None,
        tags: list[dict[str, str]] | None = None,
        tag_action: str | None = None,
    ) -> dict[str, Any]:
        """Update a time entry.

        Args:
            team_id: The team/workspace ID.
            timer_id: The time entry ID.
            description: The time entry description.
            start: Start time as Unix timestamp in milliseconds.
            end: End time as Unix timestamp in milliseconds.
            duration: Duration in milliseconds.
            task_id: The task ID to associate with the time entry.
            billable: Whether the time entry is billable.
            tags: List of tags (name, tag_fg, tag_bg).
            tag_action: Tag action - one of "replace", "add", "remove".

        Returns:
            The response from the /team/{team_id}/time_entries/{timer_id} endpoint.
        """
        data: dict[str, Any] = {
            "tags": tags if tags is not None else [],
            "tid": task_id if task_id is not None else "",
        }

        if description is not None:
            data["description"] = description
        if start is not None:
            data["start"] = start
        if end is not None:
            data["end"] = end
        if duration is not None:
            data["duration"] = duration
        if billable is not None:
            data["billable"] = billable
        if tag_action is not None:
            data["tag_action"] = tag_action

        response = self._client.put(
            f"{self.base_url}/team/{team_id}/time_entries/{timer_id}", json=data
        )
        response.raise_for_status()
        return response.json()

    def delete_time_entry(
        self, team_id: str | int, timer_id: str | int
    ) -> dict[str, Any]:
        """Delete a time entry.

        Args:
            team_id: The team/workspace ID.
            timer_id: The time entry ID to delete.

        Returns:
            The response from the /team/{team_id}/time_entries/{timer_id} endpoint.
        """
        response = self._client.delete(
            f"{self.base_url}/team/{team_id}/time_entries/{timer_id}"
        )
        response.raise_for_status()
        return response.json()

    def get_goals(
        self, team_id: str | int, *, include_completed: bool | None = None
    ) -> dict[str, Any]:
        """Get goals in a workspace.

        Args:
            team_id: The team/workspace ID.
            include_completed: Include completed goals.

        Returns:
            The response from the /team/{team_id}/goal endpoint.
        """
        params: dict[str, Any] = {}
        if include_completed is not None:
            params["include_completed"] = self._to_bool_str(include_completed)

        response = self._client.get(
            f"{self.base_url}/team/{team_id}/goal", params=params
        )
        response.raise_for_status()
        return response.json()

    def get_goal(self, goal_id: str) -> dict[str, Any]:
        """Get a goal by ID.

        Args:
            goal_id: The goal ID.

        Returns:
            The response from the /goal/{goal_id} endpoint.
        """
        response = self._client.get(f"{self.base_url}/goal/{goal_id}")
        response.raise_for_status()
        return response.json()

    def create_goal(
        self,
        team_id: str | int,
        *,
        name: str,
        due_date: int,
        description: str = "",
        multiple_owners: bool = False,
        owners: list[int] | None = None,
        color: str = "#32a852",
        start_date: int | None = None,
    ) -> dict[str, Any]:
        """Create a new goal in a workspace.

        Args:
            team_id: The team/workspace ID.
            name: The goal name (required).
            due_date: Due date as Unix timestamp in milliseconds (required).
            description: The goal description.
            multiple_owners: Whether the goal has multiple owners.
            owners: Array of owner user IDs.
            color: The goal color (hex).
            start_date: Start date as Unix timestamp in milliseconds.

        Returns:
            The response from the /team/{team_id}/goal endpoint.
        """
        data: dict[str, Any] = {
            "name": name,
            "due_date": due_date,
            "description": description,
            "multiple_owners": multiple_owners,
            "owners": owners if owners is not None else [],
            "color": color,
        }

        if start_date is not None:
            data["start_date"] = start_date

        response = self._client.post(f"{self.base_url}/team/{team_id}/goal", json=data)
        response.raise_for_status()
        return response.json()

    def update_goal(
        self,
        goal_id: str,
        *,
        name: str | None = None,
        due_date: int | None = None,
        description: str | None = None,
        rem_owners: list[int] | None = None,
        add_owners: list[int] | None = None,
        color: str | None = None,
    ) -> dict[str, Any]:
        """Update a goal.

        Args:
            goal_id: The goal ID to update.
            name: The new goal name.
            due_date: New due date as Unix timestamp in milliseconds.
            description: New goal description.
            rem_owners: Owner user IDs to remove.
            add_owners: Owner user IDs to add.
            color: New goal color (hex).

        Returns:
            The response from the /goal/{goal_id} endpoint.
        """
        data: dict[str, Any] = {
            "name": name if name is not None else "",
            "due_date": due_date if due_date is not None else 0,
            "description": description if description is not None else "",
            "rem_owners": rem_owners if rem_owners is not None else [],
            "add_owners": add_owners if add_owners is not None else [],
            "color": color if color is not None else "",
        }

        response = self._client.put(f"{self.base_url}/goal/{goal_id}", json=data)
        response.raise_for_status()
        return response.json()

    def delete_goal(self, goal_id: str) -> dict[str, Any]:
        """Delete a goal.

        Args:
            goal_id: The goal ID to delete.

        Returns:
            The response from the /goal/{goal_id} endpoint.
        """
        response = self._client.delete(
            f"{self.base_url}/goal/{goal_id}",
            headers={"Content-Type": "application/json"},
        )
        response.raise_for_status()
        return response.json()

    def create_key_result(
        self,
        goal_id: str,
        *,
        name: str,
        owners: list[int],
        type: str = "number",
        steps_start: int = 0,
        steps_end: int = 100,
        unit: str = "",
        task_ids: list[str] | None = None,
        list_ids: list[str] | None = None,
    ) -> dict[str, Any]:
        """Create a key result for a goal.

        Args:
            goal_id: The goal ID.
            name: The key result name (required).
            owners: Array of owner user IDs (required).
            type: The key result type (number, currency, boolean, percentage, automatic).
            steps_start: Starting value.
            steps_end: Ending value.
            unit: Unit of measurement.
            task_ids: Array of task IDs to link.
            list_ids: Array of list IDs to link.

        Returns:
            The response from the /goal/{goal_id}/key_result endpoint.
        """
        data: dict[str, Any] = {
            "name": name,
            "owners": owners,
            "type": type,
            "steps_start": steps_start,
            "steps_end": steps_end,
            "unit": unit,
            "task_ids": task_ids if task_ids is not None else [],
            "list_ids": list_ids if list_ids is not None else [],
        }

        response = self._client.post(
            f"{self.base_url}/goal/{goal_id}/key_result", json=data
        )
        response.raise_for_status()
        return response.json()

    def update_key_result(
        self,
        key_result_id: str,
        *,
        steps_current: int | None = None,
        note: str = "",
    ) -> dict[str, Any]:
        """Update a key result.

        Args:
            key_result_id: The key result ID.
            steps_current: Current progress value.
            note: Update note.

        Returns:
            The response from the /key_result/{key_result_id} endpoint.
        """
        data: dict[str, Any] = {
            "steps_current": steps_current if steps_current is not None else 0,
            "note": note,
        }

        response = self._client.put(
            f"{self.base_url}/key_result/{key_result_id}", json=data
        )
        response.raise_for_status()
        return response.json()

    def delete_key_result(self, key_result_id: str) -> dict[str, Any]:
        """Delete a key result.

        Args:
            key_result_id: The key result ID to delete.

        Returns:
            The response from the /key_result/{key_result_id} endpoint.
        """
        response = self._client.delete(f"{self.base_url}/key_result/{key_result_id}")
        response.raise_for_status()
        return response.json()

    def add_dependency(
        self,
        task_id: str,
        *,
        depends_on: str | None = None,
        dependency_of: str | None = None,
        custom_task_ids: bool = False,
        team_id: str | int | None = None,
    ) -> dict[str, Any]:
        """Add a dependency between tasks.

        Args:
            task_id: The task ID that is waiting on or blocking another task.
            depends_on: The task ID that must be completed before task_id can start.
            dependency_of: The task ID that is waiting for task_id to be completed.
            custom_task_ids: Whether to use custom task IDs.
            team_id: The workspace ID (required when using custom_task_ids).

        Returns:
            The response from the /task/{task_id}/dependency endpoint.
        """
        if depends_on is None and dependency_of is None:
            raise ValueError("Either depends_on or dependency_of must be provided.")

        data: dict[str, Any] = {}
        if depends_on is not None:
            data["depends_on"] = depends_on
        if dependency_of is not None:
            data["depedency_of"] = dependency_of

        params: dict[str, Any] = {}
        if custom_task_ids:
            params["custom_task_ids"] = "true"
        if team_id is not None:
            params["team_id"] = team_id

        response = self._client.post(
            f"{self.base_url}/task/{task_id}/dependency", params=params, json=data
        )
        response.raise_for_status()
        return response.json()

    def delete_dependency(
        self,
        task_id: str,
        *,
        depends_on: str | None = None,
        dependency_of: str | None = None,
        custom_task_ids: bool = False,
        team_id: str | int | None = None,
    ) -> dict[str, Any]:
        """Delete a dependency between tasks.

        Args:
            task_id: The task ID.
            depends_on: The task ID to remove from depends_on relationship.
            dependency_of: The task ID to remove from dependency_of relationship.
            custom_task_ids: Whether to use custom task IDs.
            team_id: The workspace ID (required when using custom_task_ids).

        Returns:
            The response from the /task/{task_id}/dependency endpoint.
        """
        if depends_on is None and dependency_of is None:
            raise ValueError("Either depends_on or dependency_of must be provided.")

        params: dict[str, Any] = {}
        if depends_on is not None:
            params["depends_on"] = depends_on
        if dependency_of is not None:
            params["dependency_of"] = dependency_of
        if custom_task_ids:
            params["custom_task_ids"] = "true"
        if team_id is not None:
            params["team_id"] = team_id

        response = self._client.delete(
            f"{self.base_url}/task/{task_id}/dependency", params=params
        )
        response.raise_for_status()
        return response.json()

    def add_task_link(
        self,
        task_id: str,
        *,
        links_to: str | None = None,
        custom_task_ids: bool = False,
        team_id: str | int | None = None,
    ) -> dict[str, Any]:
        """Add a link between two tasks.

        Args:
            task_id: The task to initiate the link from.
            links_to: The task to link to.
            custom_task_ids: Whether to use custom task IDs.
            team_id: The workspace ID (required when using custom_task_ids).

        Returns:
            The response from the /task/{task_id}/link/{links_to} endpoint.
        """
        if links_to is None:
            raise ValueError("links_to must be provided.")

        params: dict[str, Any] = {}
        if custom_task_ids:
            params["custom_task_ids"] = "true"
        if team_id is not None:
            params["team_id"] = team_id

        response = self._client.post(
            f"{self.base_url}/task/{task_id}/link/{links_to}", params=params
        )
        response.raise_for_status()
        return response.json()

    def delete_task_link(
        self,
        task_id: str,
        *,
        links_to: str | None = None,
        custom_task_ids: bool = False,
        team_id: str | int | None = None,
    ) -> dict[str, Any]:
        """Delete a link between two tasks.

        Args:
            task_id: The task to remove the link from.
            links_to: The linked task ID to remove.
            custom_task_ids: Whether to use custom task IDs.
            team_id: The workspace ID (required when using custom_task_ids).

        Returns:
            The response from the /task/{task_id}/link/{links_to} endpoint.
        """
        if links_to is None:
            raise ValueError("links_to must be provided.")

        params: dict[str, Any] = {}
        if custom_task_ids:
            params["custom_task_ids"] = "true"
        if team_id is not None:
            params["team_id"] = team_id

        response = self._client.delete(
            f"{self.base_url}/task/{task_id}/link/{links_to}", params=params
        )
        response.raise_for_status()
        return response.json()

    def create_task_attachment(
        self,
        task_id: str,
        *,
        attachment_path: str,
        custom_task_ids: bool = False,
        team_id: str | int | None = None,
    ) -> dict[str, Any]:
        """Upload a file as an attachment to a task.

        Args:
            task_id: The task ID to attach the file to.
            attachment_path: Path to the file to upload.
            custom_task_ids: Whether to use custom task IDs.
            team_id: The workspace ID (required when using custom_task_ids).

        Returns:
            The response from the /task/{task_id}/attachment endpoint.
        """
        params: dict[str, Any] = {}
        if custom_task_ids:
            params["custom_task_ids"] = "true"
        if team_id is not None:
            params["team_id"] = team_id

        # Open the file in binary mode
        with open(attachment_path, "rb") as f:
            files = {"attachment": (attachment_path, f, "application/octet-stream")}
            response = self._client.post(
                f"{self.base_url}/task/{task_id}/attachment",
                params=params,
                files=files,
            )
            response.raise_for_status()
            return response.json()

    def __enter__(self) -> "ClickUpClient":
        """Context manager entry."""
        return self

    def __exit__(self, *_: Any) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()
