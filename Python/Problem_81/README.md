# Problem 81 Solution

## The Problem
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cbegin%7Bpmatrix%7D%5Ccolor%7Bred%7D%7B131%7D%20%26%20673%20%26%20234%20%26%20103%20%26%2018%5C%5C%5Ccolor%7Bred%7D%7B201%7D%20%26%20%5Ccolor%7Bred%7D%7B96%7D%20%26%20%5Ccolor%7Bred%7D%7B342%7D%20%26%20965%20%26%20150%5C%5C630%20%26%20803%20%26%20%5Ccolor%7Bred%7D%7B746%7D%20%26%20%5Ccolor%7Bred%7D%7B422%7D%20%26%20111%5C%5C%20537%20%26%20699%20%26%20497%20%26%20%5Ccolor%7Bred%7D%7B121%7D%20%26%20956%5C%5C805%20%26%20732%20%26%20524%20%26%20%5Ccolor%7Bred%7D%7B37%7D%20%26%20%5Ccolor%7Bred%7D%7B331%7D%5Cend%7Bpmatrix%7D)

Find the minimal path sum from the top left to the bottom right by only moving right and down in [matrix.txt](matrix.txt), a text file containing an 80 by 80 matrix.


## My Solution
Using brute 
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
