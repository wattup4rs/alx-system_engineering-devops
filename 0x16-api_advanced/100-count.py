#!/usr/bin/python3
"""
A recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count
of given keywords (case-insentitive, delimited by spaces.
Javascript should count as javascript, but java should not)
"""

def count_words(subreddit, word_list, count_dict=None):
    """

    Recursively queries the Reddit API, parse the title of all hot articles,
    and prints a sorted count of given keywords.


    Args:
        subreddit (str): The name of the subreddit to search for.
        word_list (list): A list of keywords to count occurences of.
        count_dict (dict): A dictionary to store the count of each
        keyword (default is None).

    Returns:
        None
    """
    if count_dict is None:
        count_dict = {}

    if not word_list:
        sorted_counts = sorted(count_dict.items(),
                               key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
        return

    word = word_list[0]

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    headers = {"User-Agent": "Chris-User-Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        if data:
            for post in data:
                title = post['data']['title']
                title_words = title.lower().split()
                if word.lower() in title_words:
                    count_dict[word] = count_dict.get(word, 0) + \
                        title_words.count(word.lower())
        count_words(subreddit, word_list[1:], count_dict)
    else:
        print("Nothing")
