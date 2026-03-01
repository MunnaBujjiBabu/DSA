my_list = [1, 2, 3, 4, 5]

my_list.append(6)  # O(1)
my_list.pop()       # O(1)
my_list.insert(0, 10)  # O(n)
my_list.remove(3)  # O(n)
my_list[2] = 20    # O(1)
my_list[1:4] = [30, 40, 50]  # O(k) where k is the number of elements being replaced
my_list.sort()     # O(n log n)
my_list.reverse()  # O(n)
my_list.clear()     # O(n)
my_list.copy()      # O(n)
