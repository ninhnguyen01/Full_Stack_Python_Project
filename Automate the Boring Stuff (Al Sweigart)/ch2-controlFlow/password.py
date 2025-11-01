username = 'Mary'
password = 'Swordfish'
login = input('Enter username: ')
if login == username:
    print('Hello, ' + username)
    password_login = input('Password: ')
    if password_login == password:
        print('Access granted')
    else:
        print('Wrong password!')
else:
    print('Invalid user')
