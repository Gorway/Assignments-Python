# Create a generator function repeat_element(element, times) that yields the given element a specified number of times. Test this generator with different inputs.


def repeat_element(element, times):
  for i in range(times):
    yield element

number_generator = repeat_element(10, 5)
for element in number_generator:
  print(element, end=' ')

print('')

list_generator = repeat_element(["Python", "Odyssey"], 3)
for element in list_generator:
  print(element)