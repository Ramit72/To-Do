tasks = []

while True :
    print()
    print("Add")
    print("Show")
    print("Edit")
    print("Complete")
    print("Exit")
    command = input("What do you wanna do  : ").lower().strip()

    match command:
        case "add":
            add = input("What task do you want to add  : ").lower() + "\n"
            tasks.append(add)
            with open ("tasks.txt", "a") as f:
                f.writelines(tasks)

        case "show":
            with open ("tasks.txt", "r") as f:
                tasks = f.readlines()
            for index, items in enumerate(tasks):
                items = items.strip("\n")
                print(f"{index+1}. {items}")

        case "edit":
            edit_number = int(input("Enter the number of the task you want to edit  : ")) - 1
            new_task = input("Enter the new task  : ").title()+"\n"
            with open( "tasks.txt", "r") as f:
                tasks = f.readlines()
                tasks[edit_number] = new_task
            with open ("tasks.txt", "w") as f:
                f.writelines(tasks)

        case "complete":
            completed_task = int(input("Enter the number of the completed task  : ")) - 1
            with open("tasks.txt", "r") as f:
                tasks = f.readlines()
            tasks.pop(completed_task)
            with open ("tasks.txt", "w") as f:
                f.writelines(tasks)
        case "exit":
            break