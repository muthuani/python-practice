# Python Variables Example

# A variable is like a container that stores data.
# You can give it a name and assign a value using the "=" sign.

# Assigning an integer value to a variable
age = 12
print("Age:", age)  # Output: Age: 12

# Assigning a string value to a variable
name = "John"
print("Name:", name)  # Output: Name: Raj

# Assigning a floating-point number
height = 1.5  # in meters
print("Height:", height)  # Output: Height: 1.5

# Variables can be updated with new values
age = 13
print("Updated Age:", age)  # Output: Updated Age: 13

# Multiple variables can be assigned in a single line
x, y, z = 5, 10, 15
print("x:", x, "y:", y, "z:", z)  # Output: x: 5 y: 10 z: 15

# Variables can also hold the result of calculations
sum_value = x + y + z
print("Sum:", sum_value)  # Output: Sum: 30

# Variable names should start with a letter or underscore, 
# cannot start with a number, and cannot contain spaces or special characters
# Examples:
_valid_variable = 100
anotherVariable = 200
# 1invalid = 300  # ❌ This will cause an error
print("----------------------------------")

# Interactive Variables Example

# Ask the user to enter their name
name = input("Enter your name: ")  # input() returns a string
print("Hello,", name)

# Ask the user to enter their age
age = int(input("Enter your age: "))  # Convert input to integer
print("You are", age, "years old.")

# Ask the user to enter their height in meters
height = float(input("Enter your height in meters: "))  # Convert input to float
print("Your height is", height, "meters.")

# Calculate the year they will turn 100
current_year = 2025
year_hundred = current_year + (100 - age)
print(name + ", you will turn 100 years old in the year", year_hundred)

# Assign multiple variables in one line
x, y = 5, 10
print("x + y =", x + y)

# Update a variable
x = x + 1
print("Updated x:", x)
