# Write a form letter by using new-style formatting. 
# Save the following string as letter (you’ll use it in the next exercise):
# Assign values to variable strings named salutation, name, product, verbed (past tense verb), room, animals, percent, spokesman, and job_title. 
# Print letter with these values, using letter.format().

letter = '''Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title} '''.format(salutation = 'Mr.', name = 'John', product = 'spray', verbed = 'casued damage', 
                       room = 'living room', animals = 'animals', amount = '$15.00', percent = "90",
                       spokesman = 'Jane Doe', job_title = 'Manager')

print(letter)
