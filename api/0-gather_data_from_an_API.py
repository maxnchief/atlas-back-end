#!/usr/bin/python3
"""
This module provides functionality to fetch and
display the TODO list progress of an employee
from a given API. It uses the `requests` library
to make HTTP requests to the API and fetch
the necessary data.

Functions:
    get_employee_todo_progress(employee_id):
        Fetches and displays the TODO list progress of the specified employee.

Usage:
    Run the module from the command line with the employee ID as an argument:
    python 0-gather_data_from_an_API.py <employee_id>
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print("Employee not found")
        return

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list data
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if todos_response.status_code != 200:
        print("Error fetching TODO list")
        return

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Display the TODO list progress
    print(
        f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
