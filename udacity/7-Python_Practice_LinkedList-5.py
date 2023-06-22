## chatGPT
# this code examples was generate by 

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insertData(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def display(self):
        print("Normal Order: ", end='')
        current = self.head
        while current != None:
            print(current.data, end=' ')
            current = current.next
        print()

c = LinkedList()
c.insertData(1)
c.insertData(20)
c.insertData(-255)
c.insertData(44)
c.display()