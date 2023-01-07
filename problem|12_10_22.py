# An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev 
# fields, it holds a field named both, which is an XOR of the next node and the previous node. 
# 
# Implement an XOR linked list

# it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

# If using a language that has no pointers(such as Python), 
# you can assume you have access to get_pointer and dereference_pointer functions that converts 
# between nodes and memory addresses.

class Node:
    def __init__(self, data):
        self.data = data
        self.both = 0
    
    def __str__(self): # for printing
        return str(self.data)
    
class XORLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, element): # adds the element to the end
        #set self.tail.both to the xor of self.tail.both and the address of element
        self.tail.both = self.tail.both ^ get_pointer(element)
        #set element.both to the xor of the address of self.tail and 0
        element.both = get_pointer(self.tail) ^ 0
        #set self.tail to element
        self.tail = element

    def get(self, index): # returns the node at index
        #link(C) = addr(B)⊕addr(D)
        pass
