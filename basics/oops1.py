from abc import ABC, abstractmethod
#Let’s combine Encapsulation, Abstraction, Inheritance, and Polymorphism into one single Python program
# --------------------------
# 🔵 Abstraction
# --------------------------
class Animal(ABC):  # Abstract class
    @abstractmethod
    def sound(self):
        pass

# --------------------------
# 🟢 Encapsulation
# --------------------------
class Pet(Animal):  # Pet is still abstract because Animal is abstract
    def __init__(self, name, age):
        self.name = name             # Public attribute
        self.__age = age             # Private attribute (Encapsulation)

    def get_age(self):               # Getter for private attribute
        return self.__age

    def set_age(self, age):          # Setter for private attribute
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

# --------------------------
# 🟣 Inheritance
# --------------------------
class Dog(Pet):  # Dog inherits from Pet
    def sound(self):  # Implementation of abstract method
        print(f"{self.name} says: Woof! Woof!")

class Cat(Pet):  # Cat inherits from Pet
    def sound(self):
        print(f"{self.name} says: Meow! Meow!")

# --------------------------
# 🟠 Polymorphism
# --------------------------
def animal_sound(animal):  # Common interface
    animal.sound()

# --------------------------
# ✅ Main Program
# --------------------------
dog = Dog("Buddy", 3)
cat = Cat("Kitty", 2)

# Accessing public and private attributes
print(f"Dog's Name: {dog.name}")
print(f"Dog's Age: {dog.get_age()}")  # Encapsulation

dog.set_age(4)  # Updating age
print(f"Updated Dog's Age: {dog.get_age()}")

print()

print(f"Cat's Name: {cat.name}")
print(f"Cat's Age: {cat.get_age()}")  # Encapsulation

print()

# Polymorphism in action
animal_sound(dog)
animal_sound(cat)
