import functions
import PySimpleGUI as sg

label = sg.Text("Type in something to do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("Checklist App",
                   layout=[[label], [input_box], [add_button]],
                   font=('Helvetica', 15))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()