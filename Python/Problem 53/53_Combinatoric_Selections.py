""" --------------------------------------------------------------------------
                       PROJECT EULER   -   PROBLEM 53                     
                                                                           
               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """
import math
import numpy as np

def main():

    # Problem 53 asks to analysis n from 1<=n<=100
    # but we know it's not until n=23 & r=10 that we first exceed 1 million
    # thus we can limit our analys to the range between 23 <= n < 100
    n_range = range(23,101)
    low_limit = 1000*1000

    ans = calc_combs(n_range,low_limit)

    str_out = "There are {} combinations of (n,r) for 1<=n<=100\n".format(ans) +\
              "which are greater than {:,}".format(low_limit)
    print(str_out)

def calc_combs(nrange,lim):
    """
    Parameters
    ----------
    nrange: range
        range of n values to consider

    lim: int
        lower combination result limit
    
    Returns
    -------
    vals: int
        Sum of, not necessarily distinct, values of (n,r) such
        that their combinatoric sets are greater than lim
    """

    # where n and r are combinatoric parameters 
    combs = [reverse_factorial(n,n-r)/math.factorial(n-r) for n in nrange
             for r in range(0,n-1)]

    vals = np.greater_equal(combs,lim)

    return sum(vals)

def reverse_factorial(n,x):
    """
    Parameters
    ----------
    n: int

    x: int
        Where x = n - r 

    Returns
    -------
    f: int
        Combination result for n and r

    Notes
    -----
        This functions uses a simplified reverse factorial formula 
        to quickly caclulate a combination result
    """

    f = 1
    for i in range(0,x):
        f = f*(n-i)

    return f

if __name__ == '__main__':
    main()