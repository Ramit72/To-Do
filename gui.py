import functions
import FreeSimpleGUI as gui

label = gui.Text("Enter a Task: ")
input_box = gui.InputText(tooltip="Enter a Task: ")
add_button = gui.Button("Add")
window = gui.Window("To-Do App", layout=[[label,input_box, add_button]])
window.read()
window.close()
