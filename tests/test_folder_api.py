"""Tests for folder API methods."""

import pytest
from cucli.models import Folder


class TestFolderAPI:
    """Test cases for folder API methods."""

    @pytest.mark.vcr
    def test_get_folder(self, clickup_client):
        """Test getting a specific folder from API."""
        # Using a real folder ID from test workspace
        folder_id = "901513787576"

        response = clickup_client.get_folder(folder_id)

        # Verify response structure
        assert "id" in response
        assert "name" in response

        # Parse with Pydantic model
        folder = Folder(**response)
        assert folder.id == folder_id
        assert folder.name is not None

    @pytest.mark.vcr
    def test_update_folder(self, clickup_client):
        """Test updating a folder name."""
        folder_id = "901513787576"
        new_name = "Updated Folder Name"

        response = clickup_client.update_folder(folder_id, name=new_name)

        # Verify response structure
        assert "id" in response
        assert "name" in response

        # Parse with Pydantic model
        folder = Folder(**response)
        assert folder.name == new_name

    @pytest.mark.vcr
    def test_delete_folder(self, clickup_client):
        """Test deleting a folder."""
        # For delete, we need to use a test folder that can be deleted
        # First create one, then delete it
        folder_id = "901513799683"

        response = clickup_client.delete_folder(folder_id)

        # Delete returns empty dict or None
        assert response is None or response == {}

    def test_get_folder_missing_id(self, clickup_client):
        """Test get_folder fails gracefully with missing ID."""
        with pytest.raises(Exception):
            clickup_client.get_folder("")
