# https://pythondiario.com/2018/07/linked-list-listas-enlazadas.html
# https://geekflare.com/es/python-linked-lists/

class Node:
    def __init__(self, data = None, next= None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    # add data at frent
    def add_at_front(self, data):
        self.head = Node(data=data, next=self.head)

    def isEmpty(self):
        return not bool(self.head) # check if is empty

    def add_at_end(self, data):
        # validate if is null and create the node
        if not self.head:
            self.head = Node(data=data) 
        # else add at the end    
        current = self.head    
        while current.next:
            current  = current.next
        current.next = Node(data=data)

    def delete_node(self, key):
        current = self.head
        prev    = None
        while current and current.data != key:
            prev    = current
            current = current.next
        if prev is None:
            self.head = current.next
        elif current:
            prev.next = current.next
            current.next = None
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
            print("Last element in linked list:", temp.data)
    def print_list(self):
        current = self.head
        while (current!=None):
            print(current.data,"->", end=" ")
            current = current.next

c = LinkedList()
c.add_at_front(2)
c.add_at_end(4)
c.add_at_front(3)
print(c.isEmpty())
c.delete_node(2)
c.get_last_node()
c.print_list()