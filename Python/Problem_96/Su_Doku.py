""" --------------------------------------------------------------------------
                       PROJECT EULER   -   PROBLEM 96                     
                                                                           
               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """
import copy
import SuDokuStrategies
from itertools import product 

def main():

    f_name = 'sudoku.txt'
    grids = read_file(f_name)

    # Get all grid keys
    gs_keys = list(grids.keys())

    # Initialize soluiton list, and counter
    sol_list, count = [], 0

    # Solve each grid
    for grid_key in gs_keys:

        print("Original grid:")
        display_grid(grids,[grid_key])
        grid_result = solve_grid(grids,grid_key)
        print("Solution: ")
        display_grid(grids,[grid_key])

        if grid_result:
            count += 1
            sol_list.append(read_digits(grids,grid_key))
            
    ans = "{} grid(s) were solved. The summation of the first\n".format(count) +\
          "three cells in the top left of each solved grid is: {}".format(sum(sol_list))

    print(ans)

def read_file(f):
    """"
    Parameter
    ---------
    f: string
        file name containing Sudoku puzzles
    
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

def solve_grid(grid,grid_num):
    """
    Parameters
    ----------
    grid: dict
        Dictionary data structure containing Suduko grids
        See read_file() in Su_Doku.py for more information

    grid_num: str
        Grid number from dictionary grid. Used as key value when analyzing
        specific unsolved cells, or grids.

        Example: grid_num = 'Grid 06'

    Returns
    -------
    bool
    
    Notes
    -----
    Solves Suduko grid by first passing it through take_steps(). If a 
    solution is found the function will return True. If not, the function
    will begin to guess a value at the unsolved cell with the least amount of 
    possible solution. If that too leads to a dead end the function will
    back track and try the next unsolved cell with the least amount of possible
    solutions until a solution is found and returning True.  
    
    """

    if take_steps(grid,grid_num):
        return True

    else:

        # Begin taking a guess at the unsolved cell with least amount of 
        # possible solutions
        min_vals = [[row,col] for cv in range(2,10) 
                              for row,col in product(range(9),repeat=2) 
                              if len(grid[grid_num][row][col]) == cv]

        for row_idx,col_idx  in min_vals:
            # Copying grid to eliminate any unwanted modifications to the
            # original grid data structure
            copied_grid = copy.deepcopy(grid)

            for mv_vals in copied_grid[grid_num][row_idx][col_idx]:

                # take a guess at cell (row_idx,col_idx) but keep 
                # original value for reference
                original_val = copied_grid[grid_num][row_idx][col_idx]
                copied_grid[grid_num][row_idx][col_idx]= mv_vals

                # If guess works return True, if not try the next available
                # unsolved cell
                if take_steps(copied_grid,grid_num):
                    grid[grid_num] = copied_grid[grid_num]
                    return True

                # set value at cell (row_idx,col_idx) back to its
                # original value
                copied_grid[grid_num][row_idx][col_idx]= original_val

    return False

def take_steps(grid,grid_num,n=10):
    """
    Parameters
    ----------
    grid: dict
        Dictionary data structure containing Suduko grids
        See read_file() in Su_Doku.py for more information

    grid_num: str
        Grid number from dictionary grid. Used as key value when analyzing
        specific unsolved cells, or grids.

        Example: grid_num = 'Grid 06'

    n: int
        Number of iterations to take

    Returns
    -------
    bool
    
    Notes
    -----
    This function will take steps in solving a Sudoku puzzle by following
    three strategies:
    1) Using SuDokuStrategies.solve_cells(), check if an unsolved cell has
       only one possible solution and assign it.
    2) Using SuDokuStrategies.reduce_cells(), search across an unsolved
       cell's row, column, and box to remove possible solutions. 
    3) Using SuDokuStrategies.hidden_singles(), at a given unsolved cell
       check to see if a solution is unique to that cell by comparing it
       across its row, column, and box. 

    After all three strategies are used, the grid is checked for number of
    solved cells. Only when all 81 cells are solved will the function will
    return True. If no progress is being made by the three strategies then 
    the SuDokuStrategies.naked_pairs() strategy is used to aid in solving 
    the puzzle.

    """

    solve_progress = [0,1]

    for i in range(n):
        if solve_progress[-1] == solve_progress[-2]:

            # Try naked pair strategy
            SuDokuStrategies.naked_pairs(grid,grid_num)

            if SuDokuStrategies.check_if_solved(grid,grid_num) == solve_progress[-2]:
                break
        
        # Check if there exists any solved cells
        SuDokuStrategies.solve_cells(grid,grid_num)

        # Reduce cell possibilites
        SuDokuStrategies.reduce_cells(grid,grid_num)

        # Check if cells have a hidden single solution
        SuDokuStrategies.hidden_singles(grid,grid_num)

        cells_solved = SuDokuStrategies.check_if_solved(grid,grid_num)
        solve_progress.append(cells_solved)

        if cells_solved == 81:
            return True

    return False

def read_digits(grid,grid_num):
    """
    Parameters
    ----------
    grid: dict
        Dictionary data structure containing Suduko grids
        See read_file() in Su_Doku.py for more information

    grid_num: str
        Grid number from dictionary grid. Used as key value when analyzing
        specific unsolved cells, or grids.

    Returns
    -------
    res: int
        The first 3-digits found at the top left corner of grid_num.

    Examples
    --------
    >>> display_grid(grids,['Grid 06])
    >>> print("Top Left Integers: ",read_digits(grids,grid_key))
    Grid 06

    1  7  6 | 9  2  3 | 5  8  4 
    5  2  4 | 8  1  7 | 6  3  9 
    8  9  3 | 6  5  4 | 2  7  1 
    - - - - + - - - - + - - - -
    9  5  7 | 3  4  8 | 1  6  2 
    6  3  8 | 1  9  2 | 4  5  7 
    4  1  2 | 7  6  5 | 3  9  8 
    - - - - + - - - - + - - - -
    2  6  5 | 4  8  9 | 7  1  3 
    7  8  1 | 2  3  6 | 9  4  5 
    3  4  9 | 5  7  1 | 8  2  6 

    Top Left Integers:  176
    
    """

    row_res = [(i) for i in grid[grid_num][0][0:3]]
    res = int(''.join(row_res))

    return res

if __name__ == '__main__':
    main()