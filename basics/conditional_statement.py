# All Types of Conditional Statements in Python

# 1. Simple if statement
age = 18
if age >= 18:
    print("[IF] You are an adult.")

# 2. if-else statement
age = 16
if age >= 18:
    print("[IF-ELSE] You are an adult.")
else:
    print("[IF-ELSE] You are a minor.")

# 3. if-elif-else statement
marks = 75
if marks >= 90:
    print("[IF-ELIF-ELSE] Grade A")
elif marks >= 70:
    print("[IF-ELIF-ELSE] Grade B")
elif marks >= 50:
    print("[IF-ELIF-ELSE] Grade C")
else:
    print("[IF-ELIF-ELSE] Fail")

# 4. Nested if statement
num = 15
if num > 0:
    if num % 2 == 0:
        print("[NESTED IF] Positive even number")
    else:
        print("[NESTED IF] Positive odd number")

# 5. Ternary conditional expression
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"[TERNARY] Status: {status}")

# 6. Conditional with logical operators
age = 25
has_id = True
if age >= 18 and has_id:
    print("[LOGICAL] You can enter.")
else:
    print("[LOGICAL] Entry denied.")

# 7. Conditional with membership operators
fruits = ["apple", "banana", "mango"]
if "apple" in fruits:
    print("[MEMBERSHIP] Apple is available")
else:
    print("[MEMBERSHIP] Apple is not available")

# 8. Conditional with identity operators
x = None
if x is None:
    print("[IDENTITY] x is None")
else:
    print("[IDENTITY] x has a value")

# 9. Match-Case statement (Python 3.10+)
day = "Monday"
match day:
    case "Monday":
        print("[MATCH-CASE] Start of the week")
    case "Friday":
        print("[MATCH-CASE] Weekend is coming!")
    case _:
        print("[MATCH-CASE] Just another day")
