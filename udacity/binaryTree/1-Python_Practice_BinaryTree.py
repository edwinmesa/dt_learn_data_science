# this code was generate by chatgpt

# Full binary tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None
    
def build_full_binary_tree():
    root       = TreeNode(1)
    # level order traversal to construct full binary tree from given array of values
    root.left        = TreeNode(2)
    root.right       = TreeNode(3)
    root.left.left   = TreeNode(4)
    root.left.right  = TreeNode(5)
    root.right.left  = TreeNode(6)
    root.right.right = TreeNode(7)

    return root

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.value))
        printTree(node.right, level + 1)

# # Example usage:
# if __name__ == "__main__":
full_binary_tree_root = build_full_binary_tree()
printTree(full_binary_tree_root)

print('*' * 60)
#************************************************************************#

# Complete Binary Tree:

def build_complete_binary_tree():
    root            = TreeNode(1)
    root.left       = TreeNode(2)
    root.right      = TreeNode(3)
    root.left.left  = TreeNode(4)
    root.left.right = TreeNode(5)

    return root 

complete_binary_tree_root = build_complete_binary_tree()
printTree(complete_binary_tree_root)