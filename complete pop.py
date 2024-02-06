while True:
    # Get user input and remove space after you write a code
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + '\n'

            file = open('Journal/files/Todo.txt', "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)  # append is to add more it's a method

            file = open('Journal/files/Todo.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show' | 'display':  # you can use show or display by putting |
            file = open('Journal/files/Todo.txt', 'r')  # to read the file
            todos = file.readlines()
            file.close()

            for index, item in enumerate(
                    todos):  # this removes the parentheses etc. #enumerate is to put numbers in front of the list
                item = item.strip("\n")  # using a list comprehension you can remove the space between (backslash) items
                row = f'{index + 1}:){item}'  # the f function removes the space, put what you want to fill the space.
                # i put :)
                # in index writing +1 means the number will start from 1 and not 0
                item = item.title()  # the items will be capitalized
                print(row)

                # new_todo = [item.strip("\n") for item in todos] that's list comprehension

        case 'edit':
            number = int(input("Number of the todo to edit: "))  # convert a str to an int which is a number
            number = number - 1  # this is to make sure the count doesn't start by zero
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo  # this is to replace what you want

        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':

            break
        case _:  # this line is for when you enter something else than add sow or exit
            print("you entered an unknown command")

print("Bye!")
