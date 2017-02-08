#!/usr/bin/python3

import sys

if (len(sys.argv) != 2):
    print("Usage: ./soln.py <swears text file>")
    sys.exit(0)

inFile = open(sys.argv[1], "r")
