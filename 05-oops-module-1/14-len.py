class Vector:
    
    def __init__(self, *args):
        self.components = args
    
    def __repr__(self):
        return f"Vector{self.components}"
    
    def __str__(self):
        return f"{self.components}"
    
    def __len__(self):
        return len(self.components)
    
v1 = Vector(1,2,3,4)
print(v1)
print(len(v1))
