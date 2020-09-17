""" --------------------------------------------------------------------------
                       PROJECT EULER   -   PROBLEM 18                     
                                                                           
               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """
import numpy as np

def main():

    calculation("num_triangle.txt")

def calculation(fname):
    """
    Parameter
    ---------
    f: str
        path to text file

    Notes
    -----
    This module was created to be use in problem 67

    """
    
    with open(fname) as f:
        tri = [[int(i) for i in line.split()] for line in f ]
    
    for i in range(len(tri)-1,0,-1):
        slast,last = tri[i-1], tri[i]
        tri[i-1] = np.maximum(last[:-1],last[1:]) + slast

    str_out = "The total maximum sum from top to bottom\n" +\
              "or bottom to top ;) is : {}".format(int(tri[0]))

    print(str_out)

    return None

if __name__ == '__main__':
    main()
