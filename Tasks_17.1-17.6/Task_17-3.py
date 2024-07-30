#Built-in zip() function custom implementation.

def custom_zip(*iterables, strict=False) -> tuple:
  """
  
  Parameters:
  *iterables: One or more iterables to be zipped together.
  strict: If True, all iterables must have the same length; otherwise, the shortest iterable length is used.

  Returns:
  Tuple: A tuple of tuples, where each inner tuple contains elements from corresponding positions of the input iterables.
  Raises:
  ValueError: If {strict} is True and the iterables have different lengths.
  
  """
  if strict:
    length = len(iterables[0])
    for it in iterables:
      if len(it) != length:
        raise ValueError("In strict mode all iterables must have same length.")
    result = [tuple(it[i] for it in iterables) for i in range(length)]
  else:
    min_lenght = min(len(it) for it in iterables)  
    
    result = []
    
    for i in range(min_lenght):
      result.append(tuple(it[i] for it in iterables))
    
  return tuple(result)

result = (custom_zip("Picsart", range(7), strict=True))
print(result)
