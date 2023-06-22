class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            # O(n) time | O(1) space - where n is the length of
    def insert(self,data, position):
        if position < 0 or position > self.length():
            raise IndexError("Invalid Position")
        
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count   = 0
            while count < position - 1:
                current= current.next
                count += 1
            new_node.next = current.next
            current.next = new_node

    def delete(self, data):
        if self.head is None:
            return 
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def search(self, data):
        """Returns the node with given value"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def length(self):
        count = 0
        current = self.head
        while current:
            count +=1
            current = current.next
        return count
    
    def display(self):
        print("Normal Order: ", end='')
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def getPosition(self, position):
        if position < 1:
            return 
        current = self.head
        while current and position > 1:
            position -= 1
            current = current.next
        return current




if __name__=="__main__":
    llist=LinkedList()
    llist.append(6)
    llist.insert(2,1)
    llist.insert(3,2)
    llist.insert(4,3)
    llist.insert(5,4)
    llist.display()
    print("length:",llist.length())
    print("searching 10: ", llist.search(10))
    print("searching 6: ", llist.search(6))
    llist.delete(2)
    llist.display()
    print("the value of position 3:", llist.getPosition(3).data)