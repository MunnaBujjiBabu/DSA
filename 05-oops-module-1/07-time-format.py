import time
class Container:
    @staticmethod
    def get_time():
        print(time.strftime("%H:%M:%S", time.localtime()))
        
        
Container.get_time()