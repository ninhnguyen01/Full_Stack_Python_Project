import json

album = {'id': 42, 'title':"Back in Black"}
string = json.dumps(album) # object to string
print(string)
albumm = json.loads(string) # string to object
print(album)
