# "Office" - The Office Quotes CLI

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Tests](https://github.com/[walshat/is4010-walshat-labs]/actions/workflows/tests.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A simple Python command-line tool to fetch quotes and character information from "The Office API."

## Features
* Get a random quote from any character.
* List all available characters from the API.
* Get a random quote from a specific character.

## API Information
This project uses the free, open-source [The Office API](https://akashrajpurohit.github.io/the-office-api/) created by Akash Rajpurohit. It requires no authentication.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[walshat/is4010-walshat-labs].git
    cd is4010-walshat-labs
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can run the CLI using `python -m src.main`.

### View Help
To see all available commands and options:
```bash
python -m src.main --help
```

### Example Commands

**1. Get a random quote:**
```bash
$ python -m src.main random
"I'm not superstitious, but I am a little stitious." - Michael
```

**2. List all available characters:**
```bash
$ python -m src.main characters
Available characters:
- Andy
- Angela
- Creed
- Dwight
- Jim
- Kevin
...
```

**3. Get a random quote from a specific character:**
```bash
$ python -m src.main quote Dwight
"Identity theft is not a joke, Jim! Millions of families suffer every year!" - Dwight
```

**4. Handle invalid character:**
```bash
$ python -m src.main quote Homer
Error: Character not found.
```

## Testing
This project uses `pytest` for automated testing, including mocking all external API calls.

To run the tests locally:
1.  Make sure you have installed the dependencies (including `pytest`).
2.  Run `pytest` from the root of the project:

```bash
pytest
```