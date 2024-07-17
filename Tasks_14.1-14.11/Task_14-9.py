def print_char_on_new_line(string, start=0):
    if start >= len(string):
        return string
    print(string[start])
    print_char_on_new_line(string, start + 1)

string = "Hello World!"

print_char_on_new_line(string)
