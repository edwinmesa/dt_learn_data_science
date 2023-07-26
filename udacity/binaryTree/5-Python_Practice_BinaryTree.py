# this code was generate by chatgpt
class TreeNode:
    def __init__(self, name) -> None:
        self.name  = name
        self.left  = None
        self.right = None

def build_family_tree():
    # grandparents
    gp_mother = TreeNode("Grandma")
    gp_father = TreeNode("Grandpa")

    # Parents
    mother = TreeNode("Mother")
    father = TreeNode("Father")

    mother.left  = gp_mother
    father.right = gp_father

    # Children
    child1 = TreeNode("Child1")
    child2 = TreeNode("Child2")

    child1.left  = mother
    child1.right = father
    child2.left  = mother
    child2.right = father

    # Return the root of the family tree
    return child1

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.name))
        printTree(node.right, level + 1)

family_tree_root = build_family_tree()
printTree(family_tree_root)


