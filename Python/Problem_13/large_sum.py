""" --------------------------------------------------------------------------
                       PROJECT EULER   -   PROBLEM 13                  
                                                                           
               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo/Project-Euler                            
-------------------------------------------------------------------------- """
import numpy as np

def get_sum(file,truncate):
    """
    Gets sum of numbers in file and returns the result up to the first X
    digits as set by parameter truncate.
    """

    f = open(file)
    lines = f.readlines()
    f.close()

    numbers = np.array([int(f.rstrip('\n')) for f in lines])
    ans = sum(numbers)

    trunc_ans = int(str(ans)[:truncate])

    return trunc_ans