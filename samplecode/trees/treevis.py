"""Functions for making visualizations of tree structures"""
# MCS 275 Spring 2021 - David Dumas

def treeprint(T):
    """Print a basic text-graphic representation of
    BST or node `T`"""
    print(treestr(T))

def treestr(T):
    """Convert BST or node `T` to a text-graphic string"""
    if hasattr(T,"root"):
        root = T.root
    else:
        root = T
    s = ""
    L = level_lists(root)
    L = [ [node_str(x) for x in row] for row in L ]
    depth = len(L)
    maxlen = len(max(L,key=lambda row:max(len(x) for x in row)))
    final_row_len = (maxlen+1)*(2**depth)-1
    depth = len(L)
    for k,row in enumerate(L):
        width = (final_row_len - (2**k-1)) // 2**k
        s += "\n" + " ".join(x.center(width) for x in row) + "\n"
    return s[1:]

def level_lists(node,L=None,n=0,idx=0):
    """Convert a tree into a list of lists, where
    the k^th list has 2**k elements that are either
    None or nodes of the original tree.  Each list
    represents one of the levels of the tree."""
    if node == None:
        return
    if L==None:
        L=[]
    if len(L)<=n:
        L.append([ None for _ in range(2**n) ])
    L[n][idx] = node
    level_lists(node.left,L,n+1,2*idx)
    level_lists(node.right,L,n+1,2*idx+1)
    return L

def node_str(x):
    """Convert a node to a string, or convert None to
    the empty string"""
    if x == None:
        return ""
    else:
        return str(x)