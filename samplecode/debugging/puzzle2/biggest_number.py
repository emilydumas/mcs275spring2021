"""Debugging puzzle: Script to find largest integer in a
text file (allowing Python int literal syntax for hexadecimal,
binary, etc.)"""
# MCS 275 Spring 2021 Lecture 11

# This script is written in a way that avoids some constructions
# that would make the code more concise (e.g. list comprehensions).
# This gives more lines of code to step through during debugging.

import sys

punctuation = ".,;:-'\""

def line_words(s):
    """Break a line of text into words"""
    # Replace punctuation with whitespace
    for c in punctuation:
        s = s.replace(c," ")
    return s.split()

def is_bin_digit(c):
    """Check whether character c is a binary digit"""
    return c in "01"

def is_hex_digit(c):
    """Check whether character c is a hexadecimal digit"""
    return c in "0123456789abcdefABCDEF"

def is_octal_digit(c):
    """Check whether character c is an octal digit"""
    return c in "01234567"

def looks_like_integer(w):
    """Does string w look like an integer literal?"""
    if w.isdigit():
        return True
    if w[:2] == "0x":
        return all( [is_hex_digit(c) for c in w[2:]] )
    if w[:2] == "0b":
        return all( [is_bin_digit(c) for c in w[2:]] )
    if w[:2] == "0o":
        return all( [is_octal_digit(c) for c in w[2:]] )
    return False

def to_integer(w):
    """Convert a string to an integer, allowing binary, hex, and octal"""
    if w.isdigit():
        return int(w)
    if w[:2] == "0x":
        return hex(w)
    if w[:2] == "0b":
        return bin(w)
    if w[:2] == "0o":
        return oct(w)

def line_integers(s):
    """Find integer literals on a line and return a list of 
    corresponding integers"""
    words = line_words(s)
    integers = []
    for w in words:
        if looks_like_integer(w):
            integers.append(to_integer(w))
    return integers

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Exactly one argument required: input filename")
        exit(1)
    values = []
    with open(sys.argv[1],"rt") as infile:
        for line in infile:
            values += line_integers(line)
    
    print(max(values))