# class methods
# Dog class
class Dog:
  # Method of the class
  def bark(self):
    print("Ham-Ham")
# Create a new instance
charlie = Dog()
# Call the method
charlie.bark()
# This will output "Ham-Ham"

# Class Variables
class my_class:
  class_variable = "I am a Class \
Variable!"

x = my_class()
y = my_class()

print(x.class_variable) #I am a Class Variable!
print(y.class_variable) #I am a Class Variable!

# init method
class Animal:
  def __init__(self, voice):
    self.voice = voice
# When a class instance is created, the instance variable
# 'voice' is created and set to the input value.
cat = Animal('Meow')
print(cat.voice) # Output: Meow
dog = Animal('Woof')
print(dog.voice) # Output: Woof
