file = open("peterrabbit.txt", mode="r")

words_to_found = {"example": 0, "all": 0, "up": 0, "did": 0, "him": 0}

file_context = file.read()
file_context = file_context.lower().split()

for word in file_context:
    if word in words_to_found:
        words_to_found[word] +=1
    else:
        continue

file.close()

for word, count in words_to_found.items():
    print(f"'{word}': {count}")

