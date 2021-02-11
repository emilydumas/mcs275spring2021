"""Fibonacci numbers implemented with recursion"""
# MCS 275 Spring 2021 Lecture 12

import decs

def fib(n):
    """nth fibonacci number"""
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def fib_iterative(n):
    """nth fibonacci number (iteratively)"""
    if n <= 1:
        return n
    # TODO: Convert this to a version that
    # only ever stores two Fibonacci numbers.
    L = [1,1]
    while len(L) < n:
        L.append(L[-1]+L[-2])
    return L[-1]

if __name__=="__main__":
    import sys
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 5

    fib_timed = decs.timed(fib) # timed version
    fib_iterative_timed = decs.timed(fib_iterative) # timed version

    result = fib_timed(n)
    result_iterative = fib_iterative_timed(n)

    print("fib({}) = {} (recursive)".format(n,result))
    print("fib({}) = {} (iterative)".format(n,result_iterative))
