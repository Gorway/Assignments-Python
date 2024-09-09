#Create a class Student with private attributes name, roll_number, and grades. Implement methods to add grades, calculate the average grade, and display the student’s information. Ensure that the grades are between 0 and 100.

class Student:
  def __init__(self, roll_number):
    self.__roll_number = roll_number
    self.__grades = []

  def add_grade(self, *grades):
    for grade in grades: 
      if 0 <= grade <= 100:
        self.__grades.append(grade)
      else:
        raise ValueError("Grade must be between 0 and 100.")

  def calculate_average(self):
    if self.__grades:
      return sum(self.__grades) / len(self.__grades)
    return 0

  def get_roll_number(self):
    return self.__roll_number

  def get_grades(self):
    return self.__grades

class StudentManager:
  def __init__(self):
    self.__students = {}

  def add_student(self, name, roll_number):
    if name not in self.__students:
      self.__students[name] = Student(roll_number)
    else:
      raise ValueError("Student with this name already exists.")

  def add_grade(self, name, *grades):
    if name in self.__students:
      self.__students[name].add_grade(*grades)
    else:
      raise ValueError("Student not found.")

  def display_student_information(self, name):
    if name in self.__students:
      student = self.__students[name]
      avg_grade = student.calculate_average()
      print(f"Name: {name}")
      print(f"Roll Number: {student.get_roll_number()}")
      print(f"Grades: {student.get_grades()}")
      print(f"Average Grade: {avg_grade}")
    else:
      print("Student not found.")

manager = StudentManager()
manager.add_student(name='Poghos', roll_number='123')
manager.add_grade("Poghos", 75, 73,99,32)
manager.display_student_information("Poghos")