#!/usr/bin/python3
"""
A srcipt that, uses a REST API, for a given employee ID
and Returns information about his/her TODO list progress
exporting data in the CSV format.
"""


import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(url + f"users/{userId}").json()
    todos = requests.get(url + f"todos?userId={userId}").json()
    USERNAME_NAME = user.get("username")
    with open(f"{userId}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow(
                    [
                        userId,
                        USERNAME_NAME,
                        task.get("completed"),
                        task.get("title")
                        ]
                    )
