#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = my_list.index(search)
    my_list[a] = replace
    return my_list
