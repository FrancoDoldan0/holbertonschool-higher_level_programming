#!/usr/bin/python3
def search_replace(my_list, search, replace):

    mylist1 = list(map(lambda x: replace if x == search else x, my_list))
    return (mylist1)
