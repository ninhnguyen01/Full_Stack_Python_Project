import webbrowser
import json
import requests

from urllib.request import urlopen

print("Let's find an old website!")
site = input("Type a website url: ")
era = input("Type a year, month, and day, like 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = requests.get(url)
data = response.json()

# test example
# Type a website url: www.myspace.com
# Type a year, month, and day, like 20150613: 20030801
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy: ", old_site)
    print("It should appear in your browser now.")
    webbrowser.open(old_site)

except:
    print("Sorry, no luck finding: ", site)