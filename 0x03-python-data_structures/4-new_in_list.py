#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_my_list = my_list.copy()
    list_len = len(my_list)
    if idx < 0:
        return copy_my_list
    elif idx >= list_len:
        return copy_my_list
    else:
        copy_my_list[idx] = element
        return copy_my_list
