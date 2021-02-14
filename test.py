import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "helloworld/tom")
# print(response.json())
response = requests.get(BASE + "video/1")
print(response.json())
response = requests.get(BASE + "video/44")
print(response.json())
response = requests.put(
    BASE + "video/1", {"likes": 1, "views": 1, "name": "śmieszne kotki"})
print(response.json())
response = requests.put(
    BASE + "video/2", {"likes": 22, "views": 21, "name": "śmieszne kotki 2"})
print(response.json())
response = requests.put(
    BASE + "video/6", {"likes": 22, "views": 21, "name": "to jest 6"})
print(response.json())
response = requests.patch(BASE + "video/2", {})
print(response.json())

response = requests.get(BASE + "video/6")
print(response.json())
response = requests.delete(BASE + "video/6")
print(response)

response = requests.get(BASE + "video/6")
print(response.json())
