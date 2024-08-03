# Implement a function power_factory(n) that returns a function which raises its argument to the power of n.

def power_factory(n):
  def power_by(x):
    return x ** n
  return power_by

n = 2 

fn = power_factory(n)
print(fn(6))