"""Quicksort: another example of divide and conquer"""
# MCS 275 Spring 2021 Lecture 17
# Unfinished; we'll implement partition() in Lecture 18!
# David Dumas

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
    # There is a placeholder implementation below that uses
    # convenient built-in features of Python instead of the
    # swap-based approach we'll discuss in lecture.  It is
    # probably best to ignore it for now.
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    # .
    if end == None:
        end = len(L)
    pivot = L[end-1]
    first_part = [x for x in L[start:end] if x < pivot]
    last_part = [x for x in L[start:end-1] if x >= pivot]
    L[start:end] = first_part + [pivot] + last_part
    return start+len(first_part)
