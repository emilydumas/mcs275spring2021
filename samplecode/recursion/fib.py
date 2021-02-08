"""Fibonacci numbers implemented with recursion"""
# MCS 275 Spring 2021 Lecture 12

def fib(n):
    """nth fibonacci number"""
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

if __name__=="__main__":
    import sys
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 5
    print("fib({}) = {}".format(n,fib(n)))
