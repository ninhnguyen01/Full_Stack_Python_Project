# Choose a number from 1 to 10 and assign it to the variable secret. 
# Then select another number from 1 to 10 and assign it to the variable guess. 
# Next, write the conditional tests (if, else, and elif) to print the string too low if guess is less than secret, or too high if greater than secret, or just right if equal to secret.

secret = 7
print()
print("Enter 0 to exit!")
guess = int(input("Enter a number (1 - 10): ")) # while loop control variable 
print()

while guess != 0:
    if guess < secret:
        print("Guess is too low!")
        print()
        guess = int(input("Enter a number (1 - 10): "))
    elif guess > secret:
        print("Guess too high!")
        print()
        guess = int(input("Enter a number (1 - 10): "))
    elif guess == secret:
        print()
        print("Correct guess!")
        print()
        break # stop program after correct entry
