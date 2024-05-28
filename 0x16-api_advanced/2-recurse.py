#!/usr/bin/python3
"""
Recurssive reddit import
"""
import requests

def recurse(subreddit, hot_list=[], after=""):
    """Recursively collect titles of all hot articles from a subreddit.
    
    Args:
        subreddit (str): The subreddit to query.
        hot_list (list): Accumulator for titles.
        after (str): ID to handle pagination.

    Returns:
        list or None: List of titles, or None if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'Mozilla/5.0'}
    if after:
        url += f"&after={after}"

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None if not hot_list else hot_list

    data = response.json()
    posts = data.get('data', {}).get('children', [])
    if not posts:
        return None if not hot_list else hot_list

    hot_list.extend(post['data']['title'] for post in posts)

    after = data['data'].get('after', None)
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)
