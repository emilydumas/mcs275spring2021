"""Fibonacci numbers implemented with recursion"""
# MCS 275 Spring 2021 Lecture 12, 13

import decs  # provides timing and other decorators

def fib_recursive(n):
    """nth fibonacci number"""
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_iterative(n):
    """nth fibonacci number (iteratively)"""
    if n <= 1:
        return n
    x,y = 1,1 # store two consecutive Fib numbers
    for _ in range(n-2):
        x,y = y,x+y # replace (F_{k-1},F_k) with (F_k,F_{k+1})
    return y

if __name__=="__main__":
    import sys
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 5

    print("TIMING:")
    # In case the recursive one takes too long, we allow
    # it to be cancelled with Control-C
    try:
        result_recursive = decs.timed(fib_recursive)(n)
    except KeyboardInterrupt:
        print("fob_recursive({}) total time: unknown (interrupted)".format(n))
        result_recursive = "unknown (interrupted)"
    result_iterative = decs.timed(fib_iterative)(n)

    print("RESULTS:")
    print("fib_recursive({}) = {}".format(n,result_recursive))
    print("fib_iterative({}) = {}".format(n,result_iterative))
