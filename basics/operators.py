# Python Operators Concepts

# 1. Arithmetic Operators
print("--- Arithmetic Operators ---")
a = 10
b = 3
print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division (float)
print("a % b =", a % b)   # Modulus
print("a // b =", a // b) # Floor Division
print("a ** b =", a ** b) # Exponentiation

# 2. Comparison Operators
print("\n--- Comparison Operators ---")
x = 5
y = 10
print("x == y:", x == y)   # Equal
print("x != y:", x != y)   # Not equal
print("x > y:", x > y)     # Greater than
print("x < y:", x < y)     # Less than
print("x >= y:", x >= y)   # Greater than or equal
print("x <= y:", x <= y)   # Less than or equal

# 3. Logical Operators
print("\n--- Logical Operators ---")
p = True
q = False
print("p and q:", p and q) # Logical AND
print("p or q:", p or q)   # Logical OR
print("not p:", not p)     # Logical NOT

# 4. Assignment Operators
print("\n--- Assignment Operators ---")
a = 10
b = 5
a += b  # a = a + b
print("a += b ->", a)
a -= b  # a = a - b
print("a -= b ->", a)
a *= b  # a = a * b
print("a *= b ->", a)
a /= b  # a = a / b
print("a /= b ->", a)
a %= b  # a = a % b
print("a %= b ->", a)
a **= b # a = a ** b
print("a **= b ->", a)
a //= b # a = a // b
print("a //= b ->", a)

# 5. Bitwise Operators
print("\n--- Bitwise Operators ---")
x = 10  # 1010 in binary
y = 4   # 0100 in binary
print("x & y:", x & y)  # AND
print("x | y:", x | y)  # OR
print("x ^ y:", x ^ y)  # XOR
print("~x:", ~x)        # NOT
print("x << 2:", x << 2) # Left shift
print("x >> 2:", x >> 2) # Right shift

# 6. Identity Operators
print("\n--- Identity Operators ---")
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a is b:", a is b)   # True, same object
print("a is c:", a is c)   # False, different object
print("a is not c:", a is not c) # True

# 7. Membership Operators
print("\n--- Membership Operators ---")
fruits = ["apple", "banana", "mango"]
print("'apple' in fruits:", 'apple' in fruits)       # True
print("'orange' not in fruits:", 'orange' not in fruits) # True
