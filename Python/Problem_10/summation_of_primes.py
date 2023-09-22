""" --------------------------------------------------------------------------
                       PROJECT EULER   -   PROBLEM 10                  
                                                                           
               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo/Project-Euler                            
-------------------------------------------------------------------------- """
from number_theory.numbers import primes

primes = primes(n_limit=2000000)

# Get the sum of primes below 2e6
sum(list(primes))