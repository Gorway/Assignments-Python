# Implement a function make_memoize(f) that takes a function f and returns a memoized version of f which caches results to avoid redundant computations.
import time

def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

def make_memorize(f):
  cache = {}
    
  def memorized_f(*args):
    if args in cache:
      print("Cache Hit!")
      return cache[args]
    print("Cache Miss!")    
    start = time.time()
    result = f(*args)
    cache[args] = result
    print(f"Memorized function execution time: {time.time() - start}")
    return result
    
  return memorized_f

start = time.time()
result = fibonacci(33)
print(f"Result of calculating Fibonacci number: {result}")
print(f"Function Fibonacci execution time (without memorization): {time.time() - start}")

memorized_fibonacci = make_memorize(fibonacci)

start = time.time()
result = memorized_fibonacci(33)
print(f"Result of calculating Fibonacci number with memorization: {result} ")
print(f"Memorized function execution time (first call): {time.time() - start}")

start = time.time()
result = memorized_fibonacci(33)
print(f"Result of calculating Fibonacci number with memorization (second call with same argument): {result}")
print(f"Memorized function execution time (second call): {time.time() - start} ")

start = time.time()
result = memorized_fibonacci(34)
print(f"Result of calculating Fibonacci number with memorization (third call with different argument): {result}")
print(f"Memorized function execution time (second): {time.time() - start} ")

