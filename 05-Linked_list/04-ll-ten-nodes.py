# 10 nodes
# for loop to add nodes
# while loop to print ll

class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(1)
# head --> 1 --> none

current = head

for i in range(2,11):
    new_node = Node(i)
    current.next = new_node
    current = new_node

current = head

while current:
    print(current.value)
    current = current.next
