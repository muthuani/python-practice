# Python *args and **kwargs Example

# --- Concept ---
# *args allows a function to accept a variable number of positional arguments.
# **kwargs allows a function to accept a variable number of keyword arguments (key=value pairs).

# Example 1: Using *args
def sum_numbers(*args):
    """
    This function takes any number of positional arguments and returns their sum.
    """
    total = 0
    for num in args:
        total += num
    return total

# Calling the function with different numbers of arguments
print("Sum of 2, 3, 5:", sum_numbers(2, 3, 5))          # Output: 10
print("Sum of 1, 2, 3, 4, 5:", sum_numbers(1, 2, 3, 4, 5))  # Output: 15

# Example 2: Using **kwargs
def greet_people(**kwargs):
    """
    This function takes any number of keyword arguments and prints greetings.
    """
    for key, value in kwargs.items():
        print(f"Hello {value}! You are my {key}.")

# Calling the function with keyword arguments
greet_people(friend="Rio", sister="Maya", brother="Arun")
# Output:
# Hello Rio! You are my friend.
# Hello Maya! You are my sister.
# Hello Arun! You are my brother.

# Example 3: Using *args and **kwargs together
def introduce_person(*args, **kwargs):
    """
    This function takes multiple names as positional arguments (*args)
    and additional details as keyword arguments (**kwargs).
    """
    print("Names:", args)
    print("Details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function
introduce_person("Rio", "Maya", age=12, country="UK")
# Output:
# Names: ('Rio', 'Maya')
# Details:
# age: 12
# country: UK
