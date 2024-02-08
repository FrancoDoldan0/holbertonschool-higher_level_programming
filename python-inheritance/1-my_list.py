#!/usr/bin/python3

class MyList(list):

    def print_sorted(self):
        newlist = self[:]
        newlist.sort()
        print(newlist)
