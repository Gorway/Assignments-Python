#Write a Python class named Person that has attributes for name and age. Include a method to display the person’s details.

class Persnon:
  name = 'Bob'
  age = 30
  
  def display_info(self):
    print(f"Name: {self.name}\nAge: {self.age}")
    
p1 = Persnon()    
p1.display_info()