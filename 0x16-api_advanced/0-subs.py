#!/usr/bin/python3
"""
Get number of users from Reddit 
"""

import requests

def number_of_subscribers(subreddit):
    """ Return the number of subscribers to a given subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code !== 200:
        return 0
    else:
        data = response.json()
        if 'data' not in data:
            return 0
        if 'subscribers' not in data.get('data'):
            return 0
        return data.json()['data']['subscribers']

 