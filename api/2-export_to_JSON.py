#!/usr/bin/python3
"""A python script that returns information about an
employees TODO list progress.
"""
import json
import requests
import sys


def get_todo_info():
    """A function that gets the todo information for a particular user id"""
    user_id = sys.argv[1]
    # GET /user/<id> resource for user info
    r = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                     .format(user_id))
    user = json.loads(r.text)
    user_name = user[0].get('username')

    # GET /user/<id>/todos for todo info
    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(user_id))
    todos = json.loads(r.text)
    dict_ = {}
    task_list = []
    dict_[user_id] = task_list
    for task in todos:
        task_d = {}
        task_d['task'] = task.get('title')
        task_d['completed'] = task.get('completed')
        task_d['username'] = user_name
        task_list.append(task_d)

    with open("{}.json".format(user_id), 'w', encoding='utf-8') as fp:
        json.dump(dict_, fp)


if __name__ == "__main__":
    get_todo_info()
