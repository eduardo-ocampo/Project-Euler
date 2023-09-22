# Problem 10 Solution

## The Problem

The sum of the primes below 10 is 2+3+5+7=17.

Find the sum of all the primes below two million.

[Source](https://projecteuler.net/problem=10)

## My Solution

This is a good complementary problem to [Problem 7](../Problem_7) and shows the functionality of Python Class [number_theory.numbers.primes()](../number_theory/numbers.py). For this problem, we can use the upper number parameter to get all the primes numbers up to 2,000,00 and sum the list. 

```python
# Get the sum of primes below 2e6
sum(list(primes(n_limit=2000000)))
```
