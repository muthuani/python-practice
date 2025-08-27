# Python Set Concepts with Examples

# Sets are unordered collections of unique elements

# 1. Creating a Set
fruits = {"apple", "banana", "mango"}
print("Set:", fruits)

# 2. Adding Elements
fruits.add("orange")
print("After adding orange:", fruits)

# 3. Removing Elements
fruits.remove("banana")  # raises KeyError if element not found
print("After removing banana:", fruits)

fruits.discard("grape")  # does not raise error if element not found
print("After discard grape:", fruits)

# 4. Clearing a Set
# fruits.clear()
# print("After clearing:", fruits)

# 5. Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union (A|B):", A | B)
print("Intersection (A&B):", A & B)
print("Difference A-B:", A - B)
print("Difference B-A:", B - A)
print("Symmetric Difference (A^B):", A ^ B)

# 6. Set Methods
print("Union using method:", A.union(B))
print("Intersection using method:", A.intersection(B))
print("Difference using method A-B:", A.difference(B))
print("Difference using method B-A:", B.difference(A))
print("Symmetric Difference using method:", A.symmetric_difference(B))
print("Is A subset of B?:", A.issubset(B))
print("Is A superset of B?:", A.issuperset(B))

# 7. Checking Membership
if 3 in A:
    print("3 is in set A")

# 8. Iterating over a Set
for fruit in fruits:
    print("Fruit:", fruit)

# 9. Set Length
print("Number of elements in set:", len(fruits))

# 10. Set with Mixed Data Types
mixed_set = {1, "apple", 3.14, (2, 3)}
print("Mixed set:", mixed_set)

# 11. Frozen Set (immutable set)
frozen = frozenset([1, 2, 3])
print("Frozen set:", frozen)
# frozen.add(4)  # This will raise an error
