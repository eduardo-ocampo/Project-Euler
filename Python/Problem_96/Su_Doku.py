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
    # grid_num = 'Grid 50'

    # Initialize soluiton list, and counter
    sol_list, count = [], 0

    # Solve each grid
    for grid_num in gs_keys:

        print("Original grid:")
        display_grid(grids,[grid_num])
        grid_result = solve_grid(grids,grid_num)
        print("Solution: ")
        display_grid(grids,[grid_num])

        if grid_result:
            count += 1
            sol_list.append(read_digits(grids,grid_num))

    ans = "{} grid(s) were solved. The summation of each first\n".format(count) +\
          "three cells in the top left of each solved grid is: {}".format(sum(sol_list))
    print(ans)

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
        
    for grid in grid_keys:
        str_grid = grid + '\n\n'

        for j, r in enumerate(grid[grid]):
            if str(j) in '36':
                str_grid += '- - - - + - - - - + - - - -\n'
        
            str_grid += ' '.join(str(c)+ (' |' if str(i) in '25' else ' ') 
                for i, c in enumerate(r)) + '\n'

        print(str_grid)

    return None

def solve_grid(grid,grid_num):
    """
    Parameters
    ----------
    grid: dict
        Dictionary data structure containing Suduko grids
        See read_file() in Su_Doku.py for more information

    grid_num: str
        Grid number from dictionary grid. Used as key value when analyzing
        cells, or grids.

        Example: grid_num = 'Grid 06'

    Returns
    -------
    bool
    
    Notes
    -----
    Solves Suduko grid by first passing it through take_steps(). If a 
    solution is found the function will return True. If not, the function
    will begin to guess a value at the cell with the least amount of 
    possible solution. If that too leads to a dead end the function will
    back track and try the next cell with the least amount of possible solutions. 
    
    """

    if take_steps(grid,grid_num):
        return True

    else:

        # Begin taking a guess at the cell with least amount of 
        # possible solutions 
        min_vals = [[row,col] for cv in range(2,10) 
                              for row,col in product(range(9),repeat=2) 
                              if len(grid[grid_num][row][col]) == cv]

        for row_idx,col_idx  in min_vals:
            # Copying grid to eliminate any unwanted modifications to the
            # original grid structure
            copied_grid = copy.deepcopy(grid)

            for mv_vals in copied_grid[grid_num][row_idx][col_idx]:

                # take a guess at cell (row_idx,col_idx) but keep 
                # original value for reference
                original_val = copied_grid[grid_num][row_idx][col_idx]
                copied_grid[grid_num][row_idx][col_idx]= mv_vals

                # If guess works return True, if not try the next cell
                if take_steps(copied_grid,grid_num):
                    grid[grid_num] = copied_grid[grid_num]
                    return True

                # set value at cell (row_idx,col_idx) back 
                copied_grid[grid_num][row_idx][col_idx]= original_val

    return False

def take_steps(grid,grid_num):
    """
    Parameters
    ----------
    grid: dict
        Dictionary data structure containing Suduko grids
        See read_file() in Su_Doku.py for more information

    grid_num: str
        Grid number from dictionary grid. Used as key value when analyzing
        cells, or grids.

        Example: grid_num = 'Grid 06'

    Returns
    -------
    bool
    
    Notes
    -----
    
    """

    solve_progress = [0,1]

    for i in range(10):
        if solve_progress[-1] == solve_progress[-2]:

            # Try naked pair strategy
            SuDokuStrategies.naked_pairs(grid,grid_num)

            if SuDokuStrategies.check_if_solved(grid,grid_num) == solve_progress[-2]:
                break
        
        # Check if there exists any solved cells
        SuDokuStrategies.solve_cells(grid,grid_num)

        # Reduce cell possibilites
        SuDokuStrategies.reduce_cells(grid,grid_num)

        # Check if cells have a hiddne single solution
        SuDokuStrategies.hidden_singles(grid,grid_num)

        cells_solved = SuDokuStrategies.check_if_solved(grid,grid_num)
        solve_progress.append(cells_solved)

        if cells_solved == 81:
            return True

    return False

def read_digits(grid,grid_num):

    row_res = [(i) for i in grid[grid_num][0][0:3]]
    res = int(''.join(row_res))

    return res

if __name__ == '__main__':
    main()