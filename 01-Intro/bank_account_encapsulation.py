#bank class with instance methods - constructor, deposit, withdraw, get_balance 
#Encapsulation - data hiding and controlled access -  Achieved using public, protected, and private variables

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner                  #public
        self.__balance = balance            #private
    
    def deposit(self, amount):
        self.__balance += amount
        return f"New balance after deposit is {self.__balance}"
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"New balance after withdraw {self.__balance}"
    
    def get_balance(self):                  #controlled access
        print(f"Your balance is {self.__balance}")
        


obj1 = BankAccount('munna', 1000)
obj1.get_balance()
obj1.deposit(1000)
obj1.get_balance()
obj1.withdraw(10)
obj1.get_balance()