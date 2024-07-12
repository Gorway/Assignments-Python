import os

file_name = "specific_position.txt"


if not os.path.exists(file_name):
    file = open(file_name, mode="w")
    file.write("Picsart Academy.\n")
    file.close()
    print("File created.")

file = open(file_name, mode="r+")
file_context = file.read()
cursor_position = file.tell()
print(f"Cursor position in file {file_name}: {cursor_position} ")
input_position = input("Enter cursor position: ")
file.seek(int(input_position))
input_text = input("Enter text: ")
file.write(input_text)
print("Text added.")
file.close()

