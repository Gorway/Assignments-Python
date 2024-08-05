#Create a dictionary with functions for basic file operations (e.g., read, write, append, delete). Write a function file_manager(file_name, operation, content=NoneGG) that uses this dictionary to perform the requested file operation.

def file_read(fileName):
  file = open(fileName, 'r')
  file_content = file.read()
  file.close()
  return file_content

def file_write(fileName, text):
  file = open(fileName, 'w')
  if text != None:
    file.write(text)
    file.close()
  else:
    raise ValueError("Enter text to add into file.") 
  
def file_append(fileName, text):
  file = open(fileName, 'a')
  file.write(text)
  file.close()

def file_delete(fileName):
  try:
    file = open(fileName, 'r')
    pass
  except FileNotFoundError:
    raise FileNotFoundError(f"File not foudn: '{file_name}'")
  file = open(fileName, 'w')
  file.close()
  
file_operations = {
  "Read": file_read,
  "Write": file_write,
  "Append": file_append,
  "Delete": file_delete
}

def file_managment(fileName, operation, content=None):
  if operation in file_operations:
    if operation == "Read":
      print(file_operations[operation](fileName))
    elif operation in ["Write", "Append"]:
      file_operations[operation](fileName, content)
    elif operation == "Delete":
      file_operations[operation](fileName)
  else:
    raise ValueError("Operation is not supported.")
  
file_managment("test.txt", "Write", "Python")