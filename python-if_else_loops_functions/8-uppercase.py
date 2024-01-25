#!/usr/bin/python3
def uppercase(str):
    for stri in str:
        if ord(stri) >= ord("a") and ord(stri) <= ord("z"):
            print("{}".format(stri), end="")
        else:
            print()
