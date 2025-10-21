# tests/test_api.py
"""
Tests for the src/api.py functions, using mocking.
"""

import pytest
from unittest.mock import patch, MagicMock
from src import api
import requests

# Set the path for mocking requests.get
# It must be the path *where it is used* (i.e., in src.api)
PATCH_PATH = "src.api.requests.get"

@patch(PATCH_PATH)
def test_get_random_quote_success(mock_get):
    """Tests successful call to get_random_quote."""
    mock_response = MagicMock()
    mock_response.json.return_value = ["I am Ron Swanson."]
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    result = api.get_random_quote()

    # Check that requests.get was called correctly
    mock_get.assert_called_with(api.BASE_URL)
    # Check that the function returned the expected JSON
    assert result == ["I am Ron Swanson."]

@patch(PATCH_PATH)
def test_get_random_quote_failure(mock_get):
    """Tests a failed API call (e.g., network error)."""
    # Configure the mock to raise a RequestException
    mock_get.side_effect = requests.RequestException("Network Error")

    result = api.get_random_quote()
    
    # Check that requests.get was called
    mock_get.assert_called_with(api.BASE_URL)
    # Check that the function returned None on failure
    assert result is None

@patch(PATCH_PATH)
def test_get_multiple_quotes_success(mock_get):
    """Tests successful call to get_multiple_quotes."""
    mock_response = MagicMock()
    mock_response.json.return_value = ["Quote 1.", "Quote 2.", "Quote 3."]
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    result = api.get_multiple_quotes(3)
    
    # Check that requests.get was called with the correct URL
    mock_get.assert_called_with(f"{api.BASE_URL}/3")
    # Check the result
    assert result == ["Quote 1.", "Quote 2.", "Quote 3."]

@patch(PATCH_PATH)
def test_search_quotes_success(mock_get):
    """Tests successful call to search_quotes."""
    mock_response = MagicMock()
    mock_response.json.return_value = ["This is about meat."]
    mock_response.status_code = 200
    mock_get.return_value = mock_response
    
    query = "meat"
    result = api.search_quotes(query)

    # Check that requests.get was called with the correct search URL
    mock_get.assert_called_with(f"{api.BASE_URL}/search/{query}")
    # Check the result
    assert result == ["This is about meat."]

@patch(PATCH_PATH)
def test_search_quotes_no_results(mock_get):
    """Tests a successful search that returns no quotes."""
    mock_response = MagicMock()
    mock_response.json.return_value = []  # API returns empty list for no match
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    result = api.search_quotes("nonexistent")
    
    mock_get.assert_called_with(f"{api.BASE_URL}/search/nonexistent")
    assert result == []

def test_search_quotes_invalid_query():
    """Tests search_quotes with an invalid query (e.g., None or empty string)."""
    result_none = api.search_quotes(None)
    assert result_none is None
    
    result_empty = api.search_quotes("")
    assert result_empty is None