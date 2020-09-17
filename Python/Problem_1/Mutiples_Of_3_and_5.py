""" --------------------------------------------------------------------------
                       PROJECT EULER   -   PROBLEM 1                          
                                                                           
               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """
import numpy as np 

def main():

    limit = 1000
    multiples = [3,5]

    x = find_multiples(limit, multiples)

    str_out = "The sum of all the multiples {} below {} is: {}"
    print(str_out.format(multiples,limit,x))
    
def find_multiples(lim,mults):
    """
    Parameters
    ----------
    lim: int
        Limiting natural number

    mults: list
        List of multiples to analysis

    Returns:
    --------
    ans: int
        Sum of all multiples (mults) below limiting number
    """

    # list comprehensions to the rescue
    ans = [i for j in mults for i in range(lim) if np.mod(i,j)==0]

    # return the sum and also remove any duplicates
    return sum(np.unique(ans))

if __name__ == '__main__':
    main()