"""Demonstrate tree traversals"""
# MCS 275 Spring 2021 - David Dumas
from treeutil import random_bst
from treevis import treeprint

# TODO: Define traversal function(s)

if __name__=="__main__":
    print("Tree:")
    T = random_bst(nodes=6)
    treeprint(T)
    # Now T is an object of class `BST`
    # Its root (a `Node` object) is T.root
    
    # RUN TRAVERSAL HERE