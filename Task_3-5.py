def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero."
    return x / y


operations = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': divide
}

print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter operation number (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = operations.get(choice)


if operation:
    print("Operation result:", operation(num1, num2))
else:
    print("Invalid input")
