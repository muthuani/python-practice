# Program to Calculate Factorial Value By Using Recursion Function

#Function created to calculate factorial of a number
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)


#Accepting nth number from user to calculate factorial
a=int(input("Please Enter number to calculate factorial : "))
#calling function
fact=factorial(a)
print(f"Factorial of {a} is : {fact}")