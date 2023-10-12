#!/usr/bin/python3
"""Module for task1"""


def top_ten(subreddit):
    """requests for top ten qeuries"""
    import requests

    path = "https://www.reddit.com/r/{}/hot?limit=10.json"

    sub_info = requests.get(path.format(subreddit),
                            headers= { "User-Agent": "My-User-Agent"},
                            allow_redirects=False)

    if sub_info.status_code >= 300:
        print(None)
    else:
        [print(child.get("data").get("title"))
        for child in sub_info.json().get("data").get("children")]
