try:
    # Prompt the user to enter the total value and convert it to a float
    total_value = float(input("Enter total value: "))

    # Prompt the user to enter the value and convert it to a float
    value = float(input("Enter value: "))

    # Calculate the percentage using the formula value/total_value * 100
    percentage = value / total_value * 100

    # Print the calculated percentage
    print(f"That is {percentage}%")
except ValueError:
    # Handle the case when the user doesn't enter a number
    print("You need to enter a number. Run the program again.")

colors = [11, 34, 98, 43, 45, 54, 54]

# Iterate over each color in the list
for color in colors:
    # Check if the color is greater than 50
    if color > 50:
        # Print the color if it satisfies the condition
        print(color)

        waiting_list = ["john", "marry"]
        name = input("Enter name: ")

        try:
            number = waiting_list.index(name)
            print(f"{name}'s turn is {number}")
        except ValueError:
            print(f"{name} is not in the list.")