class Cookie:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
        
    def set_color(self, color):
        self.color = color

my_cookie_1 = Cookie("red")
my_cookie_2 = Cookie("blue")

print(my_cookie_1.color)
print(my_cookie_2.color)


my_cookie_1.set_color("green")

print(my_cookie_1.color)
print(my_cookie_2.color)
