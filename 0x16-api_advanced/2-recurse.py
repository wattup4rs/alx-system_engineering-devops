#!/usr/bin/python
""" A recursivefunction that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddits, the function should
return None.
"""

import requests

def recurse(subreddit, hot_list=[]):
    """

    Recursively queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to search for.
        hot_list (list): A list to store the titles of hot articles
        (default is an empty list).

    Returns:
        list: A list containing the titles of all articles for the
        given subreddit, or None if no results are found.
    """

    if hot_list and not subreddit:
        return hot_list

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    headers = {"User-Agent": "Chris-User-Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        if data:
            for post in data:
                hot_list.append(post['data']['title'])
            return recurse(subreddit, hot_list)
        else:
            return None
    else:
        return None
