def log_message(severity, *args, **kwargs):
  result = f"Severity: {severity}\n"
  
  for index, message in enumerate(args, start=1):
    result += f"Message {index}: {message}\n"

  for key, value in kwargs.items():
    result += f"{key}: {value}\n"

  return result
  
  
  

user = "Darth Vader"
timestamp = "A long time ago"
place = "In galaxy, far far away..."

result = log_message("Not that important", "Luke, I,m your father.", "Noooooooo....", timestamp=timestamp, user=user, place=place)

print(result)