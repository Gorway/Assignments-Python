def calculate_total_price(item1,item2,item3, /, tax_rate = 0.5):
  item_sum = item1 + item2 + item3
  total_price = item_sum + (1 * tax_rate)
  return total_price


item_prices = [155.99, 65.7, 889.50]
tax_rate = 0.24

total_price = calculate_total_price(*item_prices, tax_rate = tax_rate)
print(f"Total price included taxes ({tax_rate}): {total_price}")