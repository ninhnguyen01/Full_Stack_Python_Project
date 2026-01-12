# Techniques for Designing Classes (Title)

# 10.15 The typical UML diagram for a class has 3 sections.
# What appears in these 3 sections?
# Name of class
# Class's fields
# Class's methods

# 10.16 What is a problem domain?
""" A written description of the real-world objects,
parties, and major events related to the problem. """

# 10.17 When designing an object-oriented application,
# who should write a description of the problem domain?
""" If you understand, then you. If not, then an expert. """

# 10.18 How do you identify the potential classes in a problem
# domain description? 
""" 1) Identify nouns, pronouns, pronoun phrases.
    2) Refine list to eliminate duplicates. """

# 10.19 What are a class's responsibilities?
""" The thind a class know and the actions a class do. """

# 10.20 What 2 questions should you ask to determine a class's
# responsibilities?
""" What must the class know? What must the class do? """

# 10.21 Will all of a class's actions always be directly 
# mentioned in the problem domain description?
""" No. Not always. """

class Customer:
    def __init__(self,name,address,phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
    def set__name(self,name):
        self.__name = name
    def set__address(self,address):
        self.__address = address
    def set__phone(self,phone):
        self.__phone = phone
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone(self):
        return self.__phone

class Car:
    def __init__(self,make,model,year):
        self.__make = make
        self.__model = model
        self.__year = year
    def set__make(self,make):
        self.__make = make 
    def set__model(self,model):
        self.__model = model
    def set__year(self,year):
        self.__year = year
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year

TAX_RATE = 0.05
class ServiceQuote:
    def __init__(self,pcharge,lcharge):
        self.__parts_charges = pcharge
        self.__labor_charges = lcharge
    def set__parts_charges(self,pcharge):
        self.__parts_charges = pcharge 
    def set__labor_charges(self,lcharge):
        self.__labor_charges = lcharge
    def get__parts_charges(self):
        return self.__parts_charges
    def get__labor_charges(self):
        return self.__labor_charges
    def get_sales_tax(self):
        return self.__parts_charges * TAX_RATE
    def get_total_charges(self):
        return self.__parts_charges + self.__labor_charges + \
            (self.__parts_charges * TAX_RATE)
