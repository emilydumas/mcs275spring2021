"""Set of integers (using BST)"""
# MCS 275 Spring 2021 Lecture 21

from bst import BST
from binary import Node

class IntegerSet:
    """Set of integers supporting insert and
    membership testing"""
    def __init__(self):
        """Initialize an empty integer set"""
        self.T = BST()

    def insert(self,k):
        """Add integer `k` to the set"""
        self.T.insert(Node(k))

    def contains(self,k):
        """Test whether `k` is in the set"""
        return self.T.search(k) != None
