"""Binary trees"""
# MCS 275 Spring 2021 - Emily Dumas
# Lecture 20

class Node:
    """Node in a binary tree"""
    def __init__(self,key,parent=None,left=None,right=None):
        """Initialize a new node with given key, parent, and
        children"""
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def set_left(self,other):
        """Make node `other` the left child of this one"""
        self.left = other
        other.parent = self

    def set_right(self,other):
        """Make node `other` the right child of this one"""
        self.right = other
        other.parent = self

    def __str__(self):
        """Minimal string representation showing the key"""
        return "<" + str(self.key) + ">"

    def __repr__(self):
        """Show the same string as __str__"""
        return str(self)


if __name__=="__main__":
    import treevis
    A = Node(56)
    A.set_left(Node(21))
    A.set_right(Node(60))

    # A.left has key 21
    # these are its children
    A.left.set_left(Node(13))
    A.left.set_right(Node(39))

    # A.right has key 60
    # these are its children
    A.right.set_left(Node(58))
    A.right.set_right(Node(72))

    # A.left.left has key 13
    # these are its children
    A.left.left.set_left(Node(11))
    A.left.left.set_right(Node(20))

    # A.right.left has key 58
    # these are its children
    A.right.left.set_left(Node(57))
    A.right.left.set_right(Node(59))

    # A.right.right has key 72
    # these are its children
    A.right.right.set_left(Node(70))
    A.right.right.set_right(Node(80))

    # A.left.left.left has key 11
    # these are its children
    A.left.left.left.set_left(Node(6))

    print("Here is a sample tree:")
    treevis.treeprint(A)