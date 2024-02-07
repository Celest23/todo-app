import functions
import PySimpleGUI as sg

label = sg.Text("Type in something to do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("Checklist App", layout=[[label], [input_box, add_button]])
window.read()
window.close()