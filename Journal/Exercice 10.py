# Define a function named get_max
def get_max():
    # Create a list of grades
    grades = [9.6, 9.2, 9.7]
    # Find the maximum value in the grades list using the max() function
    maximum = max(grades)
    # Return the maximum value
    return maximum
# Call the get_max() function and print the result
print(get_max())


def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    message = f"Max: {maximum}, Min: {minimum}"
    return message


print(get_max())


def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32

print(fahrenheit)