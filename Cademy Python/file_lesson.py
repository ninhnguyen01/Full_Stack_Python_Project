# Python Readline Method
with open('Cademy Python/text/story.txt') as story_object:
    print(story_object.readline())

# Parsing JSON files to dictionary
# Use json.load with an opened file object to read the contents into a Python dictionary.
# Contents of file.json
# { 'userId': 10 }
import json
with open('Cademy Python/json/file.json') as json_file:
  python_dict = json.load(json_file)
print(python_dict.get('userId'))
# Prints 10

# Python Read Method
with open('Cademy Python/text/mystery.txt') as text_file:
   text_data = text_file.read()
   print(text_data)
