"""Binary search trees"""
# MCS 275 Spring 2021 - David Dumas
# Lecture 20

from binary import Node

class BST:
    """Binary search tree"""
    def __init__(self):
        """Initialize an empty BST with root None"""
        self.root = None

    def insert(self,x):
        """Take a node `x` and insert it into the BST in
        a suitable place"""

    def search(self,k):
        """Look for a node with key `k` and return it if
        found, or return None if there is no such node."""
        self._search(k,self.root)

    def _search(self,k,base):
        """Look for a node with key `k` in the subtree
        with root `base` and return it if found,
        or return None if there is no such node."""
        if base == None:
            return
        # Now we know base is an actual `Node` object
        if k == base.key:
            return base
        # Now we know we know we need to proceed to
        # either the left or right subtree
        if k < base.key:
            return self.search(k,base.left)
        else:
            return self.search(k,base.right)
        
