phone_letters = {'A': '2','B': '2','C': '2','D': '3','E': '3',
                 'F': '3','G': '4','H': '4','I': '4','J': '5',
                 'K': '5','L': '5','M': '6','N': '6','O': '6',
                 'P': '7','Q': '7','R': '7','S': '7','T': '8',
                 'U': '8','V': '8','W': '9','X': '9','Y': '9',
                 'Z': '9'}

num = input("Enter a name to be translated: ").upper()

number = ""
for ch in num:
    if ch in "ABC":
        ch = "2"
    elif ch in "DEF":
        ch = "3"
    elif ch in "GHI":
        ch = "4"
    elif ch in "JKL":
        ch = "5"
    elif ch in "MNO":
        ch = "6"
    elif ch in "PQRS":
        ch = "7"
    elif ch in "TUV":
        ch = "8"
    elif ch in "WXYZ":
        ch = "9"
    number += ch
print(number)
