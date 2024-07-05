#!/usr/bin/python3
"""
Returns the number of subscribers from a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ Set a custom header user-agent """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            print("We got the data")
            return data.get('subscribers', 0)
    return 0
    