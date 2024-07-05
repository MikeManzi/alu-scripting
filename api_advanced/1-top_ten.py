#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests
import sys


def top_ten(subreddit):
    agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': agent
    }

    params = {
        'limit': 10
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    reddit = response.json()
    top = reddit['data']['children']
    if len(top) is 0:
        print(None)
    else:
        for post in top:
            print(post['data']['title'])