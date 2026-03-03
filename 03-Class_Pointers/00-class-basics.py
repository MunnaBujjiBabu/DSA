class Dog:
    animal = 'domestic'             # class attribute
    def __init__(self, name, age):  # constructor
        self.name = name            # Instance attribute
        self.age = age

    def bark(self):
        print('woof')
        return f"{self.name} says woof"

dog_1 = Dog('tom', 2)               # class object
print(dog_1.name, dog_1.age, dog_1.animal)
dog_1.bark()


dog_2 = Dog('johnny', 3)            # class object
dog_2.animal = 'domestic & wild'
print(dog_2.name, dog_2.age, dog_2.animal)


print(dog_1.name, dog_1.age, dog_1.animal)
print(Dog.animal)