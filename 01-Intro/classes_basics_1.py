class Dog:
    
    species = "domesticated"
    
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    
    #class method
    @classmethod
    def inside_class_method(cls):
        return cls.species
    
    #instance method
    def inside_instance_method(self):
        return self.species
    
    #static method
    @staticmethod
    def inside_static_method(junk):
        print(Dog.species)
        return junk.species
        # return "Welcome to dogs world"
    
    
    
obj_1 = Dog('tom', 22)
# print(Dog.inside_class_method())
# print(obj_1.inside_instance_method())
# print(obj_1.inside_static_method(obj_1))

obj_1.inside_static_method(obj_1)
print(Dog.species)

Dog.species = "Munna"

# print(Dog.species)
# print(obj_1.species)

obj_1.species = "keshav"
print(Dog.species) #Munna
print(obj_1.species) #keshave
