class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
    
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    
    def display(self):
        current = self.head
        while (current != None):
            print(current.data,"->", end=" ")
            current = current.next
    
    def countNodes(self):
        current = self.head
        count   = 0 
        while (current != None):
            count += 1
            current = current.next
        return count
    
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

# Start setting up a LinkedList
ll = LinkedList(n1)
# Append to node the data
ll.append(n2)
ll.append(n3)
ll.append(n4)
# Print the list
print(ll.display())
# Print the length of list
print("Nodes:", ll.countNodes())