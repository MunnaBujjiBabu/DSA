class Person:
    instances = []
    def __init__(self):
        Person.instances.append(self)
        
    @classmethod
    def count_instances(cls):
        print(len(Person.instances))
        
        
person1 = Person()
person2 = Person()
person3 = Person()

Person.count_instances()