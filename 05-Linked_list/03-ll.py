class LinkedList:
    def __init__(self, value):
        self.value = value
        self.head = value
        self.tail = value
        self.next = None
        self.length = 1
        


my_linked_list = LinkedList(4)
print(my_linked_list.value)
print(my_linked_list.head)
print(my_linked_list.tail)
print(my_linked_list.next)
print(my_linked_list.length)