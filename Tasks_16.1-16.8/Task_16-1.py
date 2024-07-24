def greet_user(first_name, last_name, greeting_msg="Hello"):
  name = f"{first_name} {last_name}"
  greeting = f"{greeting_msg} {name}"
  return greeting


first_name = "Bob"
last_name = "Smith"
another_greeting_massage = "Good morning!"

print(greet_user(first_name,last_name,))
print(greet_user(first_name,last_name,greeting_msg=another_greeting_massage))