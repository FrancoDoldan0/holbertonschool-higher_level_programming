def uppercase(str):
        if ord(str) >= ord("a") and ord(str) <= ord("z"):
            print("{}".format(str.swapcase()))
        else:
            print()
