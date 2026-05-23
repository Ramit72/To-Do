import functions
import FreeSimpleGUI as sg

label = sg.Text("Enter a Task: ")
input_box = sg.InputText(tooltip="Enter a Task", key = "task")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_tasks(), key="tasks",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")

window = sg.Window("To-Do App",
                    layout=[
                        [label],
                        [input_box, add_button],
                        [list_box, edit_button]
                    ],
                    font=("Helvetica",12))
while True:
    event, value = window.read()
    # print(1,event)
    # print(2,value)
    # print(3,value["tasks"][0])
    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = value["task"] +"\n"
            tasks.append(new_task)
            functions.write_tasks(tasks)
            window["tasks"].update(tasks)

        case "Edit":
            task_to_edit = value["tasks"][0]
            new_task = value["task"] + "\n"

            tasks = functions.get_tasks()
            index = tasks.index(task_to_edit)
            tasks[index] = new_task
            functions.write_tasks(tasks)
            window["tasks"].update(tasks)

        case sg.WIN_CLOSED:
            break
window.close()
