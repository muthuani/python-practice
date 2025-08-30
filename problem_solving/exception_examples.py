#Create a program to make your own exception class
x = float(input('Enter a number : '))
y = float(input('Enter value by which you want to divide the number : '))
result=0
try:
    result = x/y
except ZeroDivisionError:
    print("There is a divide by zero error")

print(result)