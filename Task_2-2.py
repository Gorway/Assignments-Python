def func(x, y):
    result = (x + y) / (x - y)
    return result


num1 = float(input("Enter x value: "))
num2 = float(input("Enter y value: "))

print("Result of (x+y) / (x-y): ",func(num1, num2))