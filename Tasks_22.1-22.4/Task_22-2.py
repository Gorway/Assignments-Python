# Extend the Person class by adding an __init__ constructor method that initializes name and age when an object is created. Ensure the method uses self to assign the values.

class Persnon:
  def __init__(self,*, name, age):
    self.name = name
    self.age = age
    
  def display_info(self):
    print(f"Name: {self.name}\nAge: {self.age}")
    
p1 = Persnon(name='Bob', age=23)    
p1.display_info()