"""Program with complicated call graph"""
# MCS 275 Spring 2021 - Emily Dumas
# Quiz 5

def f(x):
    """Function that sometimes calls g and/or h, and returns
    or raises exception based on the divisibility of x"""
    if x%88==0:
        raise Exception
    if x%7==0:
        return
    if x%3==0:
        g(x*2+1)
    h(x*3-1)

def g(x):
    """Function that sometimes calls f and/or h, and returns
    or raises exception based on the divisibility of x"""
    if x%12==0:
        raise Exception
    if x%19==0:
        return
    if x%2==0:
        f(x//4+3)
    h(x//3+51)

def h(x):
    """Function that sometimes calls f, and returns
    or raises exception based on the divisibility of x"""
    if x%1063==0:
        raise Exception
    if x%37==0:
        return
    if x%2==0:
        f(x//2+16)
    f(x//3)

f(2752021)
