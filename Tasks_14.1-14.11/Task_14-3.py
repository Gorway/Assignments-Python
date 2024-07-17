def factrorial(n):
    if n == 1:
        return 1
    return n * factrorial(n - 1)

user_input = input("Enter number to calculate factorial: ")
if user_input.isdigit:
    result = factrorial(int(user_input))
    print(f"{user_input}! = {result}")
