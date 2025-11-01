# specify path to password
file_path = 'intro/password_file.txt'
# ope and read the file
password_file = open(file_path)
read_file = password_file.read()
# close the file afterward
password_file.close()
# user input
print('Enter your username: ')
account_name = input()
print('Enter your password: ')
account_password = input()
# password entry must match password in file
if account_password == read_file:
    print('Access granted')
    # create a text file
    subscription_acc = open('intro/subscription.txt','w')
    # save account info in text file
    subscription_acc.writelines('Account: Netflix\n')
    subscription_acc.writelines('Password: ABCDO\n')
    print('Account & password saved!')
    # close the text file
    subscription_acc.close()
else:
    print('Access denied!')
