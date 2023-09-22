""" --------------------------------------------------------------------------
                       PROJECT EULER   -   Number Theory Module:
                                           A Collection of Number Properties 

               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo/Project-Euler                            
-------------------------------------------------------------------------- """
import math

def is_square(x, round_to=4):
    """
    Simple method for checking if number x is a perfect square.
    Computes and round the square root of x and compares to its original
    value. If unchanged then x is a perfect square. 

    Parameters
    ----------
    x: int
        Integer Number

    round_to: None or list
        Decimal precession when getting square root of x

    Returns
    -------
    bool
        Returns True if x is a perfect square

    Examples
    --------
    >>> is_square(81)
    True
    >>> is_square(151)
    False

    """

    if not isinstance(x,int):
        raise TypeError("x must be of type int")

    sqrt_x = round(math.sqrt(x),round_to)
    sqrt_test = sqrt_x*sqrt_x

    return sqrt_test == x


def is_prime(n,debug=False):
    """
    Check if number n is likely to be prime. Number must be greater than 1
    and an even number will automatically result in False.

    Calls on the Miller-Rabin Primality Test

    Parameters
    ----------
    x: int
        Number to test 

    Returns
    -------
    bool
        Returns True is number n is likely to be prime


    """

    is_prime = False
    
    # List of first 100 prime numbers
    known_primes = [   2,   3,   5,   7,  11,  13,  17,  19,  23,  29, 
                      31,  37,  41,  43,  47,  53,  59,  61,  67,  71, 
                      73,  79,  83,  89,  97, 101, 103, 107, 109, 113, 
                     127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 
                     179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 
                     233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 
                     283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 
                     353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 
                     419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 
                     467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
    
    if n <= 1:
        msg_out = "To check if n is prime enter a number greater than 1"
        raise ValueError(msg_out)
    # Prime is already known
    elif n in known_primes:
        is_prime = True
    # Is even
    elif n % 2 == 0:
        is_prime = False
    else:
        is_prime = miller_rabin_test(n,debug=debug)

    return is_prime

    
def miller_rabin_test(n,debug=False):
    """
    The Miller-Rabin probabilistic primality testing algorithm:
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Example

    Instead of randomly selecting a number a such that 2 <= a <= n-2, specific 
    numbers at test against are predetermined

    Run debug=True to get test progress.

    """

    mr_is_prime = False

    # Get n as n = (2**r)*d+1
    # print("test to see if {} is prime".format(n))
    m = n-1
    r = 0

    # Find power r from 2**r
    while m%2 == 0:
        m /= 2
        r += 1
    d = int(m)

    if debug:
        print("reduced n to (2**r)*d+1: r = {}, d = {}\n".format(r,d))

    # Testing against small set
    # ---------------------------
    # https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Testing_against_small_sets_of_bases
    if n < 2047:
        test_against = [2]
    elif n < 1373653: 
        test_against = [2,3]
    elif n < 9080191:
        test_against = [31,73]
    elif n < 25326001:
        test_against = [2,3,5]
    elif n < 3215031751:
        test_against = [2,3,5,7]
    elif n < 4759123141:
        test_against = [2,7,61]
    elif n < 1122004669633:
        # test_against = [2,13,23,1662803]
        # https://miller-rabin.appspot.com/
        test_against = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]

    # Test witness
    if debug:
        print("test {} against small set {}".format(n,test_against))
        print("-"*30)

    for a in test_against:
        if debug:
            print("testing a: ",a)

        if mr_is_prime == True:
            break
        
        # Ferments test
        x = pow(a,d,n)
        if (x==1) or (x==n-1):
            if debug:
                print("\tx is either 1 or (n-1)")
                print("\t",x)
            mr_is_prime = True
        
        # Now test powers r against same x
        # x**(2*(d**2))
        for s in range(r):
            x  = pow(x,2,n)

            if debug:
                print("\tr = ",s)
                print("\tin 2 pow test")
                print("\t"+"-"*10)
                print("\tx: ",x)

            # Not prime
            if x == 1:
                if debug:
                    print("\tx == 1")
                    print("\tcomposite")
                continue
            
            # Prime or even stronger prime
            if x == (n-1):
                if debug:
                    print("\tx == (n-1)")
                    print("\tprime or even stronge prime")
                mr_is_prime = True
                break

    if debug:
        print("done")
        print("is prime = ",mr_is_prime)
        
    return mr_is_prime


def get_prime_pair_candidates(p_list):
    """
    Finds valid prime pairs between first prime and 
    all primes in p_list. 

    A prime pair is determined by taking two primes and concatenating them
    in any order such that the result is always prime. 
    
    i.e. 3 and 7 are prime pairs. 37 and 73 are prime

    Parameters
    ----------
    p_list: list
        list of prime numbers

    Returns
    ----------
    list
        All pair prime 

    Examples
    --------
    >>> # remove 2 as it is never a prime pair 
    >>> get_pair_candidates(list(primes(n_primes=20))[1:])
    [3, 7, 11, 17, 31, 37, 59, 67]

    """

    check_match = lambda x,y: is_prime(int(str(x)+str(y))) and \
                              is_prime(int(str(y)+str(x)))

    prime_start = p_list[0]
    candidates = [prime_start]

    for cp in p_list[1:]:
        if check_match(prime_start,cp):
            candidates.append(cp)
    
    return candidates