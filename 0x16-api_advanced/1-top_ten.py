#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests

def top_ten(subreddit):
    """

    Queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to search for.
    
    Returns:
        None
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = requests.get(url, headers=user_agent, params=params)
    all_data = response.json()

    try:
        raw1 = all_data.get('data').get('children')

        for i in raw1:
            print(i.get('data').get('title'))

    except:
        print("None")
