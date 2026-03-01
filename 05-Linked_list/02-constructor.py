class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # create new node
    def __init__(self, value, ):            #self, value is a parameter, function with self means its a function inside a class - called method
        new_node = Node(value)
        # self.new_node = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

        


node = LinkedList(1)
print(node.head.value)
node.print_list()


