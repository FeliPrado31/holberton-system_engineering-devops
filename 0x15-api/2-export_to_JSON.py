#!/usr/bin/python3
"""Write a Python script that, using this REST API
for a given employee ID,
returns information about his/her TODO list progress."""

import json
import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    api = 'https://jsonplaceholder.typicode.com'
    user = requests.get(api+'/users/'+userId)

    name = user.json().get('name')

    todos = requests.get(api+'/todos').json()

    todoUser = {}
    taskList = []

    for task in todos:
        if task.get('userId') == int(userId):
            __task = {"task": task.get('title'),
                      "completed": task.get('completed'),
                      "username": user.json().get('username')}
            taskList.append(__task)
    todoUser[userId] = taskList

    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)
