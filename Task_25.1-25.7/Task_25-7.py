import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()
except requests.exceptions.HTTPError as http_err:
    print("HTTP error occurred:", http_err)
except Exception as err:
    print("Other error occurred:", err)
else:
    print(response.json())

