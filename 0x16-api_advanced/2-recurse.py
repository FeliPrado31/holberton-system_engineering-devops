#!/usr/bin/python3
"""Module recurse
"""
from requests import *


def recurse(subreddit, hot_list=[], after=""):

    api = 'https://api.reddit.com/r/{}/hot?after={}'.format(subreddit, after)
    headers = {'User-Agent': 'happy'}
    response = get(api, headers=headers).json()
    try:
        for data in response.get('data')['children']:
            hot_list.append(data['data']['title'])
        if response['data']['after'] is not None:
            recurse(subreddit, hot_list, response['data']['after'])
        return hot_list
    except Exception:
        return None
