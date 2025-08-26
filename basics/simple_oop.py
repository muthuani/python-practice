# Python Classes and Objects Example

# --- Concept ---
# A class is like a blueprint for creating objects.
# An object is an instance of a class, which can have attributes (data) and methods (functions).

# Define a class
class Person:
    """
    This is a simple class to represent a person.
    """
    # Constructor method to initialize object attributes
    def __init__(self, name, age):
        self.name = name  # Attribute: name
        self.age = age    # Attribute: age

    # Method to display person details
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    # Method to celebrate birthday
    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

# --- Creating Objects ---
# Create an object of the class Person
person1 = Person("Rio", 12)
person2 = Person("Maya", 10)

# Accessing object methods
person1.display()  # Output: Name: Raj, Age: 12
person2.display()  # Output: Name: Maya, Age: 10

# Calling a method to change object state
person1.birthday()  # Output: Happy Birthday Raj! You are now 13 years old.

# Accessing attributes directly
print(person1.name)  # Output: Raj
print(person1.age)   # Output: 13
