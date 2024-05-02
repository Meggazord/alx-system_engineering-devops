#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports the data in CSV format.
"""

import csv
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

        employee_name = user_data.get('username')

        csv_file_name = '{}.csv'.format(employee_id)

        with open(csv_file_name, mode='w') as csv_file:
            fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for task in todos_data:
                writer.writerow({'USER_ID': employee_id,
                                 'USERNAME': employee_name,
                                 'TASK_COMPLETED_STATUS': task.get('completed'),
                                 'TASK_TITLE': task.get('title')})

        print("CSV file '{}' has been created.".format(csv_file_name))
    except Exception as e:
        print("An error occurred:", e)
