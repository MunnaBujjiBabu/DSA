class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def info(self):
        return f"{self.name} has a salary of {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, teamsize):
        self.teamsize = teamsize                # super method - reuse parent constructor
        super().__init__(name, salary)
    
    def info(self):                             # overriding
        return f"{self.name} manages a teamsize of {self.teamsize} and has a salary of {self.salary}"
    
    

emp = Employee("munna", 100)
mgr = Manager("sid", 1000, 2)

print(emp.info())
print(mgr.info())
        