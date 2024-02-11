#!/usr/bin/python3
"""Write a function that reads
a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """ Read file"""
    with open(filename, 'r', encoding="utf-8") as t:
        cont = t.read()
        print(cont, end="")
