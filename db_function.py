import datetime
import operator

now = datetime.date.today()

tasks = []
keys = []

def get_tasks():
    tasks.sort(reverse=True,key=func) 
    return tasks

def func(d):
    return d["priorityValue"]

def print_tasks():
    print("Tasks: ")
    for task in tasks:
        print(task["assignmentName"], ":" ,task["id"], "\n")
            
    print("---------------------")



def create_tasks(assignmentName, dueDate, dueTime, assignmentWeight, points, key):
    tasks.append({
        "id": key,
        "assignmentName": assignmentName,
        "dueDate": dueDate,
        "dueTime": dueTime,
        "points": points,
        "assignmentWeight": assignmentWeight,
        "priorityValue": round(assign_priority_value(dueDate, assignmentWeight, points), 2)
    })  
  

def remove_task(id):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)

def assign_priority_value(date, weight, points):
    dueDateTime = date - now
    return 10 * (1/(dueDateTime.days+1 + dueDateTime.seconds+1)) + (weight * points)


