secret_pass = "PicsartAcademy"
message = ""

while(message != "Success"):
  user_input = input("Please enter password: ")

  message = "Success" if secret_pass ==  user_input else "Error, wrong password, Please try again."

  print(message)




