# from datetime import datetime

# class Container:

#     def get_current_time():
#         print(datetime.now())
        
        
# Container.get_current_time()


import time

class Container:
    
    def get_current_time():
        print(time.strftime('%H:%M:%S', time.localtime()))
        
Container.get_current_time()