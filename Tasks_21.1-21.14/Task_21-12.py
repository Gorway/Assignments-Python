# Develop a generator function custom_zip(*iterables) that mimics the behavior of the built-in zip() function. It should yield tuples containing items from each iterable passed as arguments, stopping when the shortest iterable is exhausted. Test your generator with two or more lists of different lengths.


def custom_zip(*iterables):
  iterable = [item for item in iterables]
  
  minimal_length = min([len(it) for it in iterables])
  
  for i in range(minimal_length):
    yield tuple(iterable[i] for iterable in iterables)
    
ls1 =  [1, 3, 5]
ls2 =  ['Python', 'Odyssey', "Academy"]
ls3 =  [2, 4, 6, 7]

result = custom_zip(ls1, ls2, ls3)
print(next(result))
print(next(result))
print(next(result))