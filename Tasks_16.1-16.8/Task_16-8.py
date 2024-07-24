def set_settings(user,**kwargs):
  settings = {
    "OS": input("Linux / Windows: "),
    "Auto update": input("Auto update: on/off: "), 
    "Energy save mode": input("Energy save mode on/off: "),
    "Screen lock": input("Screen lock on/off: "),
  }

  settings.update(kwargs)

  set_apply(user, **settings)

def set_apply(user, **settings):
  print(f"User {user} settings applied successfuly.")
  print("Settings\n")
  print('-' * 10)
  for key, value in settings.items():
    print(f"{key}: {value}")

set_settings(input("Enter User name: "))