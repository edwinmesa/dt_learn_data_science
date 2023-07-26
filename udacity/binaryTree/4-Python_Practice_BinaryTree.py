# this code was generate by chatgpt
from collections import deque
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None
    

class ExpressionTree:
    def __init__(self):
        self.root = None
    
    def build_expression_tree(self, postfix_expression):
        operand_stack = []

        for token in postfix_expression:
            if token.isdigit():
                operand_stack.append(BinaryTreeNode(int(token)))
            else:
                right_operand = operand_stack.pop()
                left_operand  = operand_stack.pop()
                operator_node = BinaryTreeNode(token)
                # set the child nodes of current node to be its operands and operators from stack
                operator_node.left  = left_operand
                operator_node.right = right_operand
                operand_stack.append(operator_node)
        self.root = operand_stack.pop()
    
    def evaluate(self):
        """Evaluate expression tree"""
        return self._evaluate_recursive(self.root)
    
    def _evaluate_recursive(self, current_node):
        # if not isinstance(current_node, BinaryTreeNode):   ## base case - reached leaf node
            # (integer number or variable name). Return it as is.
        if not current_node:
            return 0
        
        if current_node.value.isdigit():
            return int(current_node.value)
        
        left_value  = self._evaluate_recursive(current_node.left)
        right_value = self._evaluate_recursive(current_node.right)

        if current_node.value == '+':
            return left_value + right_value
        elif current_node.value == '-':
            return left_value - right_value
        elif current_node.value == '*':
            return left_value * right_value
        elif current_node.value == '/':
            return left_value / right_value
        
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
        
expression = "3 4 + 5 * 6 -"
postfix_tokens = expression.split()
expression_tree = ExpressionTree()
expression_tree.build_expression_tree(postfix_tokens)
print("Postfix Expression Tree:")
expression_tree.print_tree()

result = expression_tree.evaluate()
print("Result:", result)