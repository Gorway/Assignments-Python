def reverse_string(string):
    if len(string) <= 1:
        return string
    return string[-1] + reverse_string(string[:-1])

string = "Hello, World!"

result = reverse_string(string)
print(f"Reversed string: {result}")

