#!/usr/bin/python3
"""
This module provides functionality to gather data from an API and export it to a JSON file.

"""
import json
import requests


def gather_data_from_api(user_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        raise Exception("Error fetching data from API")

    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data


def export_to_json(user_id):
    user_data, todos_data = gather_data_from_api(user_id)

    tasks = []
    for task in todos_data:
        task_info = {
            "task": task["title"],
            "completed": task["completed"],
            "username": user_data["username"]
        }
        tasks.append(task_info)

    data = {str(user_id): tasks}

    with open(f"{user_id}.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    user_id = 1  # Replace with the desired user ID
    export_to_json(user_id)
