#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            if count < x:
                try:
                    print("{:d}".format(i), end='')
                    count += 1
                except (ValueError, TypeError):
                    continue
            else:
                break
        print()
        return count
    except TypeError:
        return count
