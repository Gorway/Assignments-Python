import yaml
import json

with open('users.yaml', 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)


with open('data.json', 'w') as json_file:
    json.dump(yaml_data, json_file, indent=4)


with open('data.json', 'r') as json_file:
    json_data = json.load(json_file)



if yaml_data == json_data:
    print("Validation successful: The JSON structure retains all information.")
else:
    print("Validation failed: The JSON structure does not match the YAML data.")
