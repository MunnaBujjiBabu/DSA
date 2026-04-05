class Person:
    def __init__(self, fname , lname):
        self.fname=fname
        self.lname=lname
        # self.__repr__=self.__repr__
        
    def __repr__(self):
        return f"fnames = '{self.fname}', lnames = '{self.lname}'"
    
person1= Person("John", "Doe")
print(person1)

person2 = Person("munna", "reddy")
print(person2)