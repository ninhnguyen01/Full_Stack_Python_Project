#  Reading Input from the Keyboard 

# variable = input(prompt) 
name = input('What is your name? ')
print(name) 

# Get the user's first name.
first_name = input('Enter your first name: ')
# Get the user's last name.
last_name = input('Enter your last name: ')
# Print a greeting to the user.
print('Hello', first_name, last_name)

# Reading Numbers with the input Function
string_value = input('How many hours did you work? ')
hours = int(string_value)
print(hours)

hours = int(input('How many hours did you work? '))
pay_rate = float(input('What is your hourly pay rate? '))
total = hours * pay_rate
print("Day Paid: " + str(total)) # 'str' convert the value to text to prevent error 

# Get the user's name, age, and income.
name = input('What is your name? ')
age = int(input('What is your age? '))
income = float(input('What is your income? '))

# Display the data.
print('Here is the data you entered: ')
print('Name: ', name)
print('Age: ', age)
print('Income: ', income)
