# Create a generator function fibonacci_generator(n) that yields the first n Fibonacci numbers. Test your generator by printing all numbers yielded by it.

def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_generator(*n):
  for i in n:
    yield fibonacci(i)

# x = fibonacci_generator(*num)
# print(next(x))
# print(next(x))
# print(next(x))

num = [x for x in range(0,15)]
for num in fibonacci_generator(*num):
  print(num, end='')
