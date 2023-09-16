# Problem 3 Solution

## The Problem

The prime factors of 13195 are 5,7,13, and 29. What is the largest prime factor of the number 600851475143?

[Source](https://projecteuler.net/problem=3)

## My Solution

Instead of reinventing the "number theory" wheel, for some of my solutions I will utilize Python package [SymPy](https://www.sympy.org/en/index.html). 

For this example, a good approach would be to wrap [Fermat's factorization](https://en.wikipedia.org/wiki/Fermat%27s_factorization_method) method as a Python Class that takes a positive integer n and returns a dict containing n's prime factors and their number of occurrences. Instead I will use SymPy's builtin funciton `factorint()` to accomplish the same result and take the largest prime factor.

```python 
import sympy
print(sympy.factorint(600851475143))
```