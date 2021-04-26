#!/usr/bin/env python3
"""Compute a power of an integer"""
# MCS 275 Spring 2021 argparse example
# Based on Python module documentation example from
#   https://docs.python.org/3/howto/argparse.html
import argparse

parser = argparse.ArgumentParser() #description="Compute a power of an integer"
parser.add_argument(
    "base",
    help="base, i.e. number to be raised to a power",
    type=int  # if not specified, default type is string
)
parser.add_argument(
        "-v",
        "--verbose",
        help="enable more detailed output",
        action="store_true"
)
parser.add_argument(
        "-p",
        "--power",
        help="exponent",
        type=int,
        default=2,
)
args = parser.parse_args()  # parse or show error and exit

if args.verbose:
    print("I am about to raise {} to power {}".format(
        args.base,
        args.power)
    )
    
print(args.base**args.power) # arguments and options are attributes of
                      # the `args` object returned above
if args.verbose:
    print("Successful computation. exiting.")

