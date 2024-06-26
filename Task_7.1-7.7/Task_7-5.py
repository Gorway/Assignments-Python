# Taks 7-5

string = "radar"

isPolindrom = True

start = 0
end = len(string) - 1

while start < end:
    if string[start] != string[end]:
        isPolindrom = False
        break
    start += 1
    end -= 1

if isPolindrom:
    print(f"String '{string}' is polindrom.")
else:
    print(f"String '{string}' is not polidnrom.")

