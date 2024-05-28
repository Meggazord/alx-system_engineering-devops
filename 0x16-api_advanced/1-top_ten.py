#!/usr/bin/python3
"""
Get number of top 10 posts from Reddit
"""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit."""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 10}
    headers = {'user-agent': 'Mozilla/5.0'}
    response = requests.get(url, params=params, headers=headers, allow_redirects=False)
    try:
        for num in range(0, 10):
            print(response.json()['data']['children'][num]['data']['title'])
    except:
        print(None)