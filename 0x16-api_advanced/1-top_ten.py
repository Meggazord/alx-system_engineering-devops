#!/usr/bin/python3
"""
Get number of top 10 posts from Reddit
"""

import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json()
    posts = data.get('data', {}).get('children', [])
    if not posts:
        print(None)
        return
    for post in posts:
        print(post['data']['title'])
