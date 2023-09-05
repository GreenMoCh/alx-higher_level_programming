#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a (int or float): first number to be added
        b (int or float): second number to be added

    Returns:
        int: the sum of a and b

    Raises:
        TypeError: if a or b is neither an int nor a float
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (int(a + b))
