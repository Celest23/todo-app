todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    #the next line is to remove the space
    user_action = user_action.strip() #this removes the space after you write a code
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show'| 'display': #you can use show or display by putting |
            for index, item in enumerate(todos): #this removes the parenthese etc.. #enumerate is to put numbers in front of the list
                row = f'{index + 1}:){item}'# the f function removes the space, put what you want to fill the space. i put :)
                #in index writting +1 means the number will start from 1 and not 0
                item = item.title() #this line will make all the todo capitalized

                print(row)
        case'edit':
            number = int(input("Number of the todo to edit: "))  #convert a str to an int which is a number
            number = number - 1 # this is to make sure the count doesnt start by zero
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo  # this is to replace what you want

        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':

            break
        case _: #this line is for when you enter something else than add sow or exit
            print("you entered an unkown command")

print("Bye!")