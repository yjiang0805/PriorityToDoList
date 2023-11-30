tasks = []
classes = []

def get_tasks():
    return tasks[1:]

def create_tasks(assignmentName, assignmentClass, dueDate, dueTime, assignmentWeight, task_status):
    tasks.append({
        "assignmentName": assignmentName,
        "assignmentClass": assignmentClass,
        "dueDate": dueDate,
        "dueTime": dueTime,
        "assignmentWeight": assignmentWeight,
        "taskStatus": task_status
    })

def get_classes():
    return classes[1:]

def create_classes(className):
    classes.append({
        "className": className
    })

def search_task(assignmentName):
    for task in tasks:
        if task["assignmentName"] == assignmentName:
            return task

def delete_task(assignmentName):
    for task in tasks:
        if task["assignmentName"] == assignmentName:
            tasks.remove(task)
            return True
    return False