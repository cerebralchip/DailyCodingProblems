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

def deserialiser(nodes):
    # get the first node in the list
    val = nodes.pop(0)
    # if the value is None, return None
    if val == "None":
        return None
    # otherwise, create a new node with the value
    node = Node(val)
    # call the function recursively to get the left and right nodes
    node.left = deserialiser(nodes)
    node.right = deserialiser(nodes)
    return node

def deserialise_root(s):
    # split string into list
    nodes = s.split()
    #call recursive function to build tree
    return deserialiser(nodes)



# The following test should pass:
assert deserialise_root(serialise(node)).left.left.val == 'left.left'

print(deserialise_root(serialise(node)))
