# Use the map function with a lambda to square all elements in a list.

ls = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * x, ls ))
print(result)