#!/usr/bin/python3
"""
Get number of users from Reddit 
"""

import requests

def number_of_subscribers(subreddit):
    """ Return the number of subscribers to a given subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
    return 0
 
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print(number_of_subscribers(sys.argv[1]))
    else:
        print("Please provide a subreddit name.")
