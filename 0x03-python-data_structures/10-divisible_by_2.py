#!/usr/bin/python
def divisible_by_2(my_list=[]):
    n_list = []
    if my_list:
        for num in my_list:
            n_list.append(False if num % 2 else True)
        return n_list
