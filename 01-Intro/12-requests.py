import requests

# my_response = requests.get("https://api.github.com")
# print(my_response)
# print(my_response.status_code)
# # print(my_response.content)
# print(my_response.json())


data = {"name": "Alice","age": 25}

my_response_post = requests.post("https://google.com", json=data)
print(my_response_post)