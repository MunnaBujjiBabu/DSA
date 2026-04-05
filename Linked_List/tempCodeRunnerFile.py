    def insert(self, index, value):
        if index<0 or index>self.length:
            return None
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index-1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1 
            return True