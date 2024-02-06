# Define a function named get_age that takes two parameters
def get_age(year_of_birth, current_year=2023):
    # Calculate the age by subtracting the year_of_birth from the current_year
    age = current_year - year_of_birth
    # Return the calculated age
    return age

def get_nr_items(user_input):
    # Split the user_input string by comma and store the resulting items in the 'items' list
    items = user_input.split(',')
    # Return the length of the 'items' list
    return len(items)

def foo(a):
    # Calculate the area of a square by multiplying the length of one side by itself
    return a * a

def foo(temperature):
    if temperature > 7:
        # If the temperature is greater than 7, it is considered warm
        return "Warm"
    else:
        # If the temperature is not greater than 7, it is considered cold
        return "Cold"


def foo(password):
    if len(password) >= 8:
        # If the length of the password is greater than or equal to 8, return True
        return True
    else:
        # If the length of the password is less than 8, return False
        return False
