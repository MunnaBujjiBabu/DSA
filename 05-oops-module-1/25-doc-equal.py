class Hashtag:
    def __init__(self, string):
        self.string = '#' + string
    
    def __repr__(self):
        return f"Hashtag string = {self.string}"
    
    def __str__(self):
        return f"{self.string}"
    
    def __add__(self, other):
        return Hashtag(self.string[1:] + ' ' + other.string)

H1 = Hashtag("Hello")
H2 = Hashtag("world")
print(H1)
print(H2)
print(H1 + H2)