#Create a decorator that adds retry logic to a function. The decorator should retry the function a specified number of times if it raises an exception. Apply this decorator to a function that reads data from a file.

def repeat(n_times):
  def decorator(fn):
    def wrapper(*args,**kwargs):
      exeption = None
      for test in range(n_times):
        try:
          return fn(*args, **kwargs)
        except Exception as exc:
          exeption = exc
          print(f"Test {test + 1} failed: {exc}")
      raise exeption
    return wrapper
  return decorator

@repeat(15)
def file_read(fileName):
  file = open(fileName, 'r')
  content = file.read()
  file.close()
  return content

try:
  file_read("example.txt")
except Exception as exc:
  print(f"CAn't read file: {exc}")