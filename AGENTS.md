# Project Name: Ron Swanson Quotes CLI

## Overview
A Python-based command-line tool to fetch and display quotes from Ron Swanson (Parks and Recreation). This project fulfills the requirements of the App Dev w/ AI Midterm.

## API Integration
- **API:** Ron Swanson Quotes API
- **Base URL:** https://ron-swanson-quotes.herokuapp.com/v2/quotes
- **Key endpoints:**
  - `/quotes`: Get one random quote.
  - `/quotes/[count]`: Get a specific number of quotes.
  - `/quotes/search/[query]`: Search for quotes containing a specific word.
- **Data format:** JSON (an array of strings)

## CLI Commands
The CLI is built using `argparse` and supports the following subcommands:
- `quote`: Get a single random quote.
- `multiple <count>`: Get a specific number of random quotes (e.g., `multiple 5`).
- `search <query>`: Search for quotes containing a query (e.g., `search meat`).

## Technical Stack
- Python 3.10+
- `argparse` for CLI argument parsing
- `requests` library for API calls
- `pytest` for testing
- `unittest.mock` for mocking API calls in tests
- `GitHub Actions` for CI/CD

## Code Organization
- `src/main.py`: Entry point and `argparse` CLI setup.
- `src/api.py`: All functions that interact with the Ron Swanson API.
- `tests/test_main.py`: Pytest tests for the CLI (`main.py`).
- `tests/test_api.py`: Pytest tests for the API functions (`api.py`), using mocks.
- `.github/workflows/tests.yml`: GitHub Actions workflow for CI.

## Standards
- All functions and classes must have docstrings.
- Code follows PEP 8 style guidelines.
- All API calls are mocked in the test suite.
- Handle API errors and bad HTTP responses gracefully.