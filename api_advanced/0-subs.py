#!/usr/bin/python3
"""
Returns the number of subscribers from a subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """ Set a custom header user-agent """
    headers = {"User-Agent": "ALU-scripting API 0.1"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    try:
        response = requests.get(url, headers=headers, timeout=30, allow_redirects=False)
        response.raise_for_status()  # Raises an HTTPError for bad responses
    except requests.exceptions.Timeout:
        return "The request timed out"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

    if response.status_code == 200:
        json_data = response.json()
        subscriber_number = json_data.get("data", {}).get("subscribers", 0)
        return subscriber_number
    elif response.status_code == 404:
        return 0
    else:
        return 0
