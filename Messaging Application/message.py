import abc
import user
from typing import List
from datetime import datetime

#-----------------------------------------------------------------------------------------------
class Message(abc.ABC):
  def __init__(self, sender: 'user.User', conversation: 'user.Conversation', timestamp: datetime = None):
    self._sender = sender
    self._conversation = conversation
    self._timestamp = timestamp if timestamp else datetime.now()
  
  @abc.abstractmethod
  def display_content(self)-> None:
    ...
    
  @abc.abstractmethod
  def get_message_type(self)-> str:
    ...
#-----------------------------------------------------------------------------------------------
class TextMessage(Message):
  def __init__(self, sender: 'user.User', conversation: 'user.Conversation', content: str):
    super().__init__(sender, conversation, datetime.now())
    self._content = content
  
  def display_content(self):
    return f'Message content: {self._content}'
  
  def get_message_type(self):
    return 'Text'
    
#-----------------------------------------------------------------------------------------------
class MultimediaMessage(Message):
  def __init__(self, sender: 'user.User', conversation: 'user.Conversation', file_path: str, media_type: str):
    super().__init__(sender, conversation, datetime.now())
    self._file_path = file_path
    self._media_type = media_type
  
  def display_content(self):
    return f"Multimedia file at {self._file_path} Type: {self._media_type}"
  
  def get_message_type(self):
    return self._media_type
#-----------------------------------------------------------------------------------------------
class MessagingManager(abc.ABC):
  @abc.abstractmethod
  def send_message(self, message: 'Message')->None:
    ...
  
  @abc.abstractmethod
  def receive_message(self, message: 'Message')->None:
    ...
  
  @abc.abstractmethod
  def view_conversation_history(self, conversation: 'user.Conversation')-> List['Message']:
    ...