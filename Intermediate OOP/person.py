class Person:   
    residence = "Planet Earth"

    def __init__(self, name, age):     
        self.name = name     
        self.age = age     
        self.height = 0 

    def introduce(self):       
        print(f"Hello, my name is {self.name}")

    @classmethod   
    def wake_up(cls):       
        print("Time to start your day!")

    def __eq__(self, other):
        return self.name == other.name

class Employee(Person):   
    def __init__(self, name, age, title, department):     
        super().__init__(name, age)  
        self.title = title    
        self.department = department   
    
    def change_position(self, new_title):       
        self.title = new_title

    def introduce(self):       
        print(f"""My name is {self.name}, I am a {self.title}""")

    def __add__(self, other):     
    # Use the + operator to create a 
    # Team with the name of each Employee     
        return Team([self.name, other.name]) 
    
    def begin_job(self, department):    
        self.department = department    
        print(f"Welcome to {self.department}!")

class Team:   
    def __init__(self, team_members):     
        # team_members is a list of names     
        self.team_members = team_members   
    
    def __add__(self, other):     
        # Adding Team objects creates a larger Team     
        return Team(self.team_members + other.team_members)
    
class Student:   
    def __init__(self, school):     
        self.school = school     
        self.courses = []    
    
    def add_course(self, course_name):     
        self.courses.append(course_name)

class Intern(Employee, Student):     
    def __init__(self, age, title, department, school, duration):         
        # Make a call to BOTH constructors         
        Employee.__init__(self, age, title, department, school)         
        Student.__init__(self, school)         
        self.duration = duration 

class Manager(Employee):   
    def __init__(self, name, title, number_reports, department):     
        Employee.__init__(self, name, title, department, department)     
        self.number_reports = number_reports 
        
# This invokes a call to __init__ 
john = Person("John Casey", 38)

# Create an instance of Person 
sarah = Person("Sarah Walker", 31) 
print("Sarah's age: " + str(sarah.age))  # Retrieve the age instance attribute

print("Residency: " + str(Person.residence))

chuck = Person("Chuck", 32) 
chuck.introduce()  # Called on a Person object

# Calling a class method 
Person.wake_up() 

lester = Employee("Lester", 26, "Technician", "Electrical") 
lester.introduce()  # Inherited from Person print(lester.title)

lester.change_position("Cashier") 
print("Lester's new title: " + lester.title)

lester = Employee("Lester", 26, "Technician", "Electrical") 
lester.introduce()

# Compare two Person objects 
chuck = Person("Charles Carmichael", 25) 
charles = Person("Charles Carmichael", 25) 
print(chuck == charles) 

bryce = Person("Bryce", 25) 
orion = Person("Orion", 25) 
print(bryce == orion)

# Create two Team objects 
rookies = Team(["Casey", "Emmitt"])
veterans = Team(["Mike", "Chuck"])  

# Attempt to add these two Teams together 
dream_team = rookies + veterans 
print(type(dream_team)) 
print(dream_team.team_members)

# Create two Employee objects 
anna = Employee("Anna", 21, "Technical Specialist", "Electrical") 
jeff = Employee("Jeffrey", 21, "Musician", "Music") 

# Now, attempt to add these together to create a team 
audio_team = anna + jeff 
print(type(audio_team)) 
print(audio_team.team_members)

stephen = Intern("Stephen", 20, "Software Development", "Echo University", 10) 
stephen.begin_job("Engineering")  # Method from Employee 

stephen.add_course("Intermediate OOP in Python")  
# Method from Intern 
print(stephen.courses)

mike = Manager("Mike", "Engineering Manager", 20, "L4") 
mike.introduce() 
mike.change_position("Director of Engineering") 
print("Mike's new title: " + mike.title)
print(mike.number_reports)