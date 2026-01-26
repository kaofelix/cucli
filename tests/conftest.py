"""Shared pytest fixtures and configuration."""

import os

import pytest
from click.testing import CliRunner
from cucli.api import ClickUpClient


@pytest.fixture
def api_key():
    """Provide a test API key (actual value not used with VCR recordings)."""
    # Use real API key from environment when recording
    real_key = os.environ.get("CLICKUP_API_KEY")
    if real_key:
        return real_key
    return "pk_test_api_key_12345"


@pytest.fixture
def clickup_client(api_key):
    """Provide a ClickUpClient instance with a test API key."""
    # Set the API key for the client
    client = ClickUpClient(api_key=api_key)
    yield client
    client.close()


@pytest.fixture
def mock_api_key_env(api_key, monkeypatch):
    """Set the CLICKUP_API_KEY environment variable for testing."""
    # When recording, use the real API key from environment if available
    real_key = os.environ.get("CLICKUP_API_KEY")
    if real_key:
        monkeypatch.setenv("CLICKUP_API_KEY", real_key)
        return real_key
    # Otherwise use the mock key (for playback)
    monkeypatch.setenv("CLICKUP_API_KEY", api_key)
    return api_key


@pytest.fixture
def runner():
    """Provide a Click CliRunner for testing CLI commands."""
    return CliRunner()
