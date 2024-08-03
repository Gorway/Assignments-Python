#Implement a function make_greeting(greeting) that takes a greeting string and returns a function that takes a name and prints the greeting followed by the name.

def make_greeting(greeting_massage):
  def greeting(name=''):
    if name == '':
      raise ValueError("Enter name.")
    return f"{greeting_massage} {name}."
  return greeting

greeting_message = "Hello Dear"
greeting_function = make_greeting(greeting_message)
name = "Arkadik"
print(greeting_function(name))