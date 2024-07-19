#Recursive Function
"""def is_prime(n, divisor=2):
    if n <= 1:
        return False

    if divisor >= n:
        return True

    if n % divisor == 0:
        return False

    return is_prime(n, divisor + 1)

user_input = input("Enter number: ")

if user_input.isdigit():
    if is_prime(int(user_input)):
        print(f"{user_input} is prime.")
    else:
        print(f"{user_input} in not prime.")
"""
#Simple Function

def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

user_input = input("Enter number: ")

if user_input.isdigit():
    if isPrime(int(user_input)):
        print(f"{user_input} is prime.")
    else:
        print(f"{user_input} in not prime.")
