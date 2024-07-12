def print_nums(n):
    if n < 0:
        print("Please enter positive number.")
    for i in range(n, -1, -1):
        print(i)

user_input = input("Enter positiv number: ")

print_nums(int(user_input))
