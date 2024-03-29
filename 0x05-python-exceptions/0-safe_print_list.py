#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
    """print x elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x(int): The number of elements from my_list to print

    Returns:
        The number of elements printed
    """
    ret = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
