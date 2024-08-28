# Write a generator function custom_reduce(func, iterable, initializer=None) that mimics the behavior of functools.reduce(). It should yield intermediate results of applying func cumulatively to the items of iterable, optionally starting with initializer. Test this function with a list of numbers and a lambda function that adds two numbers.

def custom_reduce(func, iterable, initializer=None):
  if initializer != None:
    result = initializer
    for item in iterable:
      result = func(result, item)
    yield result
  else:
    if not iterable:
      raise ValueError("Iterable is empty")
    it = iter(iterable)
    result = next(it)

    for item in iterable:
      result = func(result, item)
    yield result
    
numbers = [1, 2, 3, 4, 5]

def multiply(x, y):
    return x * y
  
result = custom_reduce(multiply, numbers, initializer=10)
print(next(result))