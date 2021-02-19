"""Quicksort: another example of divide and conquer"""
# MCS 275 Spring 2021 Lecture 17
# David Dumas

def quicksort(L,start=0,end=None):
    """Reorder elements of L so that L[start:end] is sorted."""
    if end == None:
       end = len(L)
    # TODO: Add code here!


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
