import os

file_name = "exclusive_mode.txt"

text_to_write = "Adding text at exclusive mode."

if os.path.exists(file_name):
   print(f"Error: File {file_name} already exist.\n")
else:
    file = open(file_name, mode="x")
    file.write(text_to_write)
    file.close()



