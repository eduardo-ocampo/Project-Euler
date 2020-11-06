""" --------------------------------------------------------------------------
                       PROJECT EULER   -   PROBLEM 96                     
                                                                           
               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """
import copy
from itertools import product 
import SuDokuStrategies

def main():
    f_name = 'sudoku.txt'
    grids = read_file(f_name)

    # Get all grid keys
    gs_keys = list(grids.keys())
    # gs_keys = ['Grid 06']
    # gs = 'Grid 50'

    # Initialize soluiton list, and counter
    sol_list, count = [], 0

    # Solve each grid
    for gs in gs_keys:

        print("Original grid:")
        display_grid(grids,[gs])
        grid_result = solve_grid(grids,gs)
        print("Solution: ")
        display_grid(grids,[gs])

        if grid_result:
            count += 1
            sol_list.append(read_digits(grids,gs))

    ans = "{} grid(s) were solved. The summation of each first\n".format(count) +\
          "three cells in the top left of each solved grid is: {}".format(sum(sol_list))
    print(ans)

def solve_grid(grid,grid_num):


    if take_steps(grid,grid_num):
        return True

    else:

        # first strategies did not work
        # begin taking a guess and backtrack if needed
        min_vals = [[row,col] for cv in range(2,10) 
                              for row,col in product(range(9),repeat=2) 
                              if len(grid[grid_num][row][col]) == cv]
        # for cv in count_vals:
        #     for row,col in product(range(9),repeat=2):
        #         if len(grid[grid_num][row][col]) == cv:
        #             # print(grids[gs][row][col])
        #             min_vals.append([row,col])
        #             # break
        
        # print("Wokring area")
        # print("min vals:",min_vals)
        # return False
        # sec_check = False
        # print(min_vals)
        for row_idx,col_idx  in min_vals:
            # row_idx,col_idx = min_idx
            # if check_solved_grid == True:
            #     break
            # if sec_check == True:
            #     # check_solved_grid == True
            #     return True
            # print("Copying grid")
            copied_grid = copy.deepcopy(grid)
            for mv_vals in copied_grid[grid_num][row_idx][col_idx]:
                original_val = copied_grid[grid_num][row_idx][col_idx]
                # print("mv: ",mv_vals)
                # print(og_val)
                # print("Taking guess {} at {}".format(mv_vals,copied_grid[gs][mv[0]][mv[1]]))
                # print(grids[gs][min_vals[0][0]][min_vals[0][1]][0])
                copied_grid[grid_num][row_idx][col_idx]= mv_vals
                # copied_grid[gs][min_vals[0][0]][min_vals[0][1]] = '5'
                # sec_check = take_steps(copied_grid,grid_num)
                if take_steps(copied_grid,grid_num):
                    # print("Solved during second check")

                    grid[grid_num] = copied_grid[grid_num]

                    return True
                copied_grid[grid_num][row_idx][col_idx]= original_val

    return False

def read_digits(g,gs):

    row_res = [(i) for i in g[gs][0][0:3]]
    res = int(''.join(row_res))

    return res

def take_steps(g,gs):

    solve_progress = [0,1]
    # display_grid(g,sel_grids=[gss])

    for i in range(10):
        if solve_progress[-1] == solve_progress[-2]:
            # Try naked pair strategy
            SuDokuStrategies.naked_pairs(g,gs)

            if SuDokuStrategies.check_if_solved(g,gs) == solve_progress[-2]:
                break
            
            # continue
        # print("iteration: ",i)
        SuDokuStrategies.solve_cells(g,gs)
        # display_grid(grids,sel_grids=[gs])

        SuDokuStrategies.reduce_cells(g,gs)
        # display_grid(g,sel_grids=[gs])

        SuDokuStrategies.hidden_singles(g,gs)
        # display_grid(g,sel_grids=[gs])

        cells_solved = SuDokuStrategies.check_if_solved(g,gs)
        solve_progress.append(cells_solved)

        # print(ch)
        if cells_solved == 81:
            # print("Solved {}, \n\titerations = {} ".format(gss,i))
            # cou += 1
            return True

    return False
   
def read_file(f):
    """"
    Parameter
    ---------
    f: string
        file name
    
    Returns
    -------
    d: dict
        dictionary data sctructure

    Notes
    -----
    This function extracts the Sudoku grids from file f and stores them
    into a dictionary data structure. Where the Grid number is the key
    and the value is a 2D list containing the So Doku grid values.

    Examples
    --------
    >>> print(read_file('sudoku.txt'))
    {'Grid 01': 
    [['0', '0', '3', '0', '2', '0', '6', '0', '0'],
     ['9', '0', '0', '3', '0', '5', '0', '0', '1'],
     ['0', '0', '1', '8', '0', '6', '4', '0', '0'],
     ['0', '0', '8', '1', '0', '2', '9', '0', '0'],
     ['7', '0', '0', '0', '0', '0', '0', '0', '8'],
     ['0', '0', '6', '7', '0', '8', '2', '0', '0'],
     ['0', '0', '2', '6', '0', '9', '5', '0', '0'],
     ['8', '0', '0', '2', '0', '3', '0', '0', '9'],
     ['0', '0', '5', '0', '1', '0', '3', '0', '0']]}

    """

    with open(f) as fn:
        lines = fn.read().splitlines()
        grid_d = {lines[i].strip(): [list(lines[i+j]) for j in range(1,10)] 
                    for i in range(0,len(lines),10)}

    return grid_d

def display_grid(grid,sel_grids=None):
    """
    Parameters
    ----------
    grid: dict
        Dictionary data structure containing Suduko grids
        See read_file() for more information

    sel_grids: None or list
        By default set to None and will print out all Suduko grids 
        within parameter grid_d. If list of grid key(s) are passed
        only those will be printed out to the user.

    Returns
    -------
    None
        Displays grid by printing it to user see example below

    Examples
    --------
    >>> grids = read_file('sudoku.txt')
    >>> display_grid(grids,['Grid 06])
    1  0  0 | 9  2  0 | 0  0  0 
    5  2  4 | 0  1  0 | 0  0  0 
    0  0  0 | 0  0  0 | 0  7  0 
    - - - - + - - - - + - - - -
    0  5  0 | 0  0  8 | 1  0  2 
    0  0  0 | 0  0  0 | 0  0  0 
    4  0  2 | 7  0  0 | 0  9  0 
    - - - - + - - - - + - - - -
    0  6  0 | 0  0  0 | 0  0  0 
    0  0  0 | 0  3  0 | 9  4  5 
    0  0  0 | 0  7  1 | 0  0  6
    """

    if not sel_grids:
        grid_keys = grid.keys()
    elif isinstance(sel_grids,list):
        grid_keys = sel_grids
        
    for g in grid_keys:
        str_grid = g + '\n\n'

        for j, r in enumerate(grid[g]):
            if str(j) in '36':
                str_grid += '- - - - + - - - - + - - - -\n'
        
            str_grid += ' '.join(str(c)+ (' |' if str(i) in '25' else ' ') 
                for i, c in enumerate(r)) + '\n'

        print(str_grid)

    return None

if __name__ == '__main__':
    main()