""" --------------------------------------------------------------------------
                       PROJECT EULER   -   Number Theory Module:
                                           A Collection of Number Properties 

               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo/Project-Euler                            
-------------------------------------------------------------------------- """
import math

def is_square(x, round_to=4):
    """
    Simple method for checking if number x is a perfect square.
    Computes and round the square root of x and compares to its original
    value. If unchanged then x is a perfect square. 

    Parameters
    ----------
    x: int
        Integer Number

    round_to: None or list
        Decimal precession when getting square root of x

    Returns
    -------
    bool
        Returns True if x is a perfect square

    Examples
    --------
    >>> is_square(81)
    True
    >>> is_square(151)
    False

    """

    if not isinstance(x,int):
        raise TypeError("x must be of type int")

    sqrt_x = round(math.sqrt(x),round_to)
    sqrt_test = sqrt_x*sqrt_x

    return sqrt_test == x