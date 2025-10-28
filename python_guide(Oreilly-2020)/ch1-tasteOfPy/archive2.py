# web search program with archive.org

# import package
import webbrowser
import json
from urllib.request import urlopen
import requests


print("Let's find an old website.")
# enter website URL and date
site = input("Type a website URL: ")
era = input("type a year, month, and day (ex. 20150613): ")
# archive.org website to search the internet
url = "https://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = requests.get(url)
data = response.json()

# exception handling for error
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print('Found this copy: ', old_site)
    # hold control/command button and click with left mouse button to open the URL search link in browser manually
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)