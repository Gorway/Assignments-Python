#Design a class Employee with private attributes employee_id, name, and salary. Provide methods to set and get these values. Ensure that salary cannot be negative.

class Employee:
  def __init__(self, name='', salaray=0):
    self.__name = name
    self.__salary = salaray
  
  def set_name(self, name):
    self.__name = name
  
  def set_salary(self, salary):
    if salary < 0:
      raise ValueError("Enter positiv number")
    self.__salary = salary
  
  def get_name(self):
    return self.__name
  
  def get_salary(self):
    return self.__salary

ob = Employee("Den", 2000)
ob2 = Employee()
ob2.set_name("Bob")
ob2.set_salary(1000)
print(ob.get_name())
print(ob.get_salary())
print(ob2.get_name())
print(ob2.get_salary())