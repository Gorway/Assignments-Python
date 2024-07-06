users = []


while len(users) < 2:

    print("Enter User information. You can add only 2 user.")
    user_id = input("Enter ID: ")
    user_firts_name = input("Enter first name: ")
    user_last_name = input("Enter last name: ")
    user_email = input("Enter email: ")
    user_phone_number = input("Enter phone number: ")
    user_password = input("Enter password: ")

    user = { 'ID': user_id,
             'First Name': user_firts_name,
             'Last Name': user_last_name,
             'Email': user_email,
             'Phone': user_phone_number,
             'Password': user_password
       }

    users.append(user)
    print(f"(User {user_firts_name} {user_last_name} added successfully.)")

if len(users) >= 2:
    print("You cannot add more than two users.")

target_user = input("Enter name to find user: ")

for user in users:
    if user['First Name'] == target_user:
       print(f"User {target_user} is found. User ID is: {user['ID']}")
       break
    else:
        print(f"User {target_user} is not found.")


