#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = my_list.index(search)
    new_list = my_list
    new_list[a] = replace
    return new_list
