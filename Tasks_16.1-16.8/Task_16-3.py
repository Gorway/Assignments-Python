def print_user_profile(first_name,last_name, *, city, age):
  profile = f"Name: {first_name} {last_name}\nAge:{age}\nCity: {city}"
  return profile

result = print_user_profile("David", "Shaw", city="London", age=40)
print(result)