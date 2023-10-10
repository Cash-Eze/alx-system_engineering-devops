#!/usr/bin/python3

"""working on a module"""

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
        to the subreddit"""
    import requests

    sub_info = requests.get(path.format(subreddit),
                            headers = {"User-Agent": "My-User-Agent"},
                            allow_redirects=False)

    if sub_info.status_code >= 300:
        return 0

    return (sub_info.json().get("data").get("subscriber"))
