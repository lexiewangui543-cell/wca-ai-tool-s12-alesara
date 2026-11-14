import requests
url = "https://jsonplaceholder.typicode.com/users/"
response = requests.get(url, timeout=10)

# if response.status_code == 200:
#     user = response.json()
#     user = user[0]   
#     print ("Name:", user["name"])
#     print ("Email:", user["email"])
#     print ("city:", user["address"]["city"])
# else:
#  print ("request failed:", response.status_code())
print (response.json())
