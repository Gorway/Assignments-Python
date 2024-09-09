# Modify the Person class to make the age attribute private. Provide a method to get the age (get_age) and another method to set the age (set_age) with

class Person:
  def __init__(self, name='', age=0):
    self.name = name
    self.__age = age
  
  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      raise ValueError("Enter positiv number.")

  def get_age(self):
    return self.__age
  
p1 = Person('Bob')
p1.set_age(52)
print(p1.get_age())