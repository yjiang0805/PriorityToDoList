tasks = []
classes = []

def get_tasks():
    return tasks[1:]

def create_tasks(assignmentName, assignmentClass, dueDate, dueTime, assignmentWeight):
    tasks.append({
        "assignmentName": assignmentName,
        "assignmentClass": assignmentClass,
        "dueDate": dueDate,
        "dueTime": dueTime,
        "assignmentWeight": assignmentWeight
    })

def get_classes():
    return classes[1:]

def create_classes(className):
    classes.append({
        "className": className
    })