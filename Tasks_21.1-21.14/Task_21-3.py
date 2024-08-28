# Implement an infinite generator function infinite_sequence() that yields numbers starting from 1 and increments by 1 indefinitely. Use next() to retrieve and print the first 10 numbers from this generator.

def infinite_sequence(): 
  n = 1
  while True:
    yield n 
    n += 1

x = infinite_sequence()
for _ in range(10):
  print(next(x))