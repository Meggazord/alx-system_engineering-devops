#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports the data in JSON format.
"""

import json
import requests

if __name__ == "__main__":

    users_url = 'https://jsonplaceholder.typicode.com/users/'
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'

    try:
        users = requests.get(users_url)
        users_data = users.json()
        data = {}
        for user in users_data:
            todos_data = requests.get(todos_url.format(user['id'])).json()
            data[user['id']] = []
            for task in todos_data:
                data[user['id']].append({
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": user['username'] 
                })

        json_file_name = 'todo_all_employees.json'

        with open(json_file_name, mode='w') as json_file:
            json.dump(data, json_file)

    except Exception as e:
        print("An error occurred:", e)

