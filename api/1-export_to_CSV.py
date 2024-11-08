#!/usr/bin/python3
"""
This module provides functionality to gather user 
and task data from an API and export it to a CSV file.

"""
import csv
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


def export_to_csv(user_id, user_data, todos_data):
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(
        ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        for task in todos_data:
            writer.writerow([user_id, user_data['username'], task['completed'], task['title']])


if __name__ == "__main__":
    user_id = 1  # Replace with the desired user ID
    user_data, todos_data = gather_data_from_api(user_id)
    export_to_csv(user_id, user_data, todos_data)
