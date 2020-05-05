#!/usr/bin/python3
"""Write a Python script that, using this REST API
for a given employee ID,
returns information about his/her TODO list progress."""

if __name__ == '__main__':
    import requests
    import csv
    from sys import argv

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(argv[1]))
    username = r.json().get('username')

    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(argv[1]))
    data = r.json()

    with open('{}.csv'.format(argv[1]), mode='w') as f:
        writter = csv.writer(f, delimiter=',', quotechar='"',
                             quoting=csv.QUOTE_ALL)
        for task in data:
            writter.writerow([argv[1], username, task.get('completed'),
                              task.get('title')])
