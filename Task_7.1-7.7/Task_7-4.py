# Task 7-4

string = "reverse me"
reversed_string = ""

for i in range(len(string) -1, -1, -1): # or reversed_string = string[::-1]
    reversed_string += string[i]

print(reversed_string)
