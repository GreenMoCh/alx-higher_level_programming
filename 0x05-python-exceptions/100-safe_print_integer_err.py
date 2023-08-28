#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        formatted_value = "{:d}".format(value)
        print(formatted_value)
        return (True)
    except (ValueError, TypeError):
        print("Exception: Incorrect value type", file=sys.stderr)
        return (false)
