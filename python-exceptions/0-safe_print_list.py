#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    for i in range(0, x):
        try:
            print(my_list[i], end="")
            a += 1
        except Exception:
            break
    print()
    return (a)
