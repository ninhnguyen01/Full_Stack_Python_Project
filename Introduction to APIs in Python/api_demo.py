import requests

api = ''

response = requests.get(api)
print(response.text)

# GET = Retrieve a resource / Read
response = requests.get('')  
# POST = Create a resource  / Create
response = requests.post('', data={"key": "value"}) 
# PUT = Update an existing resource  / Update
response = requests.put('', data={"key": "value"})  
# DELETE = Remove a resource / Delete
response = requests.delete('')