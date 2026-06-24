import requests

url = "https://api.github.com/users/torvalds"
response = requests.get(url)
data = response.json()

print(f"用户名: {data['login']}")
print(f"Followers 数量: {data['followers']}")
