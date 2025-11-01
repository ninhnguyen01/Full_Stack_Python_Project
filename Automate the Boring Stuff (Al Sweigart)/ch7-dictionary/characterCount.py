message = """ “It was the best of times, it was the worst of times, it was the age of wisdom, \
    it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, \
        it was the season of light, it was the season of darkness, it was the spring of hope, \
            it was the winter of despair.”― Charles Dickens, A Tale of Two Cities """

count = {}

for character in message:
    count.setdefault(character, 0) 
    count[character] += 1

print(count)   