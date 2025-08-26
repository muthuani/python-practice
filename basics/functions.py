# Example 1: A simple function without parameters
def greet():
    print("Hello! Welcome to Python functions.")

# Calling the function
greet()  # Output: Hello! Welcome to Python functions.

# Example 2: Function with parameters
def greet_person(name):
    print("Hello,", name, "Welcome!")

# Calling the function with an argument
greet_person("John")  # Output: Hello, John Welcome!

# Example 3: Function that returns a value
def add_numbers(a, b):
    sum_value = a + b
    return sum_value

# Calling the function and storing the result
result = add_numbers(5, 10)
print("Sum:", result)  # Output: Sum: 15

# Example 4: Function with default parameter values
def greet_age(name, age=10):
    print(f"Hello {name}, you are {age} years old.")

greet_age("Maya")          # Output: Hello Maya, you are 10 years old.
greet_age("Maya", 12)      # Output: Hello Maya, you are 12 years old.

# Example 5: Function with multiple return values
def arithmetic_operations(x, y):
    sum_val = x + y
    diff = x - y
    return sum_val, diff

s, d = arithmetic_operations(8, 3)
print("Sum:", s, "Difference:", d)  # Output: Sum: 11 Difference: 5
