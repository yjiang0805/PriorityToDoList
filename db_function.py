import datetime
import operator

now = datetime.date.today()

tasks = []
classes = []

def get_tasks():
    tasks.sort(reverse=True,key=func) 

    for task in tasks:
        print(task["priorityValue"])

    return tasks

def func(d):
    return d["priorityValue"]

def create_tasks(assignmentName, dueDate, dueTime, assignmentWeight, points, key):
    tasks.append({
        "id": key,
        "assignmentName": assignmentName,
        "dueDate": dueDate,
        "dueTime": dueTime,
        "points": points,
        "assignmentWeight": assignmentWeight,
        "priorityValue": round(assign_priority_value(dueDate, dueTime, assignmentWeight, points), 2)
    })  
      

def remove_task(id):
    print("here!")
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)


def assign_priority_value(date, time, weight, points):
    dueDateTime = now - date
    return 10 * (1/(dueDateTime.days+1 + dueDateTime.seconds+1)) + 10 * (weight * points)


