file_name = "append_mode.txt"

text_to_append = "Hello world.\n"

file = open(file_name, mode='a')

file.write(text_to_append)

file.close()
