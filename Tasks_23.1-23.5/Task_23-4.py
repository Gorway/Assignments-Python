# Design a class ShoppingCart that encapsulates a private list of items (items). Implement methods to add an item, remove an item, and display the total number of items in the cart. Each item should have a name and price.

class ShoppingCart:
  def __init__(self):
    self.__cart = []
  
  def add_item(self, name, price):
    self.__cart.append((name, price))
  
  #def remove_item(self, name):
    #self.__cart = list(filter(lambda item: item[0] != name, self.__cart))
  
  def remove_item(self, name):
    for item in self.__cart:
      if item[0] == name:
        self.__cart.remove(item)
  
  def total_number(self):
    return len(self.__cart)
  
  def display_cart(self):
    for item in self.__cart:
        print(f"Name: {item[0]}\nPrice: {item[1]}")

ob = ShoppingCart()
ob.add_item('Water', 5)
ob.add_item('Oil', 51)
ob.add_item('Tomato', 65)
total = ob.total_number()
print(total)
ob.display_cart()
ob.remove_item("Oil")
print()
ob.display_cart()
