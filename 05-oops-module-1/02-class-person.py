class Person1:
    
    @classmethod
    def show_details(cls):
        print(f'running from {cls.__name__}')


Person1.show_details()