#!/usr/bin/python3
""" Gather data from an API """
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(url + f"users/{userId}").json()
    todos = requests.get(url + f"todos?userId={userId}").json()
    EMPLOYEE_NAME = user.get("name")
    TOTAL_NUMBER_OF_TASKS = len(todos)
    NUMBER_OF_DONE_TASKS = 0
    for task in todos:
        if task["completed"]:
            NUMBER_OF_DONE_TASKS += 1
    print(
            f"Employee {EMPLOYEE_NAME} is done with tasks"
            f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"
            )
    for task in todos:
        if task["completed"]:
            print("\t {}".format(task["title"]))
