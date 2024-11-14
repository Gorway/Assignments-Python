import requests


response = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": 1})

if response.status_code == 200:
    posts = response.json()
    for post in posts:
        print(post["title"])
else:
    print("Failed to retrieve posts:", response.status_code)

