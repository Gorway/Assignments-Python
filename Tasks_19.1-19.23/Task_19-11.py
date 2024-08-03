# Write a function make_logger(level) that returns a function which logs messages with the specified log level.

def make_logger(level):
  messages = {
    "Error" : "Your input is not valid.",
    "Success": "Your registration has been successful.",
    "Info": "Check your email."
  }
  
  def logger():
    if level in messages:
      print(f"[{level}] {messages.get(level)}")
    else:
      raise ValueError("There is no message for this level.")
  return logger

logger = make_logger("Success")
logger()