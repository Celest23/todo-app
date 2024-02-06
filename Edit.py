todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    #the next line is to remove the space
    user_action = user_action.strip() #this removes the space after you write a code
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show'| 'display': #you can use show or display by putting |
            for item in todos: #this removes the parenthese etc..
                item = item.title() #this line will make all the todo capitalized

                print(item)
        case'edit':
            number = int(input("Number of the todo to edit: "))  #convert a str to an int which is a number
            number = number - 1 # this is to make sure the count doesnt start by zero
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo  # this is to replace what you want

        case 'exit':

            break
        case _: #this line is for when you enter something else than add sow or exit
            print("you entered an unkown command")

print("Bye!")