"""Generate random binary search trees"""
# MCS 275 Spring 2021 - Emily Dumas
# NOTE: This module won't work until we add the `insert()`
# method to class `BST` in Lecture 21.
from binary import *
from bst import *
import random

def random_bst(nodes=6,seed=None):
    """Generate a BST by inserting `nodes` distinct values
    in random order.  If `seed` is given, use it as the 
    seed for the random number generator (to make it possible
    to reproduce the same tree again later, if desired)."""
    if seed == None:
        R = random
    else:
        R = random.Random(seed)
    x = R.randrange(nodes)
    T = BST()
    keys = []
    for _ in range(nodes):
        keys.append(x)
        x += 1 + R.randrange(4 + nodes//10)
    R.shuffle(keys)
    for k in keys:
        T.insert(Node(k))
    return T


def random_bst_and_node(nodes=6,seed=None):
    """Return a random BST and a node in it."""
    T,x,y = random_bst_and_node_pair(nodes=nodes,seed=seed,distinct=False)
    return T,x

def random_bst_and_node_pair(nodes=6,seed=None,distinct=False):
    """Return a random BST and two nodes in that tree.  If 
    `distinct` is True, the two nodes returned will be distinct."""
    if distinct and nodes<2:
        raise ValueError("Impossible to select two distinct nodes in a tree with {} nodes".format(nodes))
    T = random_bst(nodes=nodes,seed=seed)
    # It *is* possible to select nodes at random without making a temporary list of size
    # equal to the number of nodes, but we use a less space efficient strategy that is
    # easier to understand by reading the code.
    if seed == None:
        R = random
    else:
        R = random.Random(seed)
    L = all_descendants(T.root)
    if distinct:
        x,y=R.sample(L,k=2)
    else:
        x,y=R.choices(L,k=2)
    return T,x,y


def all_descendants(x):
    """Return a list of node `x` and all its descendants"""
    if x == None:
        return
    L=[x]
    if x.left:
        L += all_descendants(x.left)
    if x.right:
        L += all_descendants(x.right)
    return L