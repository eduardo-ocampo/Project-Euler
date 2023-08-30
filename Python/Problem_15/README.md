# Problem 15 Solution

## The Problem

Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

![](https://projecteuler.net/resources/images/0015.png)

How many such routes are there through a 20x20 grid?

[Source](https://projecteuler.net/problem=15)

## My Solution

I took a combinations approach for this problem. For a 20x20 grid there are a total of 40 decisions right or down dicisions to make. However, not all 40 can be either just right moves. Instead think about the problem as how many ways can you choose 20 rights out of the 40 moves?

$nCr = 
\begin{pmatrix}
n \\
r 
\end{pmatrix}
=
\frac{n!}{r!\left(n-r)!}$

$ 
\begin{pmatrix}
40 \\
20
\end{pmatrix}
=
\frac{40!}{20!20!}$
