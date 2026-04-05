class Dog:
    def bark(self, bow):
        self.bow=bow
        print("Dog barks")
        
class Cat(Dog):
    def mew(self):
        print("Cat does Meow")
        
obj1=Cat()

obj1.mew()