#Buit-in filter() function custom implementation.

def isEven(number: int) -> bool:
  """Checks if a number is even, return boolean."""
  return number % 2 == 0

def custom_filter(function: callable, iterable: list) -> list:
  """
  Applies a function to each item of an iterable and returns a list of elements
  for which the function returns True.

  Parameters:
  function: A function that takes a single argument and returns a boolean value.
  iterable: An iterable containing elements to be filtered.

  Returns:
  List: A list of elements for which the function returned True.

  Raises:
  ValueError: If the {function} argument is not callable or the {iterable} argument is not iterable.
  
  """
  if callable(function):
    result = []
    for item in iterable:
      if function(item):
        result.append(item)
  else:
    raise ValueError("Enter valid function and iterable type argument. ")     
  return result

numbers = [x for x in range(1,11)]
even_numbers = custom_filter(isEven, numbers)
print(f"Even numbers of list: {numbers} is {even_numbers}")
