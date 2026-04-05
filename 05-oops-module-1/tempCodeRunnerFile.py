class Doc:
    def __init__(self, string):
        self.string = string
    
    def __repr__(self):
        return f"Doc(string = {self.string})"

    def __str__(self):
        return f'{self.string}'

doc1 = Doc('Hello')
print(repr(doc1))


doc2 = Doc('World')
print(repr(doc2))