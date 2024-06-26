# Task 7-7

string = "banana"

transformed_string = ""

for char in string:
    if char == 'a':
        transformed_string += 'x'
    else:                           # or transformed_string.replace('a', 'x')
        transformed_string += char

print(transformed_string)
