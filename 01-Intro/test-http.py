import requests
response = requests.get("http://httpforever.com/")
print(response)
print(response.content)