#!/usr/bin/python3
"""
    Top hot search on Reddit
"""
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else None

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(f'Error: Failed to fetch posts from r/{subreddit}')
        return

    data = response.json()
    posts = data['data']['children']
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            word = word.lower()
            if (word in title and not title.startswith(word + '.') and not
                    title.startswith(word + '!') and not title.startswith(word + '_')):
                counts[word] = counts.get(word, 0) + 1

    after = data['data']['after']
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f'{word}: {count}')

