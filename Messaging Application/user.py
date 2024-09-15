from typing import List
from message import Message, MessagingManager



class User(MessagingManager):
  def __init__(self, name: str, contact_info: str):
    self._name = name
    self._contact_info = contact_info
    self._conversations: List['Conversation'] = []
  
  def create_conversation(self, user: 'User'):
    new_onversation = Conversation(participants=[self, user])
    self._conversations.append(new_onversation)
    user._conversations.append(new_onversation)
    return new_onversation

  def send_message(self, message: 'Message', conversation: 'Conversation'):
    conversation.add_message(message)
  
  def receive_message(self, message: 'Message'):
    print(f"Received message from {message._sender._name}: {message.display_content()}")
  
  def manage_settings(self):
    ...
  
  def get_conversation(self):
    return self._conversations
  
  def view_conversation_history(self, conversation: 'Conversation'):
    return conversation.get_messages()
  
#-------------------------------------------------------------------------------------------------------
class Conversation:
  def __init__(self, participants: List['User']):
    self._participants = participants
    self._message_history: List['Message'] = []
  
  def add_message(self, message: 'Message'):
    self._message_history.append(message)
  
  def add_user(self, user: 'User'):
    if user not in self._participants:
      self._participants.append(user)
  
  def get_messages(self):
    return self._message_history