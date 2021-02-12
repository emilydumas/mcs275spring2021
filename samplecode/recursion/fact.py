"""Factorial implemented with recursion"""
# MCS 275 Spring 2021 Lecture 12, 13

def fact(n):
    """Factorial of nonnegative integer `n`"""
    if n <= 1:
        return 1
    x = fact(n-1)
    return n*x

def fact_iterative(n):
    """Factorial, iteratively"""
    accum = 1
    for k in range(2,n+1):
        accum *= k
    return accum

if __name__=="__main__":
    import sys
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 5
    print("{}! = {} (iterative)".format(n,fact_iterative(n)))
    print("{}! = {} (recursive)".format(n,fact(n)))
