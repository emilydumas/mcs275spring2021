"""Quicksort: another example of divide and conquer"""
# MCS 275 Spring 2021 Lecture 17 and Lecture 18
# Emily Dumas

def quicksort(L,start=0,end=None,depth=0):
    """Reorder elements of L so that L[start:end] is sorted."""
    # Uncomment the line below for verbose output
    # (this is the only place the `depth` argumen is used
    #print(" "*depth + "quicksort({})".format(L[start:end]))
    if end == None:
       end = len(L)

    if end-start <= 1:
        # zero or one-element lists are always sorted
        return

    # Arrange it so that L[m] is a pivot:
    # Everything less than the pivot is in
    # L[start:m], and everything greater than
    # or equal to the pivot is in L[m+1:end]
    m = partition(L,start,end)
    
    # Recursive calls to quicksort will sort
    # the sublists to either side of the pivot.
    quicksort(L,start,m,depth+1)
    quicksort(L,m+1,end,depth+1)


def partition(L,start=0,end=None):
    """Look at L[start:end].  Take the last element as a pivot.
    Move elements around so that any value less than the pivot 
    appears before it, and any element greater than or equal to
    the pivot appears after it.  L is modified in place.  The
    final location of the pivot is returned."""
    if end == None:
        end = len(L)

    pivot = L[end-1]
    dst = start
    for src in range(start,end):
        if L[src] < pivot:
            L[src], L[dst] = L[dst], L[src]
            # Reminder:
            #   x,y = y,x swaps two values in Python
            #   no need for a temporary variable
            dst += 1
    
    # Put pivot in its correct final place with one
    # last swap
    L[end-1], L[dst] = L[dst], L[end-1]

    # Uncomment the next few lines for some verbose debugging output
    #print("Partitioned: {} {} {}".format(
    #    L[start:dst],
    #    L[dst],
    #    L[dst+1:end]
    #))
    
    return dst
