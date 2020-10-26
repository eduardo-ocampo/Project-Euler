""" --------------------------------------------------------------------------
                       PROJECT EULER   -   PROBLEM 85                  
                                                                           
               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """
import numpy as np

def main():

    idxs, rects, ans = calc_area()
    print(ans,rects,idxs)

def calc_area(v=1,h=1):
    """
    Parameters
    ----------
    h: int
        rectangle height, by default set to 1 which can be changed
        to speed up calculation if needed
    
    w: int
        rectangle width, by default set to 1 which can be changed
        to speed up calculation if needed

    Returns
    -------
    A tuple, where parameter sol_idx contains the width and height of a grid
    with the nearest solution, rects[sol_idx] is the number of rectangles
    observed in the grid, and grid_area[sol_idx] is the grid area. 

    """

    h_array = np.arange(v,100)
    w_array = np.arange(h,100).reshape(-1,1)
    
    grid_area = h_array*w_array
    rects = (w_array*w_array+w_array)*(h_array*h_array+h_array)/4

    # find index of rects whose solution is closet to 2e6
    sol_idx = np.unravel_index(abs(rects-2e6).argmin(),rects.shape)

    return sol_idx, rects[sol_idx], grid_area[sol_idx]

if __name__ == '__main__':
    main()