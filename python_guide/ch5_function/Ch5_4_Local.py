# Local Variables

# This program demonstrates two functions that have local variables
# with the same name.
def main():
    texas()
    california()
def texas():
    birds = 5000
    print(f'texas has {birds} birds.')
def california():
    birds = 8000
    print(f'california has {birds} birds.')

main()
