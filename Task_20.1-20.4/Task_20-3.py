# Create a decorator that validates the input arguments of a function (e.g., ensures all arguments are positive integers). Apply this decorator to a function that performs mathematical operations.

def make_validator(fn):
  def validator(*args, **kwargs):
    for arg in args:
      if not isinstance(arg, int) or arg < 0:
        raise ValueError("Enter only positiv natural number!")
    result = fn(*args)
    return result
  return validator

@make_validator
def add(x, y):
  return x + y

print(add(7.5, 2))