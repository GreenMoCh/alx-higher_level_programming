#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for i in range(x):
        value = my_list[i]
        try:
            formatted_value = "{:d}".format(value)
            print(formatted_value, end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            pass
    print()
    return (count)
