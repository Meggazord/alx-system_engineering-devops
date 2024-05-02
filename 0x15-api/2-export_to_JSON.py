#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports the data in JSON format.
"""

import json
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

        json_file_name = '{}.json'.format(employee_id)

        data = {employee_id: []}

        for task in todos_data:
            data[employee_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": employee_name  
            })

        with open(json_file_name, mode='w') as json_file:
            json.dump(data, json_file)

        print("JSON file '{}' has been created.".format(json_file_name))
    except Exception as e:
        print("An error occurred:", e)
