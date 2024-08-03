#Create a dictionary-based calculator where each arithmetic operation (addition, subtraction, multiplication, division) is a function stored in a dictionary. Write a function calculate(operand1, operand2, operator) that uses this dictionary to perform the requested operation.

def get_input(num):
  while True:
    user_input = input(num)
    try:
      return int(user_input)
    except ValueError:
      try:
        return float(user_input)
      except ValueError:
        print("Invalid input. Please enter a valid number.")

operations = {
  '+': lambda x, y: x + y,
  '-': lambda x, y: x - y,
  '*': lambda x, y: x * y,
  '/': lambda x, y: x / y if y != 0 else "Сannot be divided by zero"
}

op = input("Enter calculator operation (+, -, *, /): ")
operand1 = get_input("Enter operand1: ")
operand2 = get_input("Enter operand2: ")

if op in operations:
  result = operations[op](operand1, operand2)
  print(f"Result: {result}")
else:
  raise ValueError("Invalid operation")