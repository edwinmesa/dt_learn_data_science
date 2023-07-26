# this code was generate by chatgpt
from collections import deque


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
        if not current_node:
            return False
        if current_node.value == value:
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
        return left_values + right_values + [current_node.value]

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, current_node):
        if not current_node:
            return 0
        left_height = self._height_recursive(current_node.left)
        right_height = self._height_recursive(current_node.right)
        return 1 + max(left_height, right_height)

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
    
    def is_bst(self):
        return self._is_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_bst_recursive(self, current_node, min_val, max_val):
        if not current_node:
            return True

        if current_node.value <= min_val or current_node.value >= max_val:
            return False

        return (
            self._is_bst_recursive(current_node.left, min_val, current_node.value)
            and self._is_bst_recursive(current_node.right, current_node.value, max_val)
        )

    def lowest_common_ancestor(self, node1_value, node2_value):
        return self._lowest_common_ancestor_recursive(self.root, node1_value, node2_value)

    def _lowest_common_ancestor_recursive(self, current_node, node1_value, node2_value):
        if not current_node:
            return None

        if current_node.value == node1_value or current_node.value == node2_value:
            return current_node.value

        left_lca = self._lowest_common_ancestor_recursive(current_node.left, node1_value, node2_value)
        right_lca = self._lowest_common_ancestor_recursive(current_node.right, node1_value, node2_value)

        if left_lca and right_lca:
            return current_node.value

        return left_lca if left_lca else right_lca

    def print_tree(self):
        levels = self._level_order_traversal()
        for level in levels:
            print(level)

    def _level_order_traversal(self):
        levels = []
        if not self.root:
            return levels

        queue = deque()
        queue.append(self.root)

        while queue:
            level_values = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels.append(level_values)

        return levels

binary_tree = BinaryTree()
binary_tree.insert(5)
binary_tree.insert(3)
binary_tree.insert(7)
binary_tree.insert(2)
binary_tree.insert(4)
binary_tree.insert(6)
binary_tree.insert(8)

print("Is Binary Search Tree:", binary_tree.is_bst())
    # Output: True

print("Lowest Common Ancestor of 2 and 4:", binary_tree.lowest_common_ancestor(2, 4))
    # Output: 3

print("Binary Tree:")
binary_tree.print_tree()      
    









            

        



        

