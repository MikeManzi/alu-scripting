#!/usr/bin/python3
"""
Returns the number of subscribers from a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ Set a custom header user-agent """
    headers = {"User-Agent": "ALU-scripting API 0.1"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            return data.get('subscribers', 0)
    return 0
    