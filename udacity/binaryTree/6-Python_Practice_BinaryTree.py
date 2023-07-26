# this code was generate by chatgpt
# Binary Search Tree (BST):

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left  = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, current_node, value):
        if not current_node:
            return TreeNode(value)
        
        if value < current_node.value:
            current_node.left = self._insert_recursive(current_node.left, value)
        else:
            current_node.right = self._insert_recursive(current_node.right, value)
        
        return current_node
    
    def find_kth_smallest(self, k):
        return self._find_kth_smallest_recursive(self.root, k)
    
    def _find_kth_smallest_recursive(self, current_node, k):
        if not current_node:
            return None, k

        result, k = self._find_kth_smallest_recursive(current_node.left, k)
        print("Current node:", current_node.value,"K",k-1) # debug
        if k == 0:
            return result, k

        k -= 1
        if k == 0:
            return current_node.value, k

        return self._find_kth_smallest_recursive(current_node.right, k)

    def find_range_elements(self, low, high):
        elements = []
        self._find_range_elements_recursive(self.root, low, high, elements)
        return elements
    
    def _find_range_elements_recursive(self, current_node, low, high, elements):
        if not current_node:
            return
        
        if low <= current_node.value <= high:
            elements.append(current_node.value)

        if current_node.value > low:
            self._find_range_elements_recursive(current_node.left, low, high, elements)
        if current_node.value < high:
            self._find_range_elements_recursive(current_node.right, low, high, elements)

    def find_successor(self, value):
        return self._find_succesor_recursive(self.root, value)
    

    def _find_succesor_recursive(self, current_node, value):
        if not current_node:
            return None
        
        if current_node.value == value:
            if current_node.right:
                return self._find_min_node(current_node.right)
            return None
        
        if value < current_node.value:
            succesor = self._find_succesor_recursive(current_node.left, value)
            return succesor if succesor else current_node.value
        
        return self._find_succesor_recursive(current_node.right, value)
    

    def _find_min_node(self, node):
        while node.left:
            node = node.left
        return node.value
    
bst = BinarySearchTree()
elements = [5, 3, 7, 2, 4, 6, 8]
for element in elements:
    bst.insert(element)

print("K-th Smallest Element (k=3):", bst.find_kth_smallest(3))
print("Elements within Range (4, 7):", bst.find_range_elements(4, 7))
print("Successor of 4:", bst.find_successor(4))

print('*' * 60)
#************************************************************************#

class BinarySearchTree2:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        # If the tree is empty create a new root and set it to be equal to this newly
        if not current_node:
            return TreeNode(value)
        
        if value < current_node.value:
            current_node.left = self._insert_recursive(current_node.left, value)
        if value > current_node.value:
            current_node.right = self._insert_recursive(current_node.right, value)

        return current_node
    
    def search(self, value):
        """Returns True or False depending on whether `value` exists in BST"""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, current_node, value):
        if not current_node or current_node.value == value:   # Base case - we've reached an end point without finding
            return current_node

        if value < current_node.value:
            return self._search_recursive(current_node.left, value)
        return self._search_recursive(current_node.right, value) 


bst = BinarySearchTree2()
values = [5, 3, 7, 2, 4, 6, 8]

for value in values:
    bst.insert(value)


print("Search 6:", bst.search(6))  # Output: TreeNode object
print("Search 9:", bst.search(9))  # Output: None