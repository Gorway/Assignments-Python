def iteration(iterable):
  it = iter(iterable) 
  while True:
    try:
      print(next(it))
    except StopIteration:
      break

numbers = [x for x in range(11)]

iteration(numbers)