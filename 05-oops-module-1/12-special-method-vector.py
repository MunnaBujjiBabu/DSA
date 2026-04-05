class Vector:
    def __init__(self, *args):
        self.comp = args
        
    def __repr__(self):
        return f"{self.comp}"
    
vector1=Vector(2,4,6,8)    
print(vector1)
    
