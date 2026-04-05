class Dog:
    
    animal = "domesticated"         #class attribute
    
    def __init__(self, name="munna", age=23):  #constructor
        self.name = name            #instance variable
        self.age = age
    
    def talk():             # class methods
        print("bark")
        print(dog_3.age)
    
    def run(self):          # instance methods
        print(dog_3.age)

# Dog.talk()

# dog_1 = dog('tom', 2)
# dog_1.run()
# print(dog_1.name)
# print(dog_1.age)


# dog_2 = dog('john', 4)
# dog_2.animal = "domesticated & wild"

# print(dog_2.animal)
# print(dog_1.animal)

dog_3 = Dog()
# print(dog_3.age)
dog_3.run()

dog_4 = Dog("Prajwal")
# print(dog_4.age)



Dog.talk()