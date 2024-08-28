# Write a generator function read_file_lines(file_path) that reads a file line by line and yields each line. Use this generator to print each line of a file without loading the entire file into memory.
from time import sleep

def read_file_lines(file_name):
  file = open(file_name, 'r')
  try:
    for line in file:
      yield line
  finally:
    file.close()
    print("-File closed-")

reader = read_file_lines('example.txt')
for line in reader:
  sleep(1)
  print(line.strip())
