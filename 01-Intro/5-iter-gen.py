# list=[1,2,3]

# my_iterator = iter(list)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))


list_2=[1,2,3,4,5]


def count_up_to(n):
    count = 0
    while count <= n:
        yield count
        # print(count) 
        count += 1   

# count_up_to(1000)
my_count = count_up_to(1000)

for i in my_count:
    print(i)
    
temp =  f.read(chunk_size)
while chunk = temp:   # walrus operator
    yield chunk
            
            
