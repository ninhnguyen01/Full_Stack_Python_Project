# lefse, a Norwegian delicacy that resembles a tortilla

# pseudo-code
# REQUIREMENTS
#  1/2 c. butter or margarine
#  1/2 c. cream
#  2 1/2 c. flour
#  1 t. salt
#  1 T. sugar
#  4 c. riced potatoes (cold)

# DIRECTIONS
# Be sure all ingredients are cold before adding flour.
# Mix all ingredients.
# Knead thoroughly.
# Form into 20 balls. Store cold until the next step.
# For each ball:
#   Spread flour on cloth.
#   Roll ball into a circle with a grooved rolling pin.
#   Fry on griddle until brown spots appear.
#   Turn over and fry other side.

# I have prior coding experience. Everything below will make sense to you as you learn Python from this book 

# Hold key-value data (dictionary) ingredients for lefse
ingredients = {'butter or margarine': '1/2 c.', 'cream': '1/2 c.', 'flour': '2.5 c.', \
               'salt': '1 t.', 'sugar': '1 T.', 'riced potatoes (cold)': '4 c.'}

print()
print('Lefse Ingredients')
print('-' * 8) # create a section border

# check if each ingredient is in 'dictionary'
if 'butter or margarine' in ingredients.keys():
    print("Ingredient 1: ")
    print('butter or margarine')
    print(ingredients['butter or margarine'])
else:
    print("You are missing the ingredient: BUTTER OR MARGARINE")

if 'cream' in ingredients.keys():
    print("Ingredient 2: ")
    print('cream')
    print(ingredients['cream'])
else:
    print("You are missing the ingredient: CREAM")

if 'flour' in ingredients.keys():
    print("Ingredient 3: ")
    print('flour')
    print(ingredients['flour'])
else:
    print("You are missing the ingredient: FLOUR")

if 'salt' in ingredients.keys():
    print("Ingredient 4: ")
    print('salt')
    print(ingredients['salt'])
else:
    print("You are missing the ingredient: SALT")

if 'sugar' in ingredients.keys():
    print("Ingredient 5: ")
    print('sugar')
    print(ingredients['sugar'])
else:
    print("You are missing the ingredient: SUAGR")

if 'riced potatoes (cold)' in ingredients.keys():
    print("Ingredient 6: ")
    print('riced potatoes (cold)')
    print(ingredients['riced potatoes (cold)'])
else:
    print("You are missing the ingredient: RICED POTATOES (COLD)")

print('-' * 8) # create a section border


temperature = input('Are all ingredients cold? Enter (Y/n): ') # ask for input from user

if temperature.lower() == 'y': # 'lower()' purpose is to accept the letter 'Y' by converting to 'y' from user input
    print("Step 1: Add flour")
    print("Step 2: Mix all ingredients.")
    print("Step 3: Knead thoroughly.")
    print("Step 4: Form into 20 balls. Store cold until the next step.")
    print('-' * 8)
    continue_cook = input('Do you want to continue (Y/n)?: ')
    if continue_cook.upper() == 'Y':
        print("Instructions for balls")
        print("\tFor each ball: ")
        print("\tStep 1: Spread flour on cloth.")
        print("\tStep 2: Roll ball into a circle with a grooved rolling pin.")
        print("\tStep 3: Fry on griddle until brown spots appear.")
        print("\tStep 4 (final): Turn over and fry other side.")
        print('-' * 8) # create a section border
    else:
        print('You stopped cooking...')
else:
    print("Check all ingredients again. MUST BE COLD.")
    print()
