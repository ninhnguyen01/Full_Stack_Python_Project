letter = '''Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} 
{verbed} in your {room}. Please note that it should never 
be used in a {room} , especially near any {animals}.

Send us your receipt and {amount} for shipping and handling. 
We will send you another {product} that, in our tests,
is {percent} less likely to have {verbed}.

Thank you for your support.

Sincerely,

{spokesman}
{job_title}
'''

salutation_input = 'Mr.'
name_input = 'John'
product_input = 'soap cleaner'
verbed_input = 'damaged the carpet'
room_input = 'living room'
animals_input = 'pets'
amount_input = '$30.00'
percent_input = '90%'
spokesman_input = 'Jane Doe'
job_title_input = 'Manager'
entry = letter.format(salutation = salutation_input, name = name_input, product = product_input, 
                      verbed = verbed_input, room = room_input,
                      animals = animals_input, amount = amount_input, percent = percent_input,
                      spokesman = spokesman_input, job_title = job_title_input)

with open ('response.txt','w') as f:
    f.write(entry)
    print(entry)
    f.close()