#!/usr/bin/python
def divisible_by_2(my_list=[]):
    n_list = []
    for num in range(len(my_list)):
        if my_list[num] % 2 == 0:
            n_list.append(True)
        else:
            n_list.append(False)
    return n_list
