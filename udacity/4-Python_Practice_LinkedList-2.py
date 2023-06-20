#  Creating a class node where the value and pointer is stored
#  Initialize the id and name parameter so it can be passed as Node(id, name)

# Class Node
class Node():
    def __init__(self, id, name):
        self.id   = id
        self.name = name
        self.next = None

# Create a class linkedlist to store the value in a node
class LinkedList():
        # Constructor function for the linkedlist class
    def __init__(self):
        self.first = None
    
    # This function inserts the value passed by the user into parameters id and name
    # id and name is then send to Node(id, name) to store the values in node called new_node
    def insertStudent(self, id, name):
        # modify this function to insert both id and names as in Q1
        new_node = Node(id, name) # instance the object
        new_node.next = self.first
        self.first = new_node
    # This function prints the data in the list
    def printStudents(self):
        current = self.first
        while (current != None):
            print(current.id, current.name)
            current = current.next
    # This function prints the length of the linked list        
    def length(self):
        current = self.first
        count   = 0
        while (current != None):
            count += 1
            current = current.next
        return count
    # This function lets us search for a data and flag true is it exists
    def searchStudent(self, x, y):
        current = self.first
        while (current != None):
            if ((x == current.id and y== current.name)):
                return True
            current = current.next
    # This function lets us delete a data from the node
    def delStudent(self, id):
        current = self.first   # get the first element
        #iterate through the linkedlist
        while(current != None):
            if(current.id == id): # if this condition is true clear
                self.first = current.next
                return
        # if the data is in other nodes delete it
            prev    = current
            current = current.next
            if(current.id == id):
                prev.next = current.next
                return



# Create the class
my_list = LinkedList()

# Insert data using insertStudent method of my_list
my_list.insertStudent(101, "David")
my_list.insertStudent(999, "Rosa")
my_list.insertStudent(321, "Max")
my_list.insertStudent(555, "Jenny")
my_list.insertStudent(369, "Jack")


# Print the list of students
my_list.printStudents()
print('*' * 60)

# Print the length of the linked list
print(my_list.length(), ": is the size of linked list ")
print('*' * 60)

# Search for a data in linked list
if my_list.searchStudent(379, "Jack"):
    print("True")
else:
    print("False")
print('*' * 60)

# Delete a value in the linked list
my_list.delStudent(101)

# Print the linked list after the value is deleted in the linked list
my_list.printStudents() 