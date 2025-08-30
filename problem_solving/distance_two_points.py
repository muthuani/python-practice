import math   # for square root



# 1. Void function to compute and display power of a number
def power_void(base, exponent):
    result = base ** exponent
    print(f"{base} raised to the power {exponent} is {result}")

# 2. Fruitful function to compute and return power of a number
def power_fruitful(base, exponent):
    return base ** exponent

# 3. Function to display the distance between two points in XY plane (void)
def distance_void(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"Distance between points ({x1},{y1}) and ({x2},{y2}) is {distance:.2f}")

# 4. Script to display the distance between two points in XY plane
x1, y1 = 0, 0
x2, y2 = 3, 4
print("\nScript to display distance between two points")
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance between ({x1},{y1}) and ({x2},{y2}) is {distance:.2f}")

# 5. Script using void function
print("\nScript using void function for distance")
distance_void(0, 0, 3, 4)

# 6. Script using fruitful function
def distance_fruitful(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("\nScript using fruitful function for distance")
d = distance_fruitful(0, 0, 3, 4)
print(f"Distance between (0,0) and (3,4) is {d:.2f}")

# --- Running sample tasks ---
print("\nRunning sample tasks...")


power_void(2, 5)
print("Fruitful power:", power_fruitful(3, 4))
distance_void(1, 2, 4, 6)
