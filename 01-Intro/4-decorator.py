
# def my_decorator(func1):
#     def my_wrapper(a,b):
#         print("before wrapper")
#         sum_return = func1(a,b)
#         sum_return_constant = sum_return + 10
#         print(sum_return_constant)
#         print("after wrapper")
#     return my_wrapper    


# @my_decorator
# def my_add(a,b):
#     return a+b
    

# my_add(1,2)

# # my_add_1 = lambda a,b: a+b
# # print(my_add_1(5,4))



# def repeat_function(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#             return wrapper
#         return repeat_function


# @repeat_function(3)
# def print_hello():
#     print("hello")


# print_hello()





