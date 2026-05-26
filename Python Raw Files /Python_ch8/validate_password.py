# This program gets a password from the user and
# validates it.

import login2

def main():
    password = input('Enter your password: ')
    while not login2.valid_password(password):
        print('That password is not valid.')
        password = input('Enter your password: ')
    print('That is a valid password.')

if __name__ == "__main__":
    main()

# End