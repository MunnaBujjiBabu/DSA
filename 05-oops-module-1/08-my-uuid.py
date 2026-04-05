import uuid

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.book_id = self.get_id()
        
    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]
        
    
book1 = Book('python book', 'test')
print(book1.get_id())

print(book1.__dict__.items())