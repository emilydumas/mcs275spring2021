"""Demonstrate tree traversals"""
# MCS 275 Spring 2021 - David Dumas
from treeutil import random_bst
from treevis import treeprint

def preorder(x):
    """Print keys of tree with root `x` using
    preorder traversal"""
    if x:
        print(x)
        preorder(x.left)
        preorder(x.right)

def inorder(x):
    """Print keys of tree with root `x` using
    inorder traversal"""
    if x:
        inorder(x.left)
        print(x)
        inorder(x.right)

if __name__=="__main__":
    print("Tree:")
    T = random_bst(nodes=6)
    treeprint(T)
    # Now T is an object of class `BST`
    # Its root (a `Node` object) is T.root
    
    print("Preorder:")
    preorder(T.root)

    print("Inorder:")
    inorder(T.root)