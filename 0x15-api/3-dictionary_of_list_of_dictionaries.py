#!/usr/bin/python3

"""
Script that using this REST API, for a given employee ID,
returns information about his/her TODO list progress
and export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + f"users/").json()
    todo_all_employees = {}
    for user in users:
        userId = str(user.get("id"))
        USERNAME_NAME = user.get("username")
        todos = requests.get(url + f"todos?userId={userId}").json()
        user_tasks = []
        for task in todos:
            user_tasks.append({
                "username": USERNAME_NAME,
                "task": task.get("title"),
                "completed": task.get("completed")
                })
        todo_all_employees[userId] = user_tasks
    with open(f"todo_all_employees.json", "w") as jsonfile:
        json.dump(todo_all_employees, jsonfile)
