#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports the data in CSV format.
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data.get('username')

        csv_file_name = '{}.csv'.format(employee_id)

        with open(csv_file_name, mode='w', newline="") as csv_file:
            writer = csv.writer(csv_file)
            for task in todos_data:
                task_status = task.get('completed')
                task_title = task.get('title')
                writer.writerow([
                    employee_id, 
                    employee_name, 
                    task_status, 
                    task_title
                ])
    except Exception as e:
        print("An error occurred:", e)
