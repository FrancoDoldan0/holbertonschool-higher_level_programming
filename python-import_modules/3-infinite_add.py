#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    numeros = sys.argv[1:]
    if numeros == 0:
        print(argv())

    suma = sum(int(arg) for arg in numeros)
    print(suma)
