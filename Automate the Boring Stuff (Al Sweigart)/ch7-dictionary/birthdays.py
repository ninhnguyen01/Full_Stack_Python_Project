birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    
    if name in birthdays:
      print(birthdays[name] + ' is the birthday of ' + name)
      with open('ch7-dictionary/birthdays.txt','w') as b:
            b.write('\n')
            birthday_file = b.write(str(birthdays))
            print("Birthday(s) saved to file!")
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
        print(birthdays.items())
        with open('ch7-dictionary/birthdays.txt','a') as b:
            b.write('\n')
            birthday_file = b.write(str(birthdays))
            print("Birthday(s) saved to file!")
        