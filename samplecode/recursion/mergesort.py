"""Mergesort: an example of divide and conquer"""
# MCS 275 Spring 2021 Lecture 16
# Emily Dumas

def mergesort(L):
    """Sort the list L in place.  No return value."""
    # Uncomment the next line for some helpful
    # debugging messages
    #print("mergesort({})".format(L))
    if len(L) <= 1:
        # List has at most one element, so it is
        # already sorted.  Nothing to do.
        return
    
    # SPLIT
    mid = len(L) // 2
    L1 = L[:mid]  # copy first mid elements to new list L1
    L2 = L[mid:]  # copy all but first mid elements to L2

    # SOLVE
    mergesort(L1)
    mergesort(L2)

    # MERGE
    merge_sorted_lists(L1,L2,L)


def merge_sorted_lists(L1,L2,L):
    """Take sorted lists L1 and L2 and a list L whose length
    is len(L1)+len(L2).  Merge L1 and L2, maintaining sorted
    order, storing the results in L.  No return value."""
    i1 = 0  # position in L1
    i2 = 0  # position in L2
    i = 0   # position in L
    while i1<len(L1) and i2<len(L2):
        if L1[i1] <= L2[i2]:
            # Take from L1
            L[i] = L1[i1]
            i1 += 1
        else:
            # Take from L2
            L[i] = L2[i2]
            i2 += 1
        i += 1
    # Copy over any remaining part of L1
    while i1<len(L1):
        L[i] = L1[i1]
        i1 += 1
        i += 1
    # Copy over any remaining part of L2
    while i2<len(L2):
        L[i] = L2[i2]
        i2 += 1
        i += 1


def cheating_merge_sorted_lists(L1,L2,L):
    """Take sorted lists L1 and L2 and a list L whose length
    is len(L1)+len(L2).  Merge L1 and L2, maintaining sorted
    order, storing the results in L.  No return value."""
    # This is a placeholder implementation that uses
    # Python's built-in sorted() function.  It is only here
    # so that we could build and demonstrate mergesort()
    # before writing merge_sorted_lists().
    for i,x in enumerate(sorted(L1+L2)):
        L[i] = x