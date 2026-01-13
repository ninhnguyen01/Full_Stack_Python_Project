import webbrowser
import json
from urllib.request import urlopen

"""
1 - Import (make available to this program) all the code from the Python standard library module called webbrowser.
2 - Import all the code from the Python standard library module called json. This converts text data between the JSON format (see Chapter 19 later for details) and Python data structures.
3 - Import only the urlopen() function from the standard library module urllib.request.
4 - A blank line, because we don't want to feel crowded.
5 - Print some initial text to your display.
6 - Print a question about a URL, read what you type, and save it in a program variable called site.
7 - Print another question, this time reading a year, month, and day, and then save it in a variable called era. Append the hour and minute for midnight (0000); the Wayback Machine will look earlier and later for the closest date and time the page was last grabbed.
8 - Construct a string variable called url to make the Wayback Machine look up its copy of the site and date that you typed. This uses the f-string format that can embed the values of variables.
9 - Connect to the web server at that URL and request a particular web service.
10 - Get the response data and assign it to the variable contents.
11 - Decode contents to a text string in JSON format, and assign that string to the variable text.
12 - Convert the text JSON string to data (a Python data structure).
Error-checking: try to run the next four lines, and if any fail, run the last line of the program (after the except).
13 - If we got back a match for this site and date, extract its value from a three-level Python dictionary. Notice that this line and the next three are indented. That's how Python knows that they are part of the try section.
14 - Print the URL that we found.
15 - Print what will happen after the next line executes.
16 - Display the URL we found in your web browser.
17 - If anything failed in the previous four lines, Python jumps down to here.
18 - If the try code block failed, print a message and the site that we were looking for. This is indented because it should be run only if the preceding except line runs.
"""

# example
# Type a website URL: xkcd.com
# Type a year, month, and day, like 20150613: 20240728

print("Let's find an old website.")
site = input("Type a website URL: ")
era = input("Type a year, month, and day, like 20150613: ") + "0000"
url = f"http://archive.org/wayback/available?url={site}&timestamp={era}"
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)
try:
     old_site = data["archived_snapshots"]["closest"]["url"]
     print("Found this copy:", old_site)
     print("It should appear in your browser now.")
     webbrowser.open(old_site)
except:
     print("Sorry, no luck finding", site)