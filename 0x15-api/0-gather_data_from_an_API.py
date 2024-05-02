#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    employee_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data.get('name')
        total_tasks = len(todos_data)
        completed_tasks = [task.get('title') for task in todos_data if task.get('completed')]

        print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), total_tasks))
        for task in completed_tasks:
            print("\t {}".format(task))
    except Exception as e:
        print("An error occurred:", e)
