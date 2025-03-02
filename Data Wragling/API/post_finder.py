import requests

username = input("Enter the username: ")

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

users = response.json()
user_id = None

for user in users:
    if user["username"] == username:
        user_id = user["id"]

if user_id is None:
    print("User Not Found")
else:
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    posts = response.json()

    for post in posts:
        if post["userId"] == user_id:
            print(f"Title: {post['title']}\nBody: {post['body']}\n")
