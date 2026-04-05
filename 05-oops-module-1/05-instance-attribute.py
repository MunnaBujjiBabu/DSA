class Person:
    
    instances = []
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Person.instances.append(self)
    
    @classmethod
    def count_instances(cls):
        print(len(Person.instances))
        
        
person1 = Person('test', 'qa')
person2 = Person('test2', 'qa2')

Person.count_instances()