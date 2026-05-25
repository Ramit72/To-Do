import functions
import FreeSimpleGUI as sg
import time

sg.theme("DarkPurple4")
label_time = sg.Text("", key="Time")
label = sg.Text("Enter a Task: ")
input_box = sg.InputText(tooltip="Enter a Task", key = "task")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_tasks(), key="tasks",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window("To-Do App",
                    layout=[
                        [label_time],
                        [label],
                        [input_box, add_button],
                        [list_box, edit_button, complete_button],
                        [exit_button]
                    ],
                    font=("Helvetica",12))
while True:
    event, value = window.read(timeout=1000)
    if event == sg.WIN_CLOSED:
        break
    window["Time"].update(time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = value["task"] +"\n"
            tasks.append(new_task)
            functions.write_tasks(tasks)
            window["tasks"].update(tasks)
            window["task"].update("")

        case "Edit":
            try:
                task_to_edit = value["tasks"][0]
                new_task = value["task"] + "\n"

                tasks = functions.get_tasks()
                index = tasks.index(task_to_edit)
                tasks[index] = new_task
                functions.write_tasks(tasks)
                window["tasks"].update(tasks)

            except IndexError:
                sg.popup("Select an Item first",
                         font=("Helvetica", 12))

        case "Complete":
            try:
                task_to_complete = value["tasks"][0]
                tasks = functions.get_tasks()
                tasks.remove(task_to_complete)
                window["tasks"].update(tasks)
                window["task"].update("")
                functions.write_tasks(tasks)
            except ValueError:
                sg.popup("Select an Item first",
                         font=("Helvetica", 12))

        case "Exit":
            break

        case "tasks":
            window["task"].update(value=value["tasks"][0])



window.close()
