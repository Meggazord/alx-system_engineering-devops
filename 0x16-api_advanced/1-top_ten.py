#!/usr/bin/python3
"""
Get number of top 10 posts from Reddit
"""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 10}
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return
    
    try:
        data = response.json()
        posts = data['data']['children'][:10]
        for post in posts:
            print(post['data']['title'])
    except ValueError:
        print(None)
    except:
        print(None)
