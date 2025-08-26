# Python Data Types and Type Casting Example

# Different types of variables in Python

# Integer
age = 25
print("Age:", age, "Type:", type(age))  # type() shows the data type

# Float
height = 1.75
print("Height:", height, "Type:", type(height))

# String
name = "Raj"
print("Name:", name, "Type:", type(name))

# Boolean
is_student = True
print("Is student?", is_student, "Type:", type(is_student))

# Type Casting (converting from one data type to another)

# Integer to Float
age_float = float(age)
print("Age as float:", age_float, "Type:", type(age_float))

# Float to Integer
height_int = int(height)
print("Height as integer:", height_int, "Type:", type(height_int))

# Integer to String
age_str = str(age)
print("Age as string:", age_str, "Type:", type(age_str))

# String to Integer (only works if string contains numbers)
num_str = "100"
num_int = int(num_str)
print("String to integer:", num_int, "Type:", type(num_int))

# String to Float
num_float = float(num_str)
print("String to float:", num_float, "Type:", type(num_float))

# Boolean to Integer
bool_int = int(is_student)  # True becomes 1, False becomes 0
print("Boolean to integer:", bool_int, "Type:", type(bool_int))

# Boolean to String
bool_str = str(is_student)
print("Boolean to string:", bool_str, "Type:", type(bool_str))
