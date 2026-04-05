#Polymorphism means “many forms” — the same method name can behave differently depending on the object
# Achieved via method overriding (inheritance) or duck typing (dynamic typing).

class TableTennisPlayer:
    def play(self):
        print("play with TT bat")
        
class ChessPlayer:
    def play(self):
        print("play with chess pieces")
        
def game(start):
    start.play()
    

game(TableTennisPlayer())
game(ChessPlayer())