"""Paper folding sequence"""
# MCS 275 Spring 2021 Lecture 13
# Emily Dumas

# PFS(1)   1
# PFS(2)   110
# PFS(3)   1101100
# PFS(4)   110110011100100

def invert(L):
    """Switch 0<-->1 in sequence L"""
    return [ 1-x for x in L ]

def reverse(L):
    """Return L in opposite order"""
    return L[::-1]

def pfs(n):
    """Return the nth paper folding sequence"""
    if n==1:
        return [1]
    prev = pfs(n-1)
    return prev + [1] + invert(reverse(prev))

if __name__=="__main__":
    import sys
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 4
    pfs_str = ''.join([str(i) for i in pfs(n)])
    print("pfs({}) = {}".format(n,pfs_str))
