""" --------------------------------------------------------------------------
                       PROJECT EULER   -   PROBLEM 52                     
                                                                           
               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """

def main():

    int_range = range(1,1000*1000)

    # first find numbers which contain the exact same digits and area doubles
    # within int_range. This will reduce the numbers to analysis in the next step
    ans = find_matching_mult(2,int_range)

    # run ans intergers against mults 1,2,3,4,5,6
    for x in range(1,6):
        ans = find_matching_mult(x,ans)

    str_out = "Smallest possible interger = {}".format(min(ans))
    print(str_out)

def find_matching_mult(mult,num_range):
    """
    Parameters:
    -----------
    mult: int
        Multiple to compare against

    num_rnage: list
        iterable containing a list of intergers to analysis

    Returns:
    --------
    nums: list
    
    """

    nums = [n for n in num_range if len(str(n)) == len(str(n*mult)) and \
           sorted(str(n)) == sorted(str(n*mult))]

    return nums

if __name__ == '__main__':
    main()