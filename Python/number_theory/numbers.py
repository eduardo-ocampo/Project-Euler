""" --------------------------------------------------------------------------
                       PROJECT EULER   -   Number Theory Module:
                                           A Collection of Number Sequences

               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo/Project-Euler                            
-------------------------------------------------------------------------- """
import math
import collections
from itertools import compress

class primes(collections.abc.Iterator):
    """
    Iterator containing the primes numbers up to a specified bound either 
    a number limit or number of primes to return. Relies on sieving algorithm
    known as Sieve of Eratosthenes. 

    Parameters
    ----------
    n_limit: None or int
        Upper number limit to consider when searching for primes numbers.
        For example, if n_limit = 10 the algorithm  will search all primes
        number up to number 10. 

        n_limit = 10
        primes numbers = [2, 3, 5, 7]

    n_primes: None or int
        Number of first ascending prime numbers to get. For example, if 
        n_primes = 10. Will return the first 10 primes numbers:

        n_primes = 10
        prime numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


    Returns
    -------
    Iterator
        Prime numbers

    Examples
    --------
    >>> temp_primes = primes(n_limit=50)
    >>> list(temp_primes)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    >>> len(temp_primes)
    15
    >>> sum(temp_primes)
    328
    
    >>> temp_primes = primes(n_primes=1001)
    >>> list(temp_primes)[-1]
    7927
    >>> len(temp_primes)
    1001
    >>> sum(temp_primes)
    3690840

    """

    def __init__(self,n_limit=None,n_primes=None):
        
        # Require either n_limit or n_primes to be passed in...
        if (n_limit is None) and (n_primes is None):
            msg_out = "Set either upper number limit (n_limit) " +\
                      "or number of primes to get (n_primes)"
            raise TypeError(msg_out)

        # but not both!
        if (n_limit and n_primes):
            msg_out = "Can't have both number limit (n_limit) and " +\
                      "number of primes (n_primes) specified. " +\
                      "Stick with either one or another" 
            raise TypeError(msg_out)

        elif n_primes:
            # Approximate for nth prime number
            # https://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number
            limit_approx = n_primes*(math.log(n_primes)+math.log(math.log(n_primes)))
            # Set sieve limit
            self._p_limit = int(limit_approx)

            # # Get prime numbers
            # primes_boolean = self.sieve_of_eratosthenes()
            # # Map prime boolean array to numbers
            # self._primes = list(compress(range(len(primes_boolean)),primes_boolean))

        elif n_limit:
            # Set sieve limit
            self._p_limit = n_limit

        # Get prime numbers
        primes_boolean = self.sieve_of_eratosthenes()
        # Map prime boolean array to numbers
        self._primes = list(compress(range(len(primes_boolean)),primes_boolean))      

        # Ensure number of primes is not over approximated using method n_primes
        if n_primes:
            self._n_primes = n_primes
        else:      
            # Remove num 1 from len list of primes
            self._n_primes = len(self._primes) - 1

    def __len__(self):
        return self._n_primes

    def __iter__(self):
        self._i = 0
        return self
    
    def __next__(self):
        if self._n_primes <= self._i:
            raise StopIteration
        
        # Skips number 1 as it is not a prime number
        self._i += 1

        return self._primes[self._i]

    def sieve_of_eratosthenes(self):
        """
        https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

        Algorithm for finding all prime numbers up to and including number self._p_limit.
        Assumes 0 is not a prime number. 

        Returns
        -------
        list
            Boolean list of numbers up to self._p_limit where True 
            denotes a prime number for the number associated with that index.

        Examples
        --------
        >>> self._p_limit = 10 # First 10 numbers
        >>> self.sieve_of_eratosthenes() 
        [None, True, True, True, False, True, False, True, False, False, False]

        """

        p_bound = self._p_limit+1

        # Initialize Boolean Array, 0 based
        number_array = [True]*p_bound
        number_array[0] = None 

        # Start with first prime number 2
        p = 2

        while (p*p <= p_bound):

            # Is prime
            if number_array[p] == True:
                
                # Multiples of p are not prime
                for m in range(p*p,p_bound,p):
                    number_array[m] = False
            
            # Move on to next number
            p += 1

        return number_array