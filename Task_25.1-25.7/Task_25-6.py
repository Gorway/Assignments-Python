import requests

post_data = {
    "title": "Picsart Academy",
    "body": "Task 6.",
    "userId": 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=post_data)

print(response.json())

