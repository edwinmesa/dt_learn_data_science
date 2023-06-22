# provide for ChatGPT
class Node:
    def __init__(self, data):
        self.data = data
        self.prev  = None
        self.next  = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertData(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current   = current.next
            current.next  = new_node
            new_node.prev = current

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False
    
    def display(self):
        current = self.head
        while current != None:
            print(current.data, end=' ')
            current = current.next
        print()    

c = LinkedList()
c.insertData(2)
c.insertData(5)
c.insertData(10)
c.insertData(156)
c.display()
print('searching for 3 is : ', c.search(3))
print('searching for 10 is : ', c.search(10))