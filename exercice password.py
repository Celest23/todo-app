password = input("Enter your password: ")

if len(password) > 7:
    print("Great password there")
elif len(password) == 7:
    print("Password is OK, but not too strong")
else:
    print("password is weak")

    #dictionary

day_temperatures = {"morning": 10.2, "noon": 23.4, "evening": 34.4}
print(day_temperatures)

#tuples in dictionary

day_temperatures = {'morning': (1.1, 2.2, 3.4), 'noon': (2.3, 4.5, 3.1), 'evening': (2.4, 3.5, 6.5)}
print(day_temperatures)

#print a specificnumber of letter in a tuple
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])

#Print a slice of the list containing the last three elements
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[-3:])