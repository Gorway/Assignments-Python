# Task 7-1

index = -1

char_to_find = 'z'

string = "I have been working at the zoo for 2 years"

for i in range(len(string)):
    if string[i] == char_to_find:
        index = i
        break

if index > 0:
   print(f"Character '{char_to_find}' index is {index} .")
else:
   print(f"Character '{char_to_find}' not found.")
