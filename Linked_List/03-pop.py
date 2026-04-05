class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # WRITE THE PRINT_LIST METHOD HERE #
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    ####################################
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    
    def pop(self):
        if self.length == 0:
            return "List is empty"    
        elif self.length ==1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            self.tail = temp
            self.next = None
    

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    3
    
"""
