# Write a function make_adder(n) that returns a function that adds n to its argument.

def make_adder_for(n):
  def adder(x):
    return x + n
  return adder

n = 665
x = 1
add_x_to_n = make_adder_for(n)
n = add_x_to_n(x)
print(n)