def make_counter():
  count = 0
  def counter():
    nonlocal count
    count += 1
    print(count)
    return count
  return counter
  
function = make_counter()

function()
function()
function()
print(function.__name__)
print(function.__closure__)
print(function.__code__.co_freevars)