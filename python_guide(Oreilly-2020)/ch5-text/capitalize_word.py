# capitalize the word starting with m
song = """When an eel grabs your arm, 
... And it causes great harm,
... That's - a moray"""

if "moray" in song:
    song = song.replace("moray", "Moray")
    print(song)