# Implement a generator function custom_range(start, end, step) that mimics Python’s built-in range() function but can accept a float step. Use this generator to print numbers from 0 to 5 with a step of 0.5.

def custom_range(start, end, step):
  if step == 0:
    return
  if step > 0:
    while start < end:
      yield start
      start += step
  else:
    while start > end:
      yield start
      start += step
  

fn = custom_range( 1, 5 , 0.5 )
for i in fn:
  print(i)