#Write a function bar(n) that returns a list of functions. Each function should be created by a nested closure and should multiply its argument by the corresponding index. Verify the closures by inspecting their __closure__ attributes.

def bar(n):
  def make_function(index):
    def func(x):
      return x * index
    return func
  functions_list = [make_function(i) for i in range(n)]

  return functions_list

func_list = bar(3)

for i, func in enumerate(func_list):
    print(f"Function {i} result with argument 10: {func(6)}")

for func in func_list:
  print(func.__closure__)