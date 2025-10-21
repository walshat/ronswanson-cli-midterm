import pytest
from unittest.mock import patch

# We need to test the *main* module, so we import it
from src import main

# Mock data to be returned by our API functions
MOCK_QUOTE = {"quote": "Bears. Beets. Battlestar Galactica.", "character": "Jim"}
MOCK_CHARS = ["Michael", "Dwight", "Jim"]

@patch('src.main.api.get_random_quote')
@patch('sys.argv', ['main.py', 'random'])
def test_main_random_command(mock_get_random, capsys):
    """Tests the 'random' command."""
    mock_get_random.return_value = MOCK_QUOTE
    
    main.main()
    
    # Check that our mock API function was called
    mock_get_random.assert_called_once()
    
    # Capture the output printed to stdout
    captured = capsys.readouterr()
    assert '"Bears. Beets. Battlestar Galactica." - Jim' in captured.out

@patch('src.main.api.get_characters')
@patch('sys.argv', ['main.py', 'characters'])
def test_main_characters_command(mock_get_chars, capsys):
    """Tests the 'characters' command."""
    mock_get_chars.return_value = MOCK_CHARS
    
    main.main()
    
    mock_get_chars.assert_called_once()
    
    captured = capsys.readouterr()
    assert "Available characters:" in captured.out
    assert "- Michael" in captured.out
    assert "- Dwight" in captured.out

@patch('src.main.api.get_character_quote')
@patch('sys.argv', ['main.py', 'quote', 'Dwight'])
def test_main_quote_command(mock_get_char_quote, capsys):
    """Tests the 'quote [character]' command."""
    mock_get_char_quote.return_value = MOCK_QUOTE
    
    main.main()
    
    # Check that the API function was called with the correct argument
    mock_get_char_quote.assert_called_with("Dwight")
    
    captured = capsys.readouterr()
    assert '"Bears. Beets. Battlestar Galactica." - Jim' in captured.out
    
@patch('src.main.api.get_random_quote')
@patch('sys.argv', ['main.py', 'random'])
def test_main_random_api_error(mock_get_random, capsys):
    """Tests the 'random' command when the API returns an error."""
    mock_get_random.return_value = "Error: API is down."
    
    main.main()
    
    captured = capsys.readouterr()
    assert "Error: API is down." in captured.out