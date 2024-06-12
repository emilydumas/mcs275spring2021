"""Decorators for use in recursion discussion"""
# MCS 275 Spring 2021
# Emily Dumas

import time
from functools import wraps

def timed(f):
    """Decorator to print running time when f is called"""
    # NOTE: Does not support keyword arguments at the moment!
    fname = f.__name__
    @wraps(f)  # copies docstring and name of f
    def inner(*args):
        t_start = time.time()
        ret = f(*args)
        t_end = time.time()
        print("{}({}) total time: {:.3f} seconds".format(
            fname,
            ",".join([str(x) for x in args]),
            t_end-t_start
        ))
        return ret
    return inner


CALLS = {}


def count_calls(f):
    """Decorator to count number of calls by function name"""
    fname = f.__name__
    @wraps(f)  # copies docstring and name of f
    def inner(*args,**kwargs):
        f.__doc__
        if fname not in CALLS:
            CALLS[fname] = 0
        CALLS[fname] += 1
        return f(*args,**kwargs)
    return inner

ARG_CALLS = {}


def count_arg_calls(f):
    """Decorator to count number of calls by function name and arguments"""
    # NOTE: Does not support keyword arguments at the moment!
    fname = f.__name__
    @wraps(f)  # copies docstring and name of f
    def inner(*args):
        f.__doc__
        key = (fname,*args)
        if key not in ARG_CALLS:
            ARG_CALLS[key] = 0
        ARG_CALLS[key] += 1
        return f(*args)
    return inner


def print_call_counts():
    """Display counts of function calls in a nice table"""
    if CALLS:
        digits = [ len(str(x)) for x in CALLS.values() ]
        digits.append(5)
        maxdigits = max(digits)
        namechars = [ len(k) for k in CALLS ]
        namechars.append(4)
        maxnamechars = max(namechars)
    else:
        maxdigits = 5
        maxnamechars = 4
    
    print("func{}calls".format(" "*(maxnamechars-2)))
    print("-"*(maxnamechars+maxdigits+2))
    rowstr = "{: <"+str(maxnamechars)+"}  {: >"+str(maxdigits)+"}"
    for k,v in sorted(CALLS.items(),key=lambda x:x[1]):
        print(rowstr.format(k,v))


def func_call_str(T):
    """Convert (f,arg,arg,...) to string f(arg,arg,...)"""
    return "{}({})".format(T[0],",".join([str(x) for x in T[1:]]))


def print_arg_call_counts():
    """Display counts of function calls with arguments in a nice table"""
    if ARG_CALLS:
        digits = [ len(str(x)) for x in ARG_CALLS.values() ]
        digits.append(5)
        maxdigits = max(digits)
        namechars = [ len(func_call_str(k)) for k in ARG_CALLS ]
        namechars.append(4)
        maxnamechars = max(namechars)
    else:
        maxdigits = 5
        maxnamechars = 4
    
    print("func{}calls".format(" "*(maxnamechars-2)))
    print("-"*(maxnamechars+maxdigits+2))
    rowstr = "{: <"+str(maxnamechars)+"}  {: >"+str(maxdigits)+"}"
    for k,v in sorted(ARG_CALLS.items(),key=lambda x:x[1]):
        print(rowstr.format(func_call_str(k),v))



CACHE = {}

def memoize(f):
    """Simple caching decorator"""
    # NOTE: Does not support keyword arguments at the moment!
    fname = f.__name__
    @wraps(f)  # copies docstring and name of f
    def inner(*args):
        f.__doc__
        key = (fname,*args)
        if key in CACHE:
            return CACHE[key]
        else:
            res = f(*args)
            CACHE[key] = res
            return res
    return inner
