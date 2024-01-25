""" --------------------------------------------------------------------------
               PROJECT EULER   -   Geometry Module:
                                   A Collection of Simple Geometric
                                   Shapes

               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo/Project-Euler                            
-------------------------------------------------------------------------- """

import math 
import numpy as np

class circle():
    """
    A simple representation of a geometric circle.

    Defines the points in the cartesian coordinate system
    that make up the circle in the form of range (x coords)
    and domain (y coords).

    Includes functions for calling just the upper and lower
    semi-circle that make up the circle.

    If at least one lower or upper bound is not defined 
    then generates bounds from center point and radius
    padded with 10% more room

    Parameters
    ----------
    radius: int or float
        Circle radius, unitless

    center: List
        List of [x,y] origin coordinates

    x_spacing: int
        Used to space out range, requires int type
        to be used np.linspace()
    
    x_lower_bound: int or float
        Default is None

    x_upper_bound: int or float
        Default is None

    """
    def __init__(self,radius,center,x_spacing=1000,
                 x_lower_bound=None,x_upper_bound=None):

        # Get bounds, to simplify x_range 
        if x_lower_bound == None or x_upper_bound == None:
            x_lower_bound = center[0] - (radius)*1.10
            x_upper_bound = center[0] + (radius)*1.10

        # Cartesian Coordinates
        self.x_range = np.linspace(x_lower_bound,
                                   x_upper_bound,
                                   x_spacing)
        # Polar Coordiantes
        self.theta_range = np.linspace(0, 2*np.pi,
                                       x_spacing)
        
        # Circle Function Definition broken into two semi-circles
        # TODO: Handle case when x < 0
        self.yfunc_upper_semi = lambda x:    math.sqrt(radius**2 - (x-center[0])**2) + center[1]
        self.yfunc_lower_semi = lambda x: -1*math.sqrt(radius**2 - (x-center[0])**2) + center[1]

        # Create Circle from Polar
        self.range  = [radius*np.cos(theta) + center[0] for theta in self.theta_range]
        self.domain = [radius*np.sin(theta) + center[1] for theta in self.theta_range]
