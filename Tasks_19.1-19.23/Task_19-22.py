# Create a dictionary with various math functions (e.g., square, cube, square root, factorial). Write a function math_operations(number, operation) that uses this dictionary to apply the requested math function to a number.

def square(num):
  return num ** 2

def cube(num):
  return num ** 3

def square_root(num):
  return num ** 0.5

def factorial(num):
  if num <= 1:
    return 1
  return num * factorial(num -1)

Operations = {
  "Square": square,
  'Cube': cube,
  "Square root": square_root,
  'Factorial': factorial
}

def math_operation(number, operation):
  if operation in Operations:
    return Operations[operation](number)
  else:
    raise ValueError("Operation not found.")

result = math_operation(64, 'Square root')
print(result)