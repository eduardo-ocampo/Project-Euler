""" --------------------------------------------------------------------------
                       PROJECT EULER   -   PROBLEM 96                     
                                                                           
               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """
import copy
from itertools import product 

def solve_cells(grid,grid_num):
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
    None
        The passed Suduko grid will contain the updated cell values after 
        processed through this function

    Notes
    -----
    
    """

    nums = {str(i) for i in range(1,10)}
    
    for row,col in product(range(9),repeat=2):

        # Check if solution exists at (row,col)
        if len(grid[grid_num][row][col]) == 1 and int(grid[grid_num][row][col]) != 0:
            continue

        # get row, col, and box set
        row_set = set(r for r in grid[grid_num][row] if len(r)==1)
        col_set = set(grid[grid_num][i][col] for i in range(len(grid[grid_num]))  if len(grid[grid_num][i][col])==1)
        
        x = lambda a: a // 3 * 3
        box_set = set( b for i in range(x(row),x(row)+3) 
                         for b in grid[grid_num][i][x(col):x(col)+3] if len(b)==1)
        
        used_vals = row_set | col_set | box_set 
        
        if '0' in used_vals:
            used_vals.remove('0')
        
        avail_vals = nums - used_vals

        # Assign possible solutions to cell (row,col)
        grid[grid_num][row][col] = ''.join(avail_vals)

    return None

def reduce_cells(grid,grid_num):
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
    None
        The passed Suduko grid will contain the updated cell values as 
        processed through this function

    Notes
    -----

    """

    progress = [0,1]
    # nums = {str(i) for i in range(1,10)}

    # Copy grid to remove any errors when editing cells from original grid
    copied_grid = copy.deepcopy(grid)

    while((progress[-2]-progress[-1])/2 != 0):

        solve_cells(copied_grid,grid_num)
        # for row,col in product(range(9),repeat=2):

        #     # Check if solution exists at (row,col)
        #     if len(copied_grid[grid_num][row][col]) == 1 and int(copied_grid[grid_num][row][col]) != 0:
        #         continue

        #     # get row, col, and box set
        #     row_set = set(r for r in copied_grid[grid_num][row] if len(r)==1)
        #     col_set = set(copied_grid[grid_num][i][col] for i in range(len(copied_grid[grid_num]))  
        #                                           if len(copied_grid[grid_num][i][col])==1)
            
        #     x = lambda a: a // 3 * 3
        #     box_set = set( b for i in range(x(row),x(row)+3) 
        #                      for b in copied_grid[grid_num][i][x(col):x(col)+3] if len(b)==1)
            
        #     used_vals = row_set | col_set | box_set 

        #     if '0' in used_vals:
        #         used_vals.remove('0')
            
        #     avail_vals = nums - used_vals
        #     # print("avail_vals: ",avail_vals)
        #     # if len(avail_vals) == 0:
        #         # print("Wowowoowowowow")
        #         # continue


        #     copied_grid[grid_num][row][col] = ''.join(avail_vals)

        progress.append(check_if_solved(copied_grid,grid_num))

    return None

def hidden_singles(grid,grid_num):
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
    None
        The passed Suduko grid will contain the updated cell values as 
        processed through this function

    Notes
    -----

    """
       
    for row,col in product(range(9),repeat=2):

        # only consider cells with more than one possible solution
        if len(grid[grid_num][row][col]) > 1:

            original_list = grid[grid_num][row][col]
            grid[grid_num][row][col] = '0'

            # get row, col, and box set
            row_set = set(c for r in grid[grid_num][row] for c in r)
            col_set = set(c for i in range(len(grid[grid_num]))  for c in grid[grid_num][i][col] )
            
            x = lambda a: a // 3 * 3
            box_set = set( c for i in range(x(row),x(row)+3) 
                            for b in grid[grid_num][i][x(col):x(col)+3] for c in b)

            if len(set(original_list)-row_set) == 1:
                grid[grid_num][row][col] = ''.join(set(original_list)-row_set)
                continue
            if len(set(original_list)-col_set) == 1:
                grid[grid_num][row][col] = ''.join(set(original_list)-col_set)
                continue
            if len(set(original_list)-box_set) == 1:
                grid[grid_num][row][col] = ''.join(set(original_list)-box_set)
                continue

            grid[grid_num][row][col] = original_list

    return None

def naked_pairs(grid,grid_num):
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
    None
        The passed Suduko grid will contain the updated cell values as 
        processed through this function

    Notes
    -----

    """

    for row,col in product(range(9),repeat=2):

        # only consider cells with more than one possible solution
        if len(grid[grid_num][row][col]) > 1:

            # get row, col, and box list
            row_list = list(r for r in grid[grid_num][row] if len(r)>1)
            col_list = list(grid[grid_num][i][col]  for i in range(len(grid[grid_num])) if len(grid[grid_num][i][col] )>1)
            
            # x = lambda a: a // 3 * 3
            # box_set = list( b for i in range(x(row),x(row)+3) 
            #                 for b in grid[grid_num][i][x(col):x(col)+3] if len(b)>1)

            naked_col_val = [x for x in col_list if col_list.count(x) > 1 and len(x) == 2]    

            if naked_col_val and len(naked_col_val) == len(naked_col_val[0]):
                for r in range(0,9):
                    if len(grid[grid_num][r][col]) > 1 and grid[grid_num][r][col] != naked_col_val[0]:
                        for pair in naked_col_val[0]:
                            grid[grid_num][r][col] = grid[grid_num][r][col].replace(pair,"")  

            naked_row_val = [x for x in row_list  if row_list .count(x) > 1 and len(x) == 2]    
            if naked_row_val and len(naked_row_val) == len(naked_row_val[0]):
                for c in range(0,9):
                    if len(grid[grid_num][row][c]) > 1 and grid[grid_num][row][c] != naked_row_val[0]:
                        # print(grid[grid_num][row][w])  
                        for pair in naked_row_val[0]:
                            grid[grid_num][row][c] = grid[grid_num][row][c].replace(pair,"")  

    return None

def check_if_solved(grid,grid_sel):
    """
    Parameters
    ----------
    grid: dict
        Dictionary data structure containing Suduko grids
        See read_file() in Su_Doku.py for more information

    grid_sel: str
        Grid number from dictionary grid. Used as key value when analyzing
        cells, or grids.

        Example: grid_num = 'Grid 06'

    Returns
    -------
    Number of cells which contain a single solution

    """
    copied_grid = copy.deepcopy(grid)
    cell_check = [True for row,col in product(range(9),repeat=2)
                        if len(copied_grid[grid_sel][row][col]) == 1 and int(copied_grid[grid_sel][row][col]) != 0]
    
    return sum(cell_check)   