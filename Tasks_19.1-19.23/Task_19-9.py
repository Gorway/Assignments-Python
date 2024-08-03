#Write a function make_accumulator(start=0) that returns a function which adds its argument to start and returns the new total each time it is called.

def make_accumulator(start=0):
  def accumulator():
    nonlocal start;
    start += 1 
    return start
  return accumulator

total_count = make_accumulator()
total = total_count()
total = total_count()
total = total_count()
total = total_count()

print(total)