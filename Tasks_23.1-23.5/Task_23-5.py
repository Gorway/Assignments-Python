#Design a class Product with private attributes product_id, product_name, and quantity_in_stock. Implement methods to set and get the values of these attributes and to adjust the quantity_in_stock (e.g., adding stock or reducing stock).

class Product:
  def __init__(self):
    self.__storage = {}

  def set_product(self, product_id, product_name, quantity_in_stock):
    if product_id not in self.__storage:
      self.__storage[product_id] = {
        'product_name': product_name,
        'quantity_in_stock': quantity_in_stock
      }
    else:
      print(f"Product with ID {product_id} already exist.")
  
  def get_product(self, product_id):
    return self.__storage.get(product_id)
  
  def adjust_quantity(self, product_id, new_quantity):
    product = self.__storage.get(product_id)
    if product:
      updated_quantity = product['quantity_in_stock'] + new_quantity
      if updated_quantity >= 0:
        product['quantity_in_stock'] = updated_quantity
      else:
        raise ValueError("Quantity  has reached 0.")
    else:
      print("Product not found.")
  
  def display_priducts(self):
    if not self.__storage:
      print("Storage is empty")
    else:
      for product_id, info in self.__storage.items():
        print(f"ID: {product_id}\nName: {info['product_name']}\nQuantity in stock: {info['quantity_in_stock']}")

p = Product()
p.set_product(10111, 'Book', 45)
p.display_priducts()
p.adjust_quantity(10111,6555)
p.display_priducts()
p.adjust_quantity(10111,-4444)
p.display_priducts()