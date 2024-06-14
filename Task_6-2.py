strings = ["hello", "picsart", "academy", "yerevan"]

for string in strings:
        first_char = chr(ord(string[0]) - 32) if 'a' <= string[0] <= 'z' else string[0]
        print(first_char)

