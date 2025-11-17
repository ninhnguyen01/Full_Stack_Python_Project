class Dog:

    scientific_name = "Canis lupus familiaris"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Woof!")

    def hear(self, words):
        if self.name in words:
            self.speak()
