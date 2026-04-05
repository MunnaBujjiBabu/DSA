from functools import reduce

#addition
# def addition(a,b):
#     return a+b


# addit=lambda a,b:a+b
# print(addit(4, 4))

# my_list = [1, 2, 3, 4, 5]
# multiply = list(map(lambda x : x * 2, my_list))
# print(multiply)


# even_num=[1,2,3,4,5]
# printthe_even=list(filter(lambda x:x%2==0, even_num))
# print(printthe_even)

my_list = [1, 2, 4, 5, 6]
my_reduced = reduce(lambda x, y: x+y, my_list)
print(my_reduced)

