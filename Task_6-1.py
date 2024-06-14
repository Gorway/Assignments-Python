strings = ["Hello", "Bye", "Python", "PicsartAcademy"]

max_length = 0
longest_string = ""
longest_index = 0

size = len(strings)

for i in range(size):
    if len(strings[i]) > max_length:
        max_length = len(strings[i])
        longest_string = strings[i]
        longest_index = i

print(f"Longest string: {longest_string}")
print(f"Longest string index: {longest_index}")
