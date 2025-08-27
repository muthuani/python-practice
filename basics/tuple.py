#A Tuple is an ordered collection of items in Python that is immutable, meaning its elements cannot be changed after creation.

# 1. Creating a Tuple
fruits = ("apple", "banana", "mango")
print("Tuple:", fruits)

# 2. Accessing Elements
print("First fruit:", fruits[0])  # Indexing
print("Last fruit:", fruits[-1])  # Negative indexing

# 3. Slicing Tuple
print("First two fruits:", fruits[0:2])

# 4. Tuple with one element
single = (5,)  # comma is necessary
print("Single element tuple:", single)

# 5. Tuple unpacking
a, b, c = fruits
print("Unpacked values:", a, b, c)

# 6. Tuples are immutable
try:
    fruits[0] = "orange"  # This will raise an error
except TypeError as e:
    print("Error:", e)

# 7. Tuple concatenation
more_fruits = fruits + ("orange", "grape")
print("Concatenated tuple:", more_fruits)

# 8. Tuple repetition
print("Repeated tuple:", fruits * 2)

# 9. Checking element in tuple
if "apple" in fruits:
    print("Apple is in the tuple")

# 10. Tuple length
print("Number of fruits:", len(fruits))

# 11. Iterating over tuple
for fruit in fruits:
    print("Fruit:", fruit)

# 12. Tuple Methods
numbers = (1, 2, 3, 2, 4, 2)
print("Count of 2:", numbers.count(2))  # counts occurrences
print("Index of 3:", numbers.index(3))  # returns first index of value

# 13. Methods on single element tuple
print("Count of 5 in single element tuple:", single.count(5))
print("Index of 5 in single element tuple:", single.index(5))
