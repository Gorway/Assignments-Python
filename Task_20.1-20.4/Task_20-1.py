
# Write a function that reads a text file and counts the number of lines, words, and characters in the file. Then, write these statistics to a new file.

def file_statistic(file_name):
  lines_count = 0
  words_count = 0
  characterss_count = 0
  
  file = open(file_name, 'r')
  
  for line in file.readlines():
    lines_count += 1
    words_count += len(line.split())
    for char in line:
      if char.isalnum():
        characterss_count += 1
  
  file.close()
  
  output = open('output.txt', 'w')
  
  output.write(f"Lines count: {lines_count}\n")
  output.write(f"Words count: {words_count}\n")
  output.write(f"Characters count: {characterss_count}\n")
  
  output.close()
  
  print(f"Fle '{file_name}' statistics were successfully written to the file 'output.txt' ")
  
some_file = open("example.txt", 'w')
some_file.write("Hello World\nPython\nPicsart Academy\nEnd of text.\n")
some_file.close()

file_statistic('example.txt')