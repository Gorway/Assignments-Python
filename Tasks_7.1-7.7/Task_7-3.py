#Taks 7-3

string = "hello, world! are you ready?"

transformed_string = ""

for i in range(len(string)):
    if string[i].isdigit() or not string[i - 1].isalpha():
        if string[i] >= 'a' and string[i] <= 'z':
          transformed_string += chr(ord(string[i]) - 32)
        else:
            transformed_string += string[i]
    else:
        transformed_string += string[i]

print(transformed_string)
