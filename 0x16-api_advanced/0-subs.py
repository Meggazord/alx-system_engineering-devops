#!/usr/bin/python3
"""
Get number of users from Reddit
"""

import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers to a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers if the subreddit is valid, otherwise 0.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    head = {'user-agent': 'Mozilla/5.0'}
    req = requests.get(url, headers=head, allow_redirects=False)
    try:
        return req.json()['data']['subscribers']
    except:
        return 0
