# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181

def fib(count):
    a, b = 0, 1
    
    while count:
        print(a, end= ' ')
        a, b = b, b+a
        count -= 1
        print (f'count is {count}')
    

fib(100)


# import math
# print(math.sqrt(9))

