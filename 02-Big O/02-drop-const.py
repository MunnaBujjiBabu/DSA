#Big O - print 20 items - i.e n + n times = 2n times 
# O(2n) can be written as O(n) - drop constants.

def print_item(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

print_item(10)

