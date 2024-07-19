def isPowerOfTwo(n):

    if n <= 0:
        return False

    return (n & (n - 1)) == 0

def printPowersOfTwo():

    print("The first ten powers of 2:")

    print("-" * 10)

    for i in range(10):
        print(f"2^{i:<2} = {2 ** i:>3,}")

    print()

user_input = int(input("Enter a positive number to determine if it is a power of 2: "))

if user_input < 0:

    raise ValueError(f"\nError: {user_input} is not a positive number. Please enter a positive number.")
elif isPowerOfTwo(user_input):

    print(f"\nCorrect! {user_input} is a power of two.\n")

    printPowersOfTwo()
else:

    print(f"\nWrong! {user_input} is not a power of 2.\n")

