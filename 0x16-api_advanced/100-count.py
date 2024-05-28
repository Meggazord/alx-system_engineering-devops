#!/usr/bin/python3
"""
Recurssive reddit function
"""

import requests
import re

def count_words(subreddit, word_list, after="", word_counts={}):
    """
    Recursively counts occurrences of specified keywords in titles of all hot articles from a subreddit.
    
    Args:
        subreddit (str): The subreddit to query.
        word_list (list): List of keywords to count.
        after (str, optional): ID to handle pagination.
        word_counts (dict, optional): Accumulator for word counts.
    
    Returns:
        None: Prints the counts of keywords sorted by frequency and alphabetically.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'Mozilla/5.0'}
    if after:
        url += f"&after={after}"

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        if not word_counts:
            return
        else:
            sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                if count > 0:
                    print(f"{word}: {count}")
            return

    data = response.json()
    posts = data.get('data', {}).get('children', [])
    if not posts:
        return

    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            found_words = re.findall(r'\b{}\b'.format(word.lower()), title)
            if word.lower() in word_counts:
                word_counts[word.lower()] += len(found_words)
            else:
                word_counts[word.lower()] = len(found_words)

    after = data['data'].get('after', None)
    if after is None:
        sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            if count > 0:
                print(f"{word}: {count}")
    else:
        count_words(subreddit, word_list, after, word_counts)
