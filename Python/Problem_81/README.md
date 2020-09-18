# Problem 81 Solution

## The Problem
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

![](https://latex.codecogs.com/gif.latex?\begin{pmatrix}&space;\color{red}{131}&space;&&space;673&space;&&space;234&space;&&space;103&space;&&space;18\\&space;\color{red}{201}&space;&&space;\color{red}{96}&space;&&space;\color{red}{342}&space;&&space;965&space;&&space;150\\&space;630&space;&&space;803&space;&&space;\color{red}{746}&space;&&space;\color{red}{422}&space;&&space;111\\&space;537&space;&&space;699&space;&&space;497&space;&&space;\color{red}{121}&space;&&space;956\\&space;805&space;&&space;732&space;&&space;524&space;&&space;\color{red}{37}&space;&&space;\color{red}{331}&space;\end{pmatrix})


## My Solution
Using brute 
```python
Initial Matrix  <class 'numpy.ndarray'>
Shape  (3, 3)
[10  1  2]
[ 5  1 10]
[15  5 10]

Cumulative sum of first row
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
