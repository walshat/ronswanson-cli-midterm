import pytest
from unittest.mock import patch, MagicMock
from src import api
import requests

# Use a consistent mock response for successful quote fetches
MOCK_QUOTE_RESPONSE = {"quote": "That's what she said.", "character": "Michael"}
MOCK_CHAR_LIST = ["Michael", "Dwight", "Jim"]

@patch('src.api.requests.get')
def test_get_random_quote_success(mock_get):
    """Tests successful fetching of a random quote."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = MOCK_QUOTE_RESPONSE
    mock_get.return_value = mock_response

    result = api.get_random_quote()
    
    # Check that 'requests.get' was called correctly
    mock_get.assert_called_with(f"{api.BASE_URL}/quotes/random")
    # Check that the function returned the expected data
    assert result == MOCK_QUOTE_RESPONSE

@patch('src.api.requests.get')
def test_get_random_quote_failure(mock_get):
    """Tests handling of a network error."""
    # Simulate a requests exception
    mock_get.side_effect = requests.exceptions.RequestException("Network Error")

    result = api.get_random_quote()
    
    assert "Error fetching data: Network Error" in str(result)

@patch('src.api.requests.get')
def test_get_characters_success(mock_get):
    """Tests successful fetching of the character list."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = MOCK_CHAR_LIST
    mock_get.return_value = mock_response

    result = api.get_characters()
    
    mock_get.assert_called_with(f"{api.BASE_URL}/quotes/characters")
    assert result == MOCK_CHAR_LIST
    assert len(result) == 3

@patch('src.api.requests.get')
def test_get_character_quote_success(mock_get):
    """Tests successful fetching of a quote for a specific character."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = MOCK_QUOTE_RESPONSE
    mock_get.return_value = mock_response

    result = api.get_character_quote("Michael")
    
    # API formats the name to lowercase for the URL
    mock_get.assert_called_with(f"{api.BASE_URL}/quotes/random/michael")
    assert result == MOCK_QUOTE_RESPONSE

@patch('src.api.requests.get')
def test_get_character_quote_not_found(mock_get):
    """Tests API handling of a character not found."""
    mock_error = {"error": "Character not found."}
    mock_response = MagicMock()
    mock_response.status_code = 200  # The API might return 200 with an error object
    mock_response.json.return_value = mock_error
    mock_get.return_value = mock_response

    result = api.get_character_quote("NonExistent")
    
    assert "Error: Character not found." in result