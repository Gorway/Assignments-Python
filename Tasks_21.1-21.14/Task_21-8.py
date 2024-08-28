# Use a generator expression to filter and yield only even numbers from a list of numbers. Test this generator with a list of integers from 1 to 50.

numbers = [n for n in range(1, 51)]

even_numbers = (num for num in numbers if num % 2 == 0)

for number in even_numbers:
  print(number, end=' ')