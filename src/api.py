import requests

BASE_URL = "https://officeapi.akashrajpurohit.com"

def get_random_quote():
    """Fetches a single random quote from any character.

    Returns
    -------
    dict
        A dictionary containing the 'quote' and 'character' if successful.
    str
        An error message if the request fails.
    """
    try:
        response = requests.get(f"{BASE_URL}/quotes/random")
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"

def get_characters():
    """Fetches a list of all available character names.

    Returns
    -------
    list
        A list of character name strings.
    str
        An error message if the request fails.
    """
    try:
        response = requests.get(f"{BASE_URL}/quotes/characters")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"

def get_character_quote(character_name):
    """Fetches a random quote from a specific character.

    Parameters
    ----------
    character_name : str
        The name of the character to get a quote from (e.g., "Michael").

    Returns
    -------
    dict
        A dictionary containing the 'quote' and 'character' if successful.
    str
        An error message if the request fails or the character is not found.
    """
    try:
        # The API uses lowercase names in the URL path
        formatted_name = character_name.lower()
        response = requests.get(f"{BASE_URL}/quotes/random/{formatted_name}")
        response.raise_for_status()
        
        data = response.json()
        
        # Handle API's specific error message for non-existent characters
        if data.get("error"):
            return f"Error: {data['error']}"
            
        return data
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"