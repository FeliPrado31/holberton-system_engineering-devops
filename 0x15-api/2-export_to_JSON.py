#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == '__main__':
    import requests
    import json
    from sys import argv

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(argv[1]))
    username = r.json().get('username')

    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(argv[1]))
    data = r.json()

    res = {}
    res['{}'.format(argv[1])] = []
    for task in data:
        res['{}'.format(argv[1])].append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username
        })

    with open('{}.json'.format(argv[1]), 'w') as file:
        json.dump(res, file)
