# Create a dictionary with functions to calculate the area of different geometric shapes (circle, square, rectangle, triangle). Write a function calculate_area(shape, **kwargs) that uses this dictionary to calculate the area based on the provided shape and parameters.

import math

calculate_geometric_functions = {
  "circle": lambda radius: math.pi * radius ** 2,
  "triangle": lambda base, height: 0.5 * base * height,
  "square": lambda side: side ** 2,
  "rectangle": lambda width, height: height * width
}

def calculate_area(shape, **kwargs):
  if shape in calculate_geometric_functions:
    return calculate_geometric_functions[shape](**kwargs)

x = calculate_area("circle", radius=5)
print(x)