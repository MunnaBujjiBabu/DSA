#Big O - O(n2) - 100 operations i.e - 10 * 10 (n * n) i.e 100

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print_items(10)
