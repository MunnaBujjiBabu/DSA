class Father:
    def skills(self):
        print("Painting")

class Mother:
    def skills(self):
        print("dancing")
        
class Child(Mother, Father):
    def skills(self):
        print("coding")


#Method resolution order
obj_1 = Child()
obj_1.skills()