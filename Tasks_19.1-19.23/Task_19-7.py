# Use the filter function with a lambda to filter out all even numbers from a list.

ls = [x for x in range(1, 21)]

result = tuple(filter(lambda x: x % 2 == 0, ls))
print(result)