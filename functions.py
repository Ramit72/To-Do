def get_tasks(filepath="tasks.txt"):
    '''reads text files and returns contents'''
    with open(filepath, "r") as f:
        tasks_local = f.readlines()
        return tasks_local

def write_tasks(tasks,filepath="tasks.txt"):
    '''writes tasks to a text file'''
    with open(filepath, "w") as f:
        f.writelines(tasks)
