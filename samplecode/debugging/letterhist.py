"""Read a file containing a word list, and display a histogram of
first letters.  (This is the post-debugging version.)"""
# MCS 275 Spring 2021 - David Dumas
# Lecture 10

# The files "words1.txt", "words2.txt", ... are sample inputs
# for this program.

import sys

def first_letter_hist(wordlist):
    """Take a list of words, `wordlist`, and return a
    dict that gives a histogram of first letter
    frequencies (converting everything to lowercase)."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    counts = { c:0 for c in alphabet }
    for word in wordlist:
        # Uncomment the next line for print() debugging
        #print("Processing word:",word)
        first_char = word[0]
        first_char = first_char.lower()
        # Uncomment the next line for print() debugging
        #print("Incrementing count for first_char=",first_char)
        counts[first_char] += 1
    return counts

fn = sys.argv[1]
with open(fn,"rt") as infile:
    inwords = [ line.strip() for line in infile ]

hist = first_letter_hist( [ x for x in inwords if x!="" ] )
numwords = sum( [ hist[k] for k in hist ] )

print("Distribution of first letters in {} words read from {}:".format(
    numwords,
    fn
))
for c in sorted(hist.keys()):
    if hist[c] > 0:
        print("{}: {}".format(c,hist[c]))

