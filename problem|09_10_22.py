# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
# and deserialize(s), which deserializes the string back into the tree.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node = Node('root', Node('left', Node('left.left', Node('left.left.left'))), Node('right', None, Node('right.right', Node('right.right.left'))))


def serialise(root):
    if root:
        # return the value of the root node, then the left node, then the right node
        return root.val + " " + serialise(root.left) + " " + serialise(root.right)
    else:
        return "None"

# def deserialize(s):

# The following test should pass:
# assert deserialize(serialize(node)).left.left.val == 'left.left'

print(serialise(node))
