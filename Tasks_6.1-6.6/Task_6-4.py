strings = ["Hello", "PicsartAcademy", "Python", "Hello" , "Hello", "Python"]

unique_str = []
count = []

for string in strings:
    found = False
    for i in range(len(unique_str)):
        if unique_str[i] == string:
            count[i] += 1
            found = True
            break
    if not found:
        unique_str.append(string)
        count.append(1)

for i in range(len(unique_str)):
    print(f"{unique_str[i]} : {count[i]}")
