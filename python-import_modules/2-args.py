#!/usr/bin/python3
import sys

args = sys.argv[1:]
arguments = str(args)

if len(args) == 0:
    print(len(args), "arguments.", end="\n",)
else:
    print("{} {}{}".format(len(args), "arguments", ":"), end=("\n"))
    for i, arg in enumerate(args, 1):
        print("{}: {}".format(i, arg))
