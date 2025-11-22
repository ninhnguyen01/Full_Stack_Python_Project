# Caesar cipher 
# -- take each letter in your message, find its position in the alphabet, 
# take the letter located after 3 positions in the alphabet, 
# and replace the original letter with the new letter. --

text = str(input("Enter a text: "))
shift = 3

def caesar(message,offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)        
    print('encrypted text:', encrypted_text)
    with open('Cybersecurity Python/Cipher Project/Caesar cipher/plain/plain_text.txt','a') as f:
        f.write('Plain Entry: ' + message + '\n')
        f.close
        print()
        print('Plain text saved to file!')
    with open('Cybersecurity Python/Cipher Project/Caesar cipher/encrypt/encrypt.txt','a') as f:
        f.write('Secured Entry: ' + encrypted_text + '\n')
        f.close
        print()
        print('Encrypted text saved to file!')

caesar(text, shift)