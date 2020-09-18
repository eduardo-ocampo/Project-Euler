""" --------------------------------------------------------------------------
                       PROJECT EULER   -   PROBLEM 81                     
                                                                           
               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """
import numpy as np

def main():

    fname = "matrix.txt"
    with open(fname) as f:
        matrix = np.array([[int(i) for i in line.split(',')] for line in f ])

    # sum first columm 
    matrix[0] = np.cumsum(matrix,axis=1)[0]
    ans = sum_row(matrix)
    str_out = "The minimal path sum is: {}".format(ans)
    print(str_out)

def sum_row(matrix):
    """
    Parameters
    ----------
    martix: np.ndarray

    Notes
    -----
    Recursively analysis each row and determine which direction to head
    """
    try:
        matrix[1][0] += matrix[1-1][0]
    except IndexError: # break out when among the last 1
        a = matrix[-1][-1]
        return a
    
    for i in range(1,len(matrix[1])):
        matrix[1][i] += min(matrix[0][i],matrix[1][i-1])
    
    a = sum_row(matrix[1:][:])

    return a

if __name__ == '__main__':
    main()
