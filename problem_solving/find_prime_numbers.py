# Program to find prime numbers in a range

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # check up to square root
        if num % i == 0:
            return False
    return True

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Prime numbers between {start} and {end}:")
for n in range(start, end + 1):
    if is_prime(n):
        print(n, end=" ")
