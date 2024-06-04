#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return

    try:
        # Attempt to parse the JSON response
        results = response.json().get("data")
        if not results:
            print("None")
            return
        # Print the titles of the 10 hottest posts
        for c in results.get("children"):
            print(c.get("data").get("title"))
    except ValueError:
        # Handle JSON decode error
        print("None")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: {} <subreddit>".format(sys.argv[0]))
    else:
        top_ten(sys.argv[1])
