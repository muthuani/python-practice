# All Types of Loops in Python

# 1. For Loop
print("--- For Loop Example ---")
for i in range(5):  # range(5) generates numbers 0 to 4
    print("For loop iteration:", i)

# 2. While Loop
print("\n--- While Loop Example ---")
count = 0
while count < 5:
    print("While loop count:", count)
    count += 1

# 3. Break Statement
print("\n--- Break Statement Example ---")
for num in range(10):
    if num == 5:
        print("Breaking at num =", num)
        break  # exit the loop when num = 5
    print(num)

# 4. Continue Statement
print("\n--- Continue Statement Example ---")
for num in range(10):
    if num % 2 == 0:
        continue  # skip even numbers
    print("Odd number:", num)

# 5. Pass Statement
print("\n--- Pass Statement Example ---")
for num in range(5):
    if num == 3:
        pass  # placeholder, does nothing
        print("Pass executed at num =", num)
    else:
        print("Number:", num)
