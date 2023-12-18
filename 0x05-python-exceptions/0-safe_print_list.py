#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    Args:
        my_list (list): List to print elements from.
        x (int): Number of elements to print.

    Returns:
        Number of elements to be printed.
    """

    try:
        count = 0
        for element in my_list:
            if count < x:
                print(element, end='')
                count += 1
        print()
        return count
    except:
        return count
