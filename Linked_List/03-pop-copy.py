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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def print_ll(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def pop(self):
        temp = self.head
        pre = self.head
        if self.head is None:
            return None
        elif self.head.next is None:
            self.head = None
            self.tail = None
            return temp.value
        else:
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            return temp.value


                

        
        
        

l1 = LinkedList(1)
l1.append(2)
l1.append(3)

#l1.print_ll()
print(l1.pop())
# l1.print_ll()
print(l1.pop())
print(l1.pop())
#l1.print_ll()