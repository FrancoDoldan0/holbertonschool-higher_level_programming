#!/usr/bin/python3
def uppercase(str):
    for stri in str:
        upercase = stri
        if ord(stri) >= ord("a") and ord(stri) <= ord("z"):
            upercase = chr(ord(stri) - 32)

        print("{}".format(upercase), end="")
    else:
        print()
