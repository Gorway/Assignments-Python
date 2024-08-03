# Write a function compose(f, g) that returns a new function which is the composition of the functions f and g.

def make_unique(arg):
  return set(arg)

def make_muttable(arg):
  return list(arg)
    
def x2_elements(args):
  for i in range(len(args)):
    args[i] *= 2
  return args
  
def compose(make_unique, make_muttable, x2_elements):
  def _composition(n=0):
    if n!= 0:
      n = x2_elements(make_muttable(make_unique(n)))
    else:
      raise ValueError("Enter immutable and iterable type argument.")
    return n
  return _composition

immutable_nums = (1, 1, 2, 2, 3, 4, 5, 5, 2, 1)
compose_function = compose(make_unique, make_muttable, x2_elements)
result  = compose_function(immutable_nums)
print(f"Tuple of nums berfor changes: {immutable_nums}.")
print(f"After making tuple to list , removing duplicate elements and multiply by 2: {result}")