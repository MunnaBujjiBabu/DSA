class Person:
    def __init__(self, fname , lname):
        self.fname=fname
        self.lname=lname
        # self.__repr__=self.__repr__

    def __str__(self):
        return f"First name = '{self.fname}'\nLast name = '{self.lname}'"
        
    def __repr__(self):
        return f"fnames = '{self.fname}', lnames = '{self.lname}'"
    

    
person1= Person("John", "Doe")
print(person1)



person2 = Person("Edcorner", "Learning")
print(person2)

print(repr(person2))
