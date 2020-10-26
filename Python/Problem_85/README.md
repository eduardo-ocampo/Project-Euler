# Problem 85 Solution

## The Problem

By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

![](https://projecteuler.net/project/images/p085.png)

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

## My Solution

### Formula

As an example, consider a one-dimensional mx1 grid. The number of rectangles which can be formed are shown below:
|M | Rectangles|
|--|------------|
|1 |1|
|2 |3|
|3 |6|
|4 |10|
|5 |15|

To form a rectangle we need two vertical and two horizontal lines. A m x n grid has m+1 horizontal lines and n+1 vertical lines. This example has a combinatronic solution when we choose to pick 2 vertical lines from set m+1. 
nCr
The same can be shown for a one-dimensional 1xn grid, The combinatoric solution is:
nCr
For a two-dimensional grid multiply these two solutions to determine how many rectangles can be formed in a mxn grid

Calculation
In this solution, I utilized Numpy’s ability to [broadcast](https://numpy.org/devdocs/user/theory.broadcasting.html) two one-dimensional arrays. Where the first row contains a range of n values and the first column contains a range of m values. The result is a two-dimensional array containing the number of rectangles formed for a sweep of mxn combinations. A similar array was created calculating the mxn grid area. 

The final step is to find the indices where the rectangle number is closest to 2,000,000 and index the grid area array with that information. The heatmaps below illustrate how various combinations of mxn grids approach 2,000,000 rectangles.
