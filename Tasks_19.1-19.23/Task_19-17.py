# Store functions for converting temperatures between Celsius, Fahrenheit, and Kelvin in a dictionary. Write a function convert_temperature(value, from_unit, to_unit) that uses this dictionary to perform the conversion.

def make_celsius(value, unit):
  if unit == "Fahrenheit":
    return (value - 32) * 5 // 9
  elif unit == "Kelvin":
    return value - 273.15
  else:
    raise ValueError("Unknown unit")

def make_fahrenheit(value, unit):
  if unit == "Celsius":
    return value * 9 // 5 + 32
  elif unit == "Kelvin":
    return (value - 273.15) * 9 // 5 + 32
  else:
    raise ValueError("Unknown unit")
  
def make_kelvin(value, unit):
  if unit == "Celsius":
    return value + 273.15
  elif unit == "Fahrenheit":
    return (value - 32) * 5 // 9 + 273.15
  else:
    raise ValueError("Unknown unit")

convert_functions = {
  "Celsius": make_celsius,
  "Fahrenheit": make_fahrenheit,
  "Kelvin": make_kelvin
}

def convert_temperatures(value, from_unit, to_unit):
  if from_unit == to_unit:
    return value
  
  if from_unit in convert_functions:
    result = convert_functions[to_unit](value, from_unit)
    return result
  else:
    raise ValueError("Unkonw type temperature unit.")
  
print(convert_temperatures(97, "Fahrenheit", "Celsius"))