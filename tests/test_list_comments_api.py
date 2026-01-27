"""Tests for list comments API."""

import pytest


@pytest.mark.vcr()
def test_get_list_comments(clickup_client):
    """Test getting comments from a list."""
    # Get comments from a list
    data = clickup_client.get_list_comments("901520401736")

    # Verify response structure
    assert "comments" in data
    assert isinstance(data["comments"], list)


@pytest.mark.vcr()
def test_create_list_comment(clickup_client):
    """Test creating a comment on a list."""
    # Create a comment on a list
    data = clickup_client.create_list_comment(
        "901520401736",
        comment_text="Test list comment",
        assignee=None,
        notify_all=True,
    )

    # Verify response structure
    assert "id" in data
    assert "date" in data
    assert isinstance(data["id"], (str, int))


@pytest.mark.vcr()
def test_create_list_comment_with_assignee(clickup_client):
    """Test creating a comment on a list with an assignee."""
    # Create a comment on a list with an assignee
    data = clickup_client.create_list_comment(
        "901520401736",
        comment_text="Test list comment with assignee",
        assignee=272627274,
        notify_all=False,
    )

    # Verify response structure
    assert "id" in data
    assert "date" in data
    assert isinstance(data["id"], (str, int))
