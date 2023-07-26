# this code was generate by chatgpt
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None
    
class BinaryTree:
    def __init__(self): 
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, current_node, value):

        if value < current_node.value:
            if current_node.left:
                self._insert_recursive(current_node.left, value)
            else:
                current_node.left = TreeNode(value)
        else:
            if current_node.right:
                self._insert_recursive(current_node.right, value)
            else:
                current_node.right = TreeNode(value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, current_node, value):
        """Return True is the given `value` exists in binary tree."""
        if not current_node:
            # If we reach a leaf node and haven't found our target yet, it doesn't exist
            return False
        if current_node.value == value:
            # We've reached the end of the path to find our target! Return true now that its
            # been found successfully.
            return True
        elif value < current_node.value:
            # Search left subtree for this particular value recursively until either you
            # hit an empty branch or your target has been located at some point within
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)
        
    def inorder_traversal(self):
        return self._inorder_traversal_recursive(self.root)
    
    def _inorder_traversal_recursive(self, current_node):
        if not current_node:
            return []
        left_values = self._inorder_traversal_recursive(current_node.left)
        right_values = self._inorder_traversal_recursive(current_node.right)
        return left_values + [current_node.value] + right_values
    
binaryTree = BinaryTree()
print("Inserting values into Tree...")
for i in range (10,-1,-1):
    print ("inserting",i,"into BST")
    binaryTree.insert(i)

# Testing InOrder Traversal
print("Inorder Traversal: ", binaryTree.inorder_traversal())

# Searching 
print("Search 6:", binaryTree.search(6))
print("Search 9:", binaryTree.search(11))

print('*' * 60)
#************************************************************************#

class BinaryTree2:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, current_node, value):
        # If the tree is empty then create a new node and set it as root
        if value < current_node.value:

            if current_node.left:
                self._insert_recursive(current_node.left, value)
            else:
                current_node.left = TreeNode(value)
        else:
            if current_node.right:
                self._insert_recursive(current_node.right, value)
            else:
                current_node.right = TreeNode(value)

    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, current_node, value):
        if not current_node:
            return False
        elif current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)
        
    def inorder_traversal(self):
        return self._inorder_traversal_recursive(self.root)
    
    def _inorder_traversal_recursive(self, current_node):
        if not current_node:
            return []
        
        left_values = self._inorder_traversal_recursive(current_node.left)
        right_values = self._inorder_traversal_recursive(current_node.right)
        return left_values + [current_node.value] + right_values
    
    def preorder_traversal(self):
        return self._preorder_traversal_recursive(self.root)
    
    def _preorder_traversal_recursive(self, current_node):
        if not current_node:
            return []
        
        left_values = self._preorder_traversal_recursive(current_node.left)
        right_values = self._preorder_traversal_recursive(current_node.right)
        return [current_node.value] + left_values + right_values
    
    def postorder_traversal(self):
        return self._postorder_traversal_recursive(self.root)
    
    def _postorder_traversal_recursive(self, current_node):
        if not current_node:
            return []
        
        left_values = self._postorder_traversal_recursive(current_node.left)
        right_values = self._postorder_traversal_recursive(current_node.right)
        return  left_values + right_values + [current_node.value] 
    
    def height(self):
        return self._height_recursive(self.root)
    
    def _height_recursive(self, current_node):
        if not current_node:
            return 0
        
        left_height = self._height_recursive(current_node.left)
        right_height = self._height_recursive(current_node.right)
        return 1 + max([left_height, right_height])
    
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current_node, value):
        if not current_node:
            return None

        if value < current_node.value:
            current_node.left = self._delete_recursive(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._delete_recursive(current_node.right, value)
        else:
            if not current_node.left:
                return current_node.right
            elif not current_node.right:
                return current_node.left

            temp = self._find_min_node(current_node.right)
            current_node.value = temp.value
            current_node.right = self._delete_recursive(current_node.right, temp.value)

        return current_node

    def _find_min_node(self, node):
        while node.left:
            node = node.left
        return node

binaryTree2 = BinaryTree2()
binaryTree2.insert(5)
binaryTree2.insert(3)
binaryTree2.insert(7)
binaryTree2.insert(2)
binaryTree2.insert(4)
binaryTree2.insert(6)
binaryTree2.insert(8)

print("Inorder Traversal:",  binaryTree2.inorder_traversal())
print("Preorder Traversal:", binaryTree2.preorder_traversal())
print("Postorder Traversal:",binaryTree2.postorder_traversal())


print("Tree Height:", binaryTree2.height())

binaryTree2.delete(7)
print("Inorder Traversal after deleting 7:", binaryTree2.inorder_traversal())   






            

        



        

