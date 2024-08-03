# Store functions for string manipulations (such as uppercase, lowercase, title case, and reversing a string) in a dictionary. Write a function manipulate_string(s, operation) that takes a string and an operation name, and uses the dictionary to perform the requested string manipulation.

def upper(string=''):
  return string.upper()

def lower(string=''):
  return string.lower()

def capit(string=''):
  return string.capitalize()

def rev(string=''):
  return string[::-1]

string_manipulations = {
  'uppercase': upper,
  'lowercase': lower,
  'capitalize': capit,
  'reverse': rev 
}

def manipulate_string(s, operation):
  if operation in string_manipulations:
    print(string_manipulations[operation](s))
    

some_string = "python"

manipulate_string(some_string, 'reverse')