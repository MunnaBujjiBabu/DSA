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
        #case1: empty ll
        #case2: two or more nodes 
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
    
    def print_ll(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def pop(self):
        #two pointer method:
        #case 1: empty ll
        #case 2: only one node in ll
        #case 3: two or more nodes in ll
        current = self.head
        pre = self.head
        if self.head is None:
            return None
        elif self.head.next is None:
            self.head = None
            self.tail = None
            self.length -= 1
            return current
        else:
            while current.next:
                pre = current
                current = current.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            return current
        
        
    def prepend(self, value):
        new_node = Node(value)
        #case 1: empty ll
        #case 2: one or more nodes
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True
        
    def popfirst(self):
        #case 1: empty ll
        #case 2: only one node in ll
        #case 3: two or more nodes in ll
        temp = self.head
        if self.head is None:
            return None
        elif self.head.next is None:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            self.head = self.head.next
            temp.next = None
            self.length -= 1
        return temp    
        
    def get(self, index):
        temp = self.head
        if index < 0 or index >= self.length:
            return None
        else:
            for _ in range(index):
                temp = temp.next
        return temp.value
        
    def set(self, index, value):
        # case 1: invalid index
        # case 2: change value of first node 
        # case 3: change value of other node
        temp = self.head
        if index < 0 or index >= self.length:
            return None
        else:
            for i in range(index):
                temp = temp.next
            temp.value = value
        return True
        
    def insert_value(self, index, value):
        # case 1: empty ll
        # case 2: first node
        # case 3: last node
        # case 4: other nodes
        new_node = Node(value)
        if index < 0 or index > self.length:
            return None
        elif self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length
            return True
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return True
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return True
        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
            
    def remove_value(self, index):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            self.popfirst()
            self.length -= 1
            return True
        elif index == self.length:
            self.pop()
            self.length -= 1
            return True
        else:
            current = self.head
            pre = self.head
            for i in range(index):
                pre = current
                current = current.next
            pre.next = current.next
            current.next = None
            self.length -= 1
        return pre
            
    def reverse_list(self):
        pass
            
            
        
    
l1  = LinkedList(1)            
l1.append(2)
l1.append(3)
l1.pop()
l1.append(5)
l1.prepend(6)
l1.prepend(101)


l1.print_ll()
print("over")
# print(l1.length)
# print(l1.get(4))

# l1.set(7, 200)
# l1.print_ll()

# l1.insert_value(2, 200)
# l1.print_ll()
# print("over")
l1.remove_value(3)
l1.print_ll()