while True:
    print('Who are you?')
    name = input('Enter name: ')
    if name != 'Kim':
        print('Invald user!')
        continue
    print(f'Hello, {name}! What is the password?')
    print('Hint: fish')
    password = input('Password: ')
    if password == 'Swordfish':
        break
    else:
        print()
        print('Try again')
        password = input('Password: ')
        if password == 'Swordfish':
            break

print('Access granted! Welcome!')