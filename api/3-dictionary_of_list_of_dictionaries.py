#!/usr/bin/python3
"""
This module fetches user data and their associated tasks 
from a placeholder API
and stores the information in a JSON file.
The data is organized in a dictionary
where each key is a user ID and the value is a 
list of dictionaries containing
task details for that user.

"""
import json
import requests

# URL for the API
url = "https://jsonplaceholder.typicode.com"

# Fetch users
users = requests.get(f"{url}/users").json()

# Dictionary to store all tasks for all employees
all_tasks = {}


# Iterate through each user to fetch their tasks
for user in users:
    user_id = user['id']
    username = user['username']
    tasks = requests.get(
        f"{url}/todos", params={"userId": user_id}).json()
    
    # List to store tasks for the current user
    user_tasks = []
    for task in tasks:
        user_tasks.append({
            "username": username,
            "task": task['title'],
            "completed": task['completed']
        })
    
    # Add the user's tasks to the dictionary
    all_tasks[user_id] = user_tasks

# Write the dictionary to a JSON file

with open("todo_all_employees.json", "w") as json_file:
    json.dump(all_tasks, json_file)
