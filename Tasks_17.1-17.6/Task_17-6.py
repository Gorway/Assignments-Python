def square(x):
  return x**2

def apply_function(function, iterable):
  it = iter(iterable)
  res = []
  
  while True:
    try:
      res.append(function(next(it)))
    except StopIteration:
      break
  return res

numbers = (x for x in range(5))
res = apply_function(square, numbers)
print(res)