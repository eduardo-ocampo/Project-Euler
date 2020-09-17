# Problem 67 Solution

## The Problem

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

**3**

**7** 4

2 **4** 6

8 5 **9** 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in [num_triangle.txt](num_triangle.txt), a 15K text file containing a triangle with one-hundred rows.

**NOTE:** This is a much more difficult version of [Problem 18](../Problem_18). It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

## My Solution
This is a more difficult version of [Problem 18](../Problem_18). However, the algorithm used to solve the problem is the exact same. For this reason `Maximum_Path_Sum_II.py` calls and utilizes module ```calculation()``` to solve the puzzle.
