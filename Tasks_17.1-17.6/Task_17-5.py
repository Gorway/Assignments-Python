def get_nth_element(iterable, element_index):
  it = iter(iterable)
  start = 0
  while start < element_index:
    try:
      nth_element = next(it)
      start += 1
    except StopIteration:
      break
  return nth_element

numbers = [ x**2 for x in range(11)]
print(numbers)
res = get_nth_element(numbers, element_index=5)
print(res)