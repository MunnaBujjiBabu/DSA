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
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def my_empty_ll(self):
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
        return True
        
            
                








my_linked_list = LinkedList(10)

print("head: ", my_linked_list.head)
print("value: ", my_linked_list.head.value)
print("tail: ", my_linked_list.tail)
print("length: ", my_linked_list.length)
print("next:" , my_linked_list.head.next)

my_linked_list.my_empty_ll()

# my_linked_list.print_list()
my_linked_list.append(11)
# my_linked_list.print_list()
my_linked_list.append(12)
# my_linked_list.print_list()
my_linked_list.append(13)
my_linked_list.print_list()
print("tail: ", my_linked_list.tail)
print("head: ", my_linked_list.head)