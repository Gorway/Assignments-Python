# Implement a function make_config(key, value) that returns a function which, when called, returns a dictionary with the given key-value pair.

def make_config(key, value):
  def config():
      res = {}
      res[key] = value # or return {key: vvalue}
      return res
  return config

fn = make_config("Picsart", "Academy")
res = fn()
print(res)