class Employee:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

print()
person = Employee(input("Enter all name(s): "))   
print()

with open("OOP Demo/employeeRecord.csv", 'a') as f:
    f.write("\n")
    f.write(str(person))
    print("Name: " + str(person))
    print()
