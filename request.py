import requests

url = "https://jsonplaceholder.typicode.com/users/"

response = requests.get(url, timeout=10)

if response.status_code == 200:
    users = response.json()

    user = users[0]

    print("USER DETAILS")
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("City:", user["address"]["city"])
    print("Company:", user["company"]["name"])

else:
    print("Request failed:", response.status_code)