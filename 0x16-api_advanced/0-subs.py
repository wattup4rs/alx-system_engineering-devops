#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""
import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "0x16-api_advanced (gideonwatt@gmail.com)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return (response.json().get('data')).get('subscribers')
    else:
        return 0
