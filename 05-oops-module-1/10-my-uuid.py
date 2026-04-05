import uuid

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.book_id = self.get_id()
        
        
    @staticmethod    
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]

    def test(self):
        print(f'book is {self.title} author is {self.author} and id is {self.book_id}')

book1 = Book('test', 'qa')

book2 = Book('python', 'qa')


print(book1.get_id())
book1.test()
book2.test()
