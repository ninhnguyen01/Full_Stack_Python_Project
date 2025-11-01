import random

random_num = random.randint(1,10)
for guesses in range(1,7):
    guesses = 0
    print('Guess a number between 1-6 (6 chances)')
    guess = int(input("number: "))
    guesses += guess
    if guesses == 6:
        break
    else:
        if guess > random_num:
            print('Guess is too high!')
            print()
        elif guess < random_num:
            print('Guess is too low!')
            print()
        else:
            print("Guess is correct!")
            print()
            break
        
if guess == random_num:
    print('Good job! You got it in ' + str(guesses - 1) + ' guesses!')
else:
    print('Nope. The number was ' + str(random_num))
