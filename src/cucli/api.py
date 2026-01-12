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

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def __enter__(self) -> "ClickUpClient":
        """Context manager entry."""
        return self

    def __exit__(self, *_: Any) -> None:
        """Context manager exit."""
        self.close()
