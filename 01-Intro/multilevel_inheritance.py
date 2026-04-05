class Senior_manager:
    def skills(self):
        print("Managerial skills")
        
class Lead(Senior_manager):
    def lead_skills(self, name="Junk"):
        self.name = name
        print("Leading a team")
        
class Employee(Lead):
    def emp_skills(self):
        print("table tennis skils")
        
# obj1=Employee()
#obj1.emp_skills()
# obj1.lead_skills("akamai")
# print(obj1.name)
# obj1.name = "Google"

#print(obj1.name)

# Employee.emp_skills()
#obj1=Employee()
obj1.emp_skills()