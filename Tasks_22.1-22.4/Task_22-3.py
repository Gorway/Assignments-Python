# Add a method to the Person class called greet that prints a greeting message including the person’s name.


class Persnon:
  def __init__(self,*, name, age):
    self.name = name
    self.age = age
    
  def display_info(self):
    print("Personal information.")
    print(f"Name: {self.name}\nAge: {self.age}")
    
  def greet(self):
    print(f"Hello {self.name}.")
    
p1 = Persnon(name='Bob', age=23)    
p1.greet()
p1.display_info()