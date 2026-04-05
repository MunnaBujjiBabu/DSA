class animal:
    pass
    status = 'domesticated'
    # def __init__(self, mainspeed):
    #     self.mainspeed = mainspeed
    
    def walk(self, speed):
        self.speed = speed
    
    
class dogs(animal):
    dog_status = animal.status
    animal.walk(30)
    

list_1 = []

list_1.sort



# obj_1 = animal()
# obj_1.walk(10)
# print(obj_1.speed)

obj_2 = dogs()
print(obj_2.dog_status)
print(obj_2.speed)
