# mangling

class Account:
    def __init__(self, name, id):
        self.name=name
        self.__id=id
        
    def func_2(self):
        print(self.__id)
        
acc = Account("Bank account", 3)
print(acc._Account__id)
acc.func_2()