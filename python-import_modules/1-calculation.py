#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    suma = add(a, b)
    resta = sub(a, b)
    multi = mul(a, b)
    divi = div(a, b)

    print("{} + {} = {}".format(a, b, suma), end="\n")
    print("{} - {} = {}".format(a, b, resta), end="\n")
    print("{} * {} = {}".format(a, b, multi), end="\n")
    print("{} / {} = {}".format(a, b, divi), end="\n")
