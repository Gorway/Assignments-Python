# Create a generator exception_propagator(iterable) that yields each item in iterable. If an item is "error", raise a ValueError exception with the message “An error occurred!“. Test this generator with a list containing the string "error".

def exception_propagator(iterable):
  for item in iterable:
    if item == 'error':
      raise ValueError("An error occurred!")
    yield item

strings = ['Python','Odyssey','error']

gen = exception_propagator(strings)

# print(next(gen))
# print(next(gen))
# print(next(gen))

try:
  for item in gen:
    print(item)
except ValueError as e:
  print(e)