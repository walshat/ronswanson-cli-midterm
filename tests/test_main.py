# tests/test_main.py
"""
Tests for the CLI logic in src/main.py.
We mock the API functions themselves, not the 'requests' library.
"""

import pytest
from unittest.mock import patch, MagicMock
import sys
from src import main

# --- Test 'quote' command ---
@patch("src.main.api.get_random_quote")
def test_main_quote(mock_get_random, capsys):
    """Tests the 'quote' command."""
    # Setup mock
    mock_get_random.return_value = ["This is a test quote."]
    
    # Simulate command-line arguments
    sys.argv = ["main.py", "quote"]
    
    # Run main
    main.main()
    
    # Check that our mock was called
    mock_get_random.assert_called_once()
    
    # Check the output
    captured = capsys.readouterr()
    assert "This is a test quote." in captured.out
    assert "1. " in captured.out

# --- Test 'multiple' command ---
@patch("src.main.api.get_multiple_quotes")
def test_main_multiple(mock_get_multiple, capsys):
    """Tests the 'multiple' command."""
    # Setup mock
    mock_get_multiple.return_value = ["Quote A", "Quote B"]
    
    # Simulate command-line arguments
    sys.argv = ["main.py", "multiple", "2"]
    
    # Run main
    main.main()
    
    # Check that our mock was called with the correct arg
    mock_get_multiple.assert_called_with(2)
    
    # Check the output
    captured = capsys.readouterr()
    assert "Quote A" in captured.out
    assert "Quote B" in captured.out
    assert "1. " in captured.out
    assert "2. " in captured.out

# --- Test 'search' command ---
@patch("src.main.api.search_quotes")
def test_main_search(mock_search, capsys):
    """Tests the 'search' command."""
    # Setup mock
    mock_search.return_value = ["Found a meat quote."]
    
    # Simulate command-line arguments
    sys.argv = ["main.py", "search", "meat"]
    
    # Run main
    main.main()
    
    # Check that our mock was called with the correct arg
    mock_search.assert_called_with("meat")
    
    # Check the output
    captured = capsys.readouterr()
    assert "Found a meat quote." in captured.out

# --- Test API failure ---
@patch("src.main.api.get_random_quote")
def test_main_api_failure(mock_get_random, capsys):
    """Tests that a failure message is printed if API returns None."""
    # Setup mock
    mock_get_random.return_value = None  # Simulate API error
    
    # Simulate command-line arguments
    sys.argv = ["main.py", "quote"]
    
    # Run main
    main.main()
    
    # Check the output
    captured = capsys.readouterr()
    assert "Failed to retrieve quotes." in captured.out