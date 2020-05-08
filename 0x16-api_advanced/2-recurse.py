#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no results
are found for the given subreddit, the function should return None.
"""
from requests import *


def recurse(subreddit, res_list=[], after=""):

    url = 'https://api.reddit.com/r/{}/hot?after={}'.format(subreddit, after)
    headers = {'user-agent': 'chrome:happy/0.1.0'}

    response = get(url, headers=headers).json()

    try:
        for data in response.get('data')['children']:
            res_list.append(data['data']['title'])
        if response['data']['after'] is not None:
            recurse(subreddit, res_list, response['data']['after'])
        return res_list
    except Exception:
        return None

