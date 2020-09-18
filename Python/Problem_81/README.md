# Problem 81 Solution

## The Problem
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cbegin%7Bpmatrix%7D%5Ccolor%7Bred%7D%7B131%7D%20%26%20673%20%26%20234%20%26%20103%20%26%2018%5C%5C%5Ccolor%7Bred%7D%7B201%7D%20%26%20%5Ccolor%7Bred%7D%7B96%7D%20%26%20%5Ccolor%7Bred%7D%7B342%7D%20%26%20965%20%26%20150%5C%5C630%20%26%20803%20%26%20%5Ccolor%7Bred%7D%7B746%7D%20%26%20%5Ccolor%7Bred%7D%7B422%7D%20%26%20111%5C%5C%20537%20%26%20699%20%26%20497%20%26%20%5Ccolor%7Bred%7D%7B121%7D%20%26%20956%5C%5C805%20%26%20732%20%26%20524%20%26%20%5Ccolor%7Bred%7D%7B37%7D%20%26%20%5Ccolor%7Bred%7D%7B331%7D%5Cend%7Bpmatrix%7D)

Find the minimal path sum from the top left to the bottom right by only moving right and down in [matrix.txt](matrix.txt), a text file containing an 80 by 80 matrix.


## My Solution
It would not be recommended to try every single possible path to solve this problem, as there are 1.075072087 E+23 possible paths. Instead I used an algorithm that would dynamically determine the best minimum path. Below is a short example of the algorithm at work on a 3x3 matrix .


```python
Initial Matrix  <class 'numpy.ndarray'>
Shape  (3, 3)
[10  1  2]
[ 5  1 10]
[15  5 10]

Cumulative Sum of First Row
[10 11 13]

Matrix  <class 'numpy.ndarray'>
Shape  (3, 3)
[10 11 13]
[15 12 22]
[15  5 10]

Matrix  <class 'numpy.ndarray'>
Shape  (2, 3)
[15 12 22]
[30 17 27]

Matrix  <class 'numpy.ndarray'>
Shape  (1, 3)
[30 17 27]
```


To begin either cumulatively sum the first column or row. I decided to perform an initial cumulative sum along the first row (first set of column values). Then move down one row while summing the first two row values, and work your way across the row. Where at each coordinate we sum the smallest of either the left or top value. At the end you will end up with the minimum path sum. For a 80x80 matrix the amount of recursive steps taken was 6,320. Surely a much better approach than comparing 1.075072087 E+23 possible paths
