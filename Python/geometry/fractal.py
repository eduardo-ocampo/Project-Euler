""" --------------------------------------------------------------------------
               PROJECT EULER   -   Geometry Module:
                                   A Collection of Fractal Geometry

               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo/Project-Euler                            
-------------------------------------------------------------------------- """

import math
import numpy as np 

class blancmange():
    """
    Blancmange Curve as defined by
    https://en.wikipedia.org/wiki/Blancmange_curve
    
    The Blancmange Curve is a self-affine fractal curve constructible by 
    midpoint subdivision.

    The blancmange function is defined by:

    $\sum_{n=0}^{\infty} \frac{s(2^nx)}{2^n}$

    where s(x) is the distance from x to the nearest integer. 
    Here the method self.calc() is the inner most calculation while 
    self.sum_calc() deals with the summation up to n_range not infinity.

    """
    def __init__(self):

        self.calc = lambda x,n: self.triangle_wave((2**n)*x)/(2**n)
        self.sum_calc = lambda x,n_range: sum([self.calc(x,n) for n in n_range])

    def triangle_wave(self,t_num):
        """
        Triangle wave, defined by s(x) = min|x-n| that is, 
        s(x) is the distance from xo the nearest integer
        """

        nearest_int = round(t_num)
        distance = abs(nearest_int-t_num)

        return distance