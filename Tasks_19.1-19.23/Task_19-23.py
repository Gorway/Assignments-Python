# Store functions for text processing (e.g., word count, character count, find word, replace word) in a dictionary. Write a function process_text(text, operation, **kwargs) that uses this dictionary to perform the requested text processing operation.

def wordCount(text):
  words = text.split()
  return len(words)

def characterCount(text):
  result = [character for character in text if character.isalpha()]
  return len(result)

def findWord(text, word):
  return text.split().count(word)

def replaceWord(text, oldWord, newWord):
  return text.replace(oldWord, newWord)

text_operations = {
  "Word count": wordCount,
  "Character Count": characterCount,
  "Find Word": findWord,
  "Replace Word": replaceWord
}

def process_text(text, operation, **kwargs):
  if not text:
    raise ValueError("Text can't be empty.")
  
  if operation in text_operations:
    text_operations[operation](text, **kwargs)
  else:
    raise ValueError("Operation not found.")
    