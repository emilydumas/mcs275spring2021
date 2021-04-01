# MCS 275 Spring 2021 Project 3 Solution
# David Dumas

# Project description:
# https://www.dumas.io/teaching/2021/spring/mcs275/nbview/projects/project3.html

"""
Reads a list of chromaticities and names from the CSV file
(name given as first command line argument) and provides a
lookup service using keyboard input.  Each time the user
enters a chromaticity in the format
  r g b
the name will be found and printed, or a message will be
shown indicating the chromaticity was not in the CSV file.
Entering a blank line ends the program.
"""

import sys
import csv
from chroma import Chroma, ChromaNameMapping

if len(sys.argv) != 2:
    print("ERROR: Required command line argument missing.\n")
    print("Usage: {} FILENAME".format(sys.argv[0]))
    print("Reads chromaticity dictionary from FILENAME (CSV)")
    print("then performs interactive name lookup.")
    sys.exit(1)

names = ChromaNameMapping()
with open(sys.argv[1], "rt", newline="") as infile:
    rdr = csv.DictReader(infile)
    for row in rdr:
        components = [int(row[k]) for k in ("red", "green", "blue")]
        c = Chroma(*components)
        names[c] = row["name"]

# Main command loop: Read a line, parse it, look it up
for line in sys.stdin:
    line = line.strip()  # ignore leading and trailing whitespace
    # blank line?  If so, exit the loop (ending the program)
    if not line:
        break

    # Attempt to make a Chromaticity from the values on the input line.

    # By converting all of the items on the line into integers and passing them
    # to Chroma(), there is a chance of a failure due to non-integer values
    # (generating a ValueError at int(x)), values that do not for a chromatcitiy
    # (generating a ValueError at Chroma(...)), or the wrong number of values,
    # generating a TypeError at Chroma(...).

    try:
        fields = [int(x) for x in line.split()]
        c = Chroma(*fields)
    except (ValueError, TypeError):
        print("<invalid>")
        continue

    # Here we use Python's feature where multiple exception types can be caught
    # in a single except block by giving a tuple of exception types.  This is
    # included as a nice demonstration of a code-saving move in cases where
    # several exception types need to be handled in the same way.  This wasn't
    # something we covered in lecture though, so it was expected you would do
    # the same thing with e.g.
    #     except ValueError:
    #         print("<invalid>")
    #         continue
    #     except TypeError:
    #         print("<invalid>")
    #         continue
    # or by manually checking for the correct number of arguments before calling
    # Chroma()

    # Find the chromaticity's name
    try:
        print(names[c])
    except KeyError:
        print("<not found>")
