# Assign True or False to the variables small and green. 
# Write if/else statements to print which of these matches those choices: cherry, pea, watermelon, pumpkin.

small = True
green = True

if small and not green:
    print("It's a cherry!")
elif small and green:
    print("It's a pea!")
elif not small and green:
    print("It's a watermelon!")
else:
    print("It's a pumpkin!")
    