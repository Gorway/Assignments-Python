# Create two generators: gen1() yields numbers from 1 to 5, and gen2() uses yield from to yield all values from gen1() and then yields numbers from 6 to 10. Print all values yielded by gen2().

def gen1():
  up_to_5 = 6
  for n in range(1, up_to_5):
    yield n
    
def last_value_from_gen(generator):
    last_value = 0
    for value in generator:
        last_value = value
    return last_value

def gen2():
  last_value = last_value_from_gen(gen1())
  yield from gen1()
  
  up_to_10 = 11
  for i in range(last_value +1 , up_to_10):
    yield i

test = gen2()
for num in test:
  print(num, end=' ')