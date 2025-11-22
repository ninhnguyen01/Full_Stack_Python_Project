primarycolor = str(input('Enter a primary color: '))
primarycolor2 = str(input('Enter a primary color: '))

if primarycolor == 'red' and primarycolor2 == 'blue':
    print(f'When you mix {primarycolor} and {primarycolor2}, you get purple.')
elif primarycolor == 'blue' and primarycolor2 == 'red':
    print(f'When you mix {primarycolor} and {primarycolor2}, you get purple.')
elif primarycolor == 'red' and primarycolor2 == 'yellow':
    print(f'When you mix {primarycolor} and {primarycolor2}, you get orange.')
elif primarycolor == 'yellow' and primarycolor2 == 'red':
    print(f'When you mix {primarycolor} and {primarycolor2}, you get orange.')
elif primarycolor == 'blue' and primarycolor2 == 'yellow':
    print(f'When you mix {primarycolor} and {primarycolor2}, you get green.')
elif primarycolor == 'yellow' and primarycolor2 == 'blue':
    print(f'When you mix {primarycolor} and {primarycolor2}, you get green.')
else: 
    print('You did not enter primary colors (red, blue, or yellow) in the correct combo!')
    