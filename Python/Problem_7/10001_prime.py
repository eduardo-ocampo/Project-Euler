""" --------------------------------------------------------------------------
                       PROJECT EULER   -   PROBLEM 7                  
                                                                           
               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo/Project-Euler                            
-------------------------------------------------------------------------- """
from number_theory import primes

primes = primes(n_primes=10001)

# Get last prime number in list
list(primes)[-1]