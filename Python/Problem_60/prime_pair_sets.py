""" --------------------------------------------------------------------------
                       PROJECT EULER   -   PROBLEM 60                  
                                                                           
               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo/Project-Euler                            
-------------------------------------------------------------------------- """
from number_theory.numbers import primes
from number_theory.properties import is_prime
from number_theory.properties import get_prime_pair_candidates

# Upper numerical limit
num_primes = 2000

primes_list = list(primes(n_primes=num_primes))
# Remove numbers that will most likely not result in prime string
primes_list.remove(2)
primes_list.remove(5)

# Check to see if xy and yx are primes
check_match = lambda x,y: is_prime(int(str(x)+str(y))) and \
                          is_prime(int(str(y)+str(x)))

# Initialize 4 and 5 prime candidates list
quad_candidates, quint_candidates = [], []

# Limit how many initial primes to run
first_pair_indx_limit = 10

for indx_1, prime_1 in enumerate(primes_list[:first_pair_indx_limit]):
    candidates = get_prime_pair_candidates(primes_list[indx_1:])

    # Not worth going further if number of prime candidates 
    # won't result in 5 primes 
    if len(candidates) < 4:
        continue

    for indx_2, prime_2 in enumerate(candidates[1:-1]):

        for indx_3, prime_3 in enumerate(candidates[indx_2+1+1:-1]):

            if check_match(prime_2,prime_3):

                for indx_4, prime_4 in enumerate(candidates[(indx_2+indx_3+1+1+1):-1]):

                    if check_match(prime_2,prime_4) and \
                       check_match(prime_3,prime_4):

                        quad_candidates.append([prime_1,prime_2,prime_3,prime_4])

                        for indx_5, prime_5 in enumerate(candidates[(indx_2+indx_3+indx_4+1+1+1+1):]):

                            if check_match(prime_2,prime_5) and \
                               check_match(prime_3,prime_5) and \
                               check_match(prime_4,prime_5):

                                quint_candidates.append([prime_1,prime_2,prime_3,prime_4,prime_5])