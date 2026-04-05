a = 10
b = "AKAMAI"

try:
    c=a/b 
except TypeError:
    print("you are trying to divide string by interger ")
else:
    print("IT WORKS")  
    
finally:
    print("It works anytime")