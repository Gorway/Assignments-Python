from user import User
import message

user1 = User('Bob', 'Bob@gmail.com')
user2 = User('Tom', 'Tom@gmail.com')
user3 = User('Jenny', 'Jenny@gmail.com')

academy_chat = user1.create_conversation(user2)
text_message = message.TextMessage(user2, academy_chat, "Hi Tom")
user2.send_message(text_message,academy_chat)
user1.receive_message(text_message)
print(text_message.get_message_type())
user1.create_conversation(user3)
image = message.MultimediaMessage(user3, academy_chat,"'home/Example.png'", 'Image')
user1.send_message(image, academy_chat)
user1.receive_message(image)
work_chat = user1.create_conversation(user2)
work_chat.add_user(user3)
user2.send_message(text_message, work_chat)
s = user2.get_conversation()
s[0].add_message(image)