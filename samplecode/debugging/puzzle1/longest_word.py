"""Debugging puzzle: Script to find longest word in a text file
and the number of times it appears (case-insensitive)."""
# MCS 275 Spring 2021 Lecture 11

# This script is written in a way that avoids some constructions
# that would make the code more concise (e.g. list comprehensions).
# This gives more lines of code to step through during debugging.

import sys

punctuation = ".,;:-'\""

def lower_line_words(s):
    """Break a line of text into words, converted to lower case"""
    # Replace punctuation with whitespace
    for c in punctuation:
        s = s.replace(c," ")
    # Split into words, which may be capitalized
    raw_words = s.split()
    # Normalize capitalization
    lower_words = []
    for w in raw_words:
        lower_words.append(w.lower())
    return lower_words

def lower_file_words(fobj):
    """Take an open text file object and return a list of words
    in the file (all lower case)"""
    filewords = []
    for line in fobj:
        linewords = lower_line_words(line)
        filewords += linewords
    return filewords

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Exactly one argument required: input filename")
        exit(1)
    with open(sys.argv[1],"rt",encoding="UTF-8") as infile:
        wordlist = lower_file_words(infile)
    hist = dict()
    for word in wordlist:
        if word not in hist:
            hist[word] = 0
        hist[word] += 1
    # Find maximum length, then record all words of that length
    # TODO: Make this more efficient by doing it all in one pass
    maxlen = max( [len(word) for word in hist] )
    maxwords = [word for word in hist if len(word)==maxlen]

    # Report results
    print("The longest word length was {} characters.".format(maxlen))
    print("There were {} word(s) of this length:".format(len(maxwords)))
    for word in maxwords:
        print("Word \"{}\" ocurred {} times".format(word,hist[word]))

