# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


def fin(count):
    a, b = 0, 1
    
    while count:
        print(a, end = ' ')
        a, b = b, a + b
        count -= 1





fin(100)