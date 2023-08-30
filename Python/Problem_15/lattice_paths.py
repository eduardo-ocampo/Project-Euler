""" --------------------------------------------------------------------------
                       PROJECT EULER   -   PROBLEM 15                  
                                                                           
               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo/Project-Euler                            
-------------------------------------------------------------------------- """
import math

def get_routes(n_grid):
    """
    Get all possible routes for getting from the top left corner of a NxN grid
    to the bottom right corner by only being able to move right and down.
    """

    # Assumes square grid
    total_moves = n_grid*2
    num_right_moves = n_grid

    combinations = math.factorial(total_moves) / (math.factorial(num_right_moves)*math.factorial(total_moves-num_right_moves))

    return combinations
