class Student:     
    def __init__(self, student_name, ssn):         
        self.name = student_name
        self.ssn = ssn      
    
    @property       
    def ssn(self):         
        return "XXX-XX-" + self._ssn[-4:]  
    
    @ssn.setter       
    def ssn(self, new_ssn):   
        if len(new_ssn) == 11:       
            self._ssn = new_ssn 

    @ssn.deleter     
    def ssn(self):         
        raise AttributeError("Can't delete SSN") 
    
    def __getattr__(self, student_name):
        self.__setattr__(student_name, None)
        return None  

    def __setattr__(self, name, value):     
        # If value is a string, set the attribute using the __dict__ attribute     
        if isinstance(value, str):       
            print(f"Setting {name} = {value}")       
            self.__dict__[name] = value      
        else: # Otherwise, raise an exception noting an incorrect data type         
            raise Exception("Unexpected data type!")
        if value is None:  # Print a message denoting a placeholder             
            print(f"Setting placeholder for {name}")          
            self.__dict__[name] = value  # Set the attribute 
        
shaw = Student("Daniel Shaw", "193-80-1821") 
shaw.residence_hall = "Honors College South"
print(shaw.residence_hall)
