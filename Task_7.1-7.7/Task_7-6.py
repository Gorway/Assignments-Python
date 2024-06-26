# Task 7-6

string1 = "Hello"
string2 = "World!"

result = ""

for s in [string1, string2]:
    if result:
        result += " "
    result += s

print(result)

