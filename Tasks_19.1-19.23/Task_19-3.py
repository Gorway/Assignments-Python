# Create a function apply_twice(f, x) that applies a given function f to an argument x two times.

def square(n):
  return n * n

def apply_twice(f, x):
    def apply1():
        nonlocal x
        x = f(x)  
        def apply2():
            nonlocal x
            x = f(x) 
        apply2()  
        return x 
    return apply1

print(apply_twice(square, 2)())