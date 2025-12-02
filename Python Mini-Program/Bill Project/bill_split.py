import random

# Function to create and update the dictionary with bill split
def split_the_bill():
    # Step 1: Get the number of people
    num_people = int(input("How many people will be joining, including you? "))
    
    # Step 2: Validate the number of people
    if num_people <= 0:
        print("No one is joining for the party")
        return
    
    # Initialize an empty dictionary
    friends_dict = {}
    
    # Collect names and store them in the dictionary
    for _ in range(num_people):
        name = input("Enter the name of a person joining: ")
        friends_dict[name] = 0
    
    # Step 3: Get the total bill
    total_bill = float(input("Enter the total bill amount: "))
    
    # Step 4: Calculate the split amount and round it
    split_amount = round(total_bill / num_people, 2)
    
    # Step 5: Update the dictionary with the split values
    for name in friends_dict:
        friends_dict[name] = split_amount
    
    # Step 6: Ask the user if they want to use the lucky feature
    lucky_feature = input("Would you like to choose a lucky person? Write 'Yes' or 'No': ").strip().lower()
    
    # Step 7: Handle the lucky feature
    if lucky_feature == 'yes':
        lucky_person = random.choice(list(friends_dict.keys()))
        print(f"{lucky_person} is the lucky one!")
    else:
        print("No one is going to be lucky.")
    
    # Step 8: Print the updated dictionary
    print(friends_dict)

# Call the function
split_the_bill()
