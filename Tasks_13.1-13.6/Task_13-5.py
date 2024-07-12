def find_uppercase_letter(string):
    for i in string:
        if i >= 'A' and i <= 'Z':
            return i
    return '-1'

user_input = input("Enter text with some uppercase letter: ")

result = find_uppercase_letter(user_input)

if result != '-1':
    print(f"First uppercase letter in string: '{user_input}' is '{result}'.")
else:
    print("Uppercase letter  not exist.")
