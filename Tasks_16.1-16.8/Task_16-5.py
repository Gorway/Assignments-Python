def display_product(name, model, color):
  result = f"Product details:\nName: {name}\nModel: {model}\nColor: {color}"

  return result

product = {"Name": "Beko", "Model": "ZT109", "Color": "Silver"}

result = display_product(**product)

print(result)



"""
def display_product(**product):
  name =  product['Name']
  model = product['Model']
  color = product['Color']

  result = f"Product Description\nName: {name}\nModel: {model}\nColor: {color}"

  return result

product = {"Name": "Beko", "Model": "ZT109", "Color": "Silver"}
result = display_product(**product)
print(result)
"""