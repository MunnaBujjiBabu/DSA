class Container:
    @classmethod
    def show_details(cls):
        print(f"Running from {cls.__name__}")
        

container = Container()

container.show_details()