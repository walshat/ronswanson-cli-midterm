# Ron Swanson Quotes CLI

[![Run Python Tests](https://github.com/walshat/ronswanson-cli-midterm/actions/workflows/tests.yml/badge.svg)](https://github.com/walshat/ronswanson-cli-midterm/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A simple Python command-line tool to fetch timeless wisdom from Ron Swanson.



## 📋 Features

* Get a random Ron Swanson quote.
* Get a specific number of random quotes.
* Search for quotes containing a specific word (e.g., "meat", "government").

## 🚀 Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/walshat/ronswanson-cli-midterm.git](https://github.com/walshat/ronswanson-cli-midterm.git)
    cd ronswanson-cli-midterm
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

The CLI is run using `python -m src.main` from the project's root directory.

### Get Help
To see all available commands and options:
```bash
python -m src.main --help
```

### Example 1: Get a single random quote
```bash
python -m src.main quote
```
**Output:**
```
1. "Never half-ass two things. Whole-ass one thing."
```

### Example 2: Get multiple quotes
```bash
python -m src.main multiple 3
```
**Output:**
```
1. "The government is a greedy piglet that suckles on a taxpayer's teat until they have sore, chapped nipples."

2. "There's only one thing I hate more than lying: skim milk. Which is water that's lying about being milk."

3. "Fishing relaxes me. It's like yoga, except I still get to kill something."
```

### Example 3: Search for a quote
```bash
python -m src.main search "meat"
```
**Output:**
```
1. "I call this turf ‘n’ turf. It’s a 16-ounce T-bone and a 24-ounce porterhouse. Also, whisky and a cigar. I am going to consume all of this at the same time because I am a free American."
```

## Testing

This project uses `pytest` and `unittest.mock` for testing. All API calls are mocked to ensure tests run quickly and reliably without network dependency.

To run the tests locally:
```bash
pytest
```

## API Information

This tool uses the free [Ron Swanson Quotes API](https://github.com/jamesseanwright/ron-swanson-quotes), which does not require an API key.

## Technologies Used

* Python 3.10
* `argparse`
* `requests`
* `pytest`
* GitHub Actions