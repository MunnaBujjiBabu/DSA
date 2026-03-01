# O(a + b)
# In this example, we have two parameters `a` and `b`. 
# The time complexity of the `print_items` function is O(a + b) because 
# it iterates through both parameters independently. 
# The first loop runs `a` times and the second loop runs `b` times, 
# resulting in a total of `a + b` iterations.


def print_items(a, b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)


print_items(a, b)