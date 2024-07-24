def registration_check(first_name, last_name, *, country=''):
  if first_name == '' or last_name =='':
    raise ValueError("First name and last name are required")
  print(f"Successful Registrtion\nWelcome {first_name} {last_name}.")
  if country:
    print(f"Your country: {country}")



full_name = []
full_name.append(input("Enter First name*:"))
full_name.append(input("Enter Lastdo name*:"))
country = input("Enter your country(not requireda): ")
registration_check(*full_name, country=country)