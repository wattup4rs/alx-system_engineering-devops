#!/usr/bin/python3
"""
A script that uses a REST API, for a given employee ID, returns
information about his/her TODO list progress 
and exports data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(url + f"users/{userId}").json()
    todos = requests.get(url + f"todos?userId={userId}").json()
    USERNAME_NAME = user.get("username")
    user_tasks = {userId: []}
    for task in todos:
        user_tasks[userId].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": USERNAME_NAME
            })
    with open(f"{userId}.json", "w") as jsonfile:
        json.dump(user_tasks, jsonfile)
