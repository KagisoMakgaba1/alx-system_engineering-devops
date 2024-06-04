#!/usr/bin/python3
"""This script queries the Reddit API and returns the number of total
subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to return the number of subscribers for a
    given subreddit.

    :param subreddit: The name of the subreddit.
    :return: Number of subscribers or 0 if invalid subreddit.
    """
    # Define the URL for the subreddit's about.json endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "Mozilla/5.0 (compatible; myscript/1.0)"}

    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status code indicates a successful request
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract the number of subscribers
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            # If the subreddit is invalid or not found, return 0
            return 0
    except Exception:
        # In case of any other exceptions, return 0
        return 0
