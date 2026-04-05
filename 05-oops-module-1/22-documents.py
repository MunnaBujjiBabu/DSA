class Doc:
    def __init__(self, string):
        self.string = string
    
    def __repr__(self):
        return f"Doc(string = '{self.string}')"
    
    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Doc(self.string + ' ' + other.string)
    
doc1 = Doc('Object')
doc2 = Doc('Oriented')

print(doc1 + doc2)
print(repr(doc1 + doc2))