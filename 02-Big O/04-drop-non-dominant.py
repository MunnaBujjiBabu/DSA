# O(n2) for nested for loop & o(n) for k loop
# total O(n2 + n), but n i negligible i.e non dominant compared to O(n2)
# so drop off the n i.e O(n2 + n) is called as O(n2)


def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
            
    for k in range(n):
        print(k)



print_items(10)

