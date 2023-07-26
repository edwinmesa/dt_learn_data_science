class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # pass
        self.root =  self._insert_recursive(self.root, new_val)

    def _insert_recursive(self, current_node, new_val):
        if not current_node :
            return Node(new_val)
        
        if new_val < current_node.value:
            current_node.left = self._insert_recursive(current_node.left, new_val)
        else:
            current_node.right = self._insert_recursive(current_node.right, new_val)

        return current_node

    def search(self, find_val):
        return self._search_recursive(self.root, find_val)
    
    def _search_recursive(self, current_node, find_val):
        
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))