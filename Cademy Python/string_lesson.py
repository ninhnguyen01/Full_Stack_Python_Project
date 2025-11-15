# Escaping Characters
txt = "She said \"Never let go\"."

print(txt)

# in syntax
game = "Popular PC Game: Cyberpunk 2077"

print("Cyber" in game)
print("2076" in game)

# Indexing and slicing strings
str = "color"
print(str[1])
print(str[-1])
print(str[2:5])
print(str[:4])
print(str[-3:])

# Iterate string
str = "Hail Atreides!"

for c in str:
    print(c)

# Built in function len()
length = len(str)
print(length)

colors = ["red", "yellow", "green"]
print(len(colors))

# String concatenation
x = "One Fish,"
y = "two fish."

z = x + y
print(z)

# Python string.format()
msg1 = "Nicholas spricht {} Sprachen. Er spricht {}, {}, {}."
print(msg1.format(3, "Englisch", "Vietnamesisch", "Deutsch"))

msg2 = "Nicholas {verb} ein {noun}."
print(msg2.format(verb="hat", noun="Auto"))

# String methods
greeting = "Willkommen nach Amerika"
print(greeting.lower())

text1 = "   Hello there   "
text2 = "+-Apple and Oranges-+"

print(text1.strip())
print(text2.strip("-+"))

name = "cyber punk 2077"
print(name.title())

tech_place = "Silicon Valley"
print(tech_place.split())

mountain_name = "Everest"
print(mountain_name.find("E"))

fruit = "berry"
print(fruit.replace("r","R"))

gender = "Man"
print(gender.upper())

x = "-".join(["Coding","is","awesome"])
print(x)
