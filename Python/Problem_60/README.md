# Problem 60 Solution

## The Problem

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

[Source](https://projecteuler.net/problem=60)

## My Solution

My first attempt to solve this problem involved checking if two primes concatenate to produce another prime by looking in a large prime list:

```python 
large_prime_list = list(primes(n_primes=1000000))

check_math = lambda x,y: (int(str(x)+str(y)) in large_prime_list) and
                         (int(str(y)+str(x)) in large_prime_list)
```

This seemed very inefficient and runtime was getting long. I researched more efficient algorithms and came across the [Miller-Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test). Prompting my first implantation of a probabilistic primality test approach and creating Python function [number_theory.properties.is_prime()](../number_theory/properties.py) as a helper function. By using the Miller-Rabin primality test I successfully generated a solution and reduced runtime to less than 2 seconds.