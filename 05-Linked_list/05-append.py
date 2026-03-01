class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
        
    def display(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
        print("None")
        
ll = LinkedList()
ll.append(11)
ll.append(7)
ll.append(5)
ll.display()