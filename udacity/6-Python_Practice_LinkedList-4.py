class Node:
    def __init__(self, data):
        # data of node
        self.data = data
        # next pointer 
        self.next = None


class LinkedList:
    def __init__(self):
        # initializing the hed with None
        self.head = None

    # Insert new node
    def insert(self, new_node):
        # checking the head is empty or not
        if self.head:
            # getting the last node
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next
            # assining the new node to the next pointer of last node
            last_node.next = new_node
        else:
            # assigning the first element as a head
            self.head = new_node

    #display the nodes
    def display(self):
        temp_node = self.head
        while temp_node != None:
            # printing the node data
            print(temp_node.data, end="->")
            temp_node = temp_node.next
        print('Null')


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert(Node(1))
    linked_list.insert(Node(2))
    linked_list.insert(Node(3))
    linked_list.insert(Node(4))
    linked_list.display()