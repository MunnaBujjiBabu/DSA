class Person:
    @classmethod
    def show_details(cls):
        print(f"{cls.__name__}")
    
    # show_details = classmethod(show_details)
        
#person1=Person()
Person.show_details()