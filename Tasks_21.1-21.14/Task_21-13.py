# Create a generator function custom_filter(func, iterable) that mimics the behavior of the built-in filter() function. It should yield items from iterable where func(item) returns True. Test this function with a list of integers and a lambda function that checks if the number is even.

def custom_filter(func, iterable):
  if callable(func):
    for item in iterable:
      if func(item):
        yield item

result = custom_filter(lambda x: x % 2 == 0, [x for x in range(20)])
for i in result:
  print(i, end=' ')