import requests
import json

url = 'http://localhost:8888/productionplan'
path = "payload3.json"

response = requests.post(url, json = path)

# print(json_object.content)


print("Status code: ", response.status_code)
print("Printing Entire Post Request")
print(response.json())
