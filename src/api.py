# src/api.py
"""
Handles all API calls to the Ron Swanson Quotes API.
"""

import requests

BASE_URL = "https://ron-swanson-quotes.herokuapp.com/v2/quotes"

def get_random_quote():
    """
    Fetches a single random quote from the API.

    Returns:
        list: A list containing a single quote string, or None if an error occurs.
    """
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def get_multiple_quotes(count=1):
    """
    Fetches a specified number of random quotes.

    Args:
        count (int): The number of quotes to fetch.

    Returns:
        list: A list of quote strings, or None if an error occurs.
    """
    try:
        # Ensure count is a positive integer
        count = max(1, int(count))
        url = f"{BASE_URL}/{count}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except ValueError:
        print("Error: Count must be an integer.")
        return None

def search_quotes(query):
    """
    Searches for quotes containing a specific term.

    Args:
        query (str): The search term.

    Returns:
        list: A list of matching quote strings, or None if an error occurs.
    """
    if not query or not isinstance(query, str):
        print("Error: Search query must be a non-empty string.")
        return None
        
    try:
        url = f"{BASE_URL}/search/{query}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error searching quotes: {e}")
        return None