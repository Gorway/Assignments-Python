def process_data(*data, operation=sum):
  if operation == sum:
    result = sum(data)
  elif operation == max:
    result = max(data)
  else:
    raise ValueError(f"Error , operation {operation} is not foun")
  
  return result

data = [123, 33]
sum_of_data= process_data(*data)
print(f"Sum of data {data} = {sum_of_data}")
find_max = process_data(*data, operation=max)
print(f"Max value data {data} is {find_max}")