#Creating JSON file
import json

data = [
  {"id": 1, "category": "Books", "title": "Python Programming"},
  {"id": 2, "category": "Cars", "title": "Subaru"},
  {"id": 3, "category": "Books", "title": "Learn JSON"},
]

file =  open('data.json', 'w')
json.dump(data, file)
file.close()

print("JSON file created: 'data.json' ")


# Write a function that reads a JSON file containing a list of dictionaries. The function should process the data (e.g., find all entries with a specific attribute) and write the results to a new JSON file.
import json

def filter_json(input_file: str, output_file: str, attribute: str, value) -> None:
  file = open(input_file, 'r')
  data = json.load(file)
  
  file.close()

  filtered_data = [item for item in data if item.get(attribute) == value]
  output = open(output_file, 'w')
  json.dump(filtered_data, output, indent=4)

  print(f" Filtered result written to file: {output_file}")

filter_json('data.json', 'filtered_data.json', 'category', 'Books')
