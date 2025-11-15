#elif statement

pet_type = "dog"

if pet_type == "dog":
    print("You have a dog.")
elif pet_type == "cat":
    print("You have a cat.")
else:
    print("You have another pet.")

# or operator
x = 3

if x > 2 or x < 3:
    print(True)
else:
    print(False)

# == operator
gender = "man"

if gender == "man":
    print(True)
else:
    print(False)

# !- operator
if gender != "woman":
    print("They are not the same.")
else:
    print("They are the same.")

# and operator
x = 5

if x > 4 and x < 7:
    print(True)
else:
    print(False)
