import FreeSimpleGUI as sg
label1 = sg.Text("Enter feet: ")
input1 = sg.InputText("", key = "feet")
label2 = sg.Text("Enter inches: ")
input2 = sg.InputText("", key = "inches")

button = sg.Button("Convert")
output = sg.Text('', key = "meters")
window = sg.Window("Convertor",
                   layout=[
                       [label1, input1],
                       [label2,input2],
                       [button, output]
                        ]
                   )
while True:
    event, values = window.read()
    print(window.read())
    print(values)
    total_inches = (int(values["feet"])*12)+int(values["inches"])
    print(total_inches)
    meters = total_inches*0.0254
    window["meters"].update(meters)

window.close()