# Task 7-2

string = "capitalize"

transformed_char = string[0]

if transformed_char >= 'a' and transformed_char <= 'z':
    transformed_char = chr(ord(transformed_char) -  32)
    transformed_string = transformed_char + string[1:]

print(transformed_string)
