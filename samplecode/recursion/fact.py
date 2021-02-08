"""Factorial implemented with recursion"""
# MCS 275 Spring 2021 Lecture 12

def fact(n):
    """Factorial of nonnegative integer `n`"""
    print("fact({}) started".format(n))
    if n <= 1:
        print("n={} so fact() returns answer immediately".format(n))
        return 1
    print("Making recursive call")
    x = fact(n-1)
    print("fact({}) finished".format(n))
    return n*x

if __name__=="__main__":
    import sys
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 5
    print("{}! = {}".format(n,fact(n)))
