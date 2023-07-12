# this code was generate by chatgpt

def is_palindrome(string):
    if len(string) <= 1:  # base case: empty string or single character is a palindrome
        return True
    elif string[0] != string[-1]:  # base case: characters at the ends don't match, not a palindrome
        return False
    else:
        # recursive call to check inner substring
        return is_palindrome(string[1:-1])


word = "radar"
result = is_palindrome(word)

if result:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not palindrome")

print('*' * 60)
# ************************************************************************#


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)  # recursive call for left subtree
        print(node.value) # visit the current node
        in_order_traversal(node.right) # recursive call for right subtree


# Create the binary tree
root             = Node(1) # 1
root.left        = Node(2) # 2,1
root.right       = Node(3) # 2,1,3
root.left.left   = Node(4) # 4,2,1,3
root.right.right = Node(5) # 4,2,1,3,5

# Performing in-order traversal
print("In-order traversal:")
in_order_traversal(root)
