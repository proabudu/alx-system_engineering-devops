#!/usr/bin/python3
"""
number of subscribers for a given subreddit

This script queries the Reddit API to retrieve the number of subscribers
(total subscribers, not active users) for a specified subreddit.

Raises an exception if the API request fails.
"""

from requests import get


def number_of_subscribers(subreddit: str) -> int:
    """
    Function that queries the Reddit API and returns the number of subscriber
    (not active users, total subscribers) for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if an error 

    Raises:
        Exception: If the API request fails.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)

    if response.status_code == 200:  # Check for successful response
        results = response.json()
        return results.get('data', {}).get('subscribers', 0)  # Handle po
    else:
        raise Exception(f"API request  status code: {response.status_code}")

# Example usage (assuming you have the requests library installed)
subreddit_name = "learnpython"
num_subscribers = number_of_subscribers(subreddit_name)
print(f"The subreddit '{subreddit_name}' has {num_subscribers} subscribers.")
