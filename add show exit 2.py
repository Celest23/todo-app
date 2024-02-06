todos = []

while True:
    user_action = input("Type add, show, or exit: ")
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
        case'exit':
            break
        case _: #this line is for when you enter something else than add sow or exit
            print("you entered an unkown command")

print("Bye!")