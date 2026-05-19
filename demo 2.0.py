import functions
tasks = []
filename = "tasks.txt"

while True :
    print()
    print("Add")
    print("Show")
    print("Edit")
    print("Complete")
    print("Exit")

    command = input("What do you wanna do  : ").lower().strip()

    if command.startswith("add"):
        add = command[4:] + "\n"
        tasks.append(add)
        tasks = functions.get_tasks()
        tasks.append(add)
        functions.write_tasks(tasks)

    elif command.startswith("show"):
        tasks = functions.get_tasks()
        for index, items in enumerate(tasks):
            items = items.strip("\n")
            print(f"{index+1}. {items}")

    elif command.startswith("edit"):
        try:
            edit = int(command[5:])
            edit -= 1
            new_task = input("Enter the new task  : ").title()+"\n"
            tasks = functions.get_tasks()
            tasks[edit] = new_task
            functions.write_tasks(tasks)

        except ValueError:
            print("Edit function requires integer input")
            continue
        except IndexError:
            print("There is no task with that value")
            continue

    elif command.startswith("complete"):
        try:
            completed_task = (int(command[9:]))
            completed_task -= 1
            tasks = functions.get_tasks(filename)
            tasks.pop(completed_task)
            functions.write_tasks(tasks)

        except ValueError:
            print("Complete function requires integer input")
        except IndexError:
            print("There is no task with that value")

    elif command.startswith("exit"):
        break

    else:
        print("Invalid Input")