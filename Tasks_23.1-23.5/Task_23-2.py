#Design a class Book with private attributes title, author, and price. Create methods to set and get the values of these attributes. Ensure that the price cannot be set below a certain value (e.g., 10).

class Book:
  def __init__(self,*, title, author, price):
    self.__title = title
    self.__author = author
    self.__price = price if price >= 10 else 10
    
  def set_title(self, title):
    self.__title = title
  
  def set_author(self, author):
    self.__author = author
    
  def set_price(self, price):
    if price >= 10:
      self.__price = price
    else:
      raise ValueError("The price cannot be set below a certain value (10)")
  
  def get_title(self):
    return self.__title
  
  def get_author(self):
    return self.__author
  
  def get_price(self):
    return self.__price
    
    
b = Book(title='The Castle', author='Kafka', price=12)
print(b.get_title())