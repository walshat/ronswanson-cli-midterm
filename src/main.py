# src/main.py
"""
Main entry point for the Ron Swanson Quotes CLI.
Uses argparse to define commands and calls API functions.
"""

import argparse
from src import api

def main():
    """Main function to parse arguments and execute commands."""
    parser = argparse.ArgumentParser(
        description="Fetch quotes from the Ron Swanson API."
    )
    # Make subparsers required
    subparsers = parser.add_subparsers(dest="command", required=True,
                                       help="Available commands")

    # 1. 'quote' command
    subparsers.add_parser(
        "quote", help="Get a single random Ron Swanson quote."
    )

    # 2. 'multiple' command
    multiple_parser = subparsers.add_parser(
        "multiple", help="Get multiple random Ron Swanson quotes."
    )
    multiple_parser.add_argument(
        "count", type=int, help="The number of quotes to fetch (e.g., 5)"
    )

    # 3. 'search' command
    search_parser = subparsers.add_parser(
        "search", help="Search for quotes containing a specific word."
    )
    search_parser.add_argument(
        "query", type=str, help="The word to search for (e.g., 'meat')"
    )

    args = parser.parse_args()

    # --- Execute based on command ---
    quotes = None
    if args.command == "quote":
        quotes = api.get_random_quote()
    elif args.command == "multiple":
        quotes = api.get_multiple_quotes(args.count)
    elif args.command == "search":
        quotes = api.search_quotes(args.query)

    # --- Print results ---
    if quotes:
        if len(quotes) == 0:
            print("No quotes found for your query.")
        else:
            # Print each quote on a new line, formatted nicely
            for i, quote in enumerate(quotes):
                print(f"\n{i+1}. \"{quote}\"")
    else:
        # This handles cases where the API functions returned None
        print("Failed to retrieve quotes.")

if __name__ == "__main__":
    main()