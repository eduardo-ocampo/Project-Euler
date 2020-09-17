""" --------------------------------------------------------------------------
                       PROJECT EULER   -   PROBLEM 317                  
                                                                           
               Copyright (c) Eduardo Ocampo, All Rights Reserved               
               https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """
import numpy as np
import matplotlib.pyplot as plt
import time

def main():

    v, g, yo, = 20, 9.81, 100
    
    theta_res = 200

    
    a = (np.pi*2*v*v)/(g*g)
    b = (v*v)/(2*g)+yo

    tick = time.time()
    # volume = integration_method(v,g,yo,a,b)

    # volume = numerical_solution(v,g,yo)
    tock = time.time()
    print(volume)
    print('Time: ', tock - tick )


    plot_projectivles(v,g,theta_res,yo)

def numerical_solution(v,g,yo):
    """
    Parameters
    ----------

    Returns
    -------

    Notes
    -----
        this takes too long, time elapsed was 320.46612787246704 seconds
        solution was  
                     1856532.834509362

    """

    theta = np.linspace(0,np.pi/2,10000)
    temp = []

    x_range = np.linspace(-10,110,120001)

    for x in x_range:
        y = np.tan(theta)*x+(((-g*0.5)/((v*np.cos(theta))*(v*np.cos(theta))))*x*x+yo)
    
        if max(y) > 0 and x >0:
            temp.append(max(y)*np.pi*2*(x)*0.001)

    return sum(temp)

def integration_method(v,g,yo,a,b):
    v = (g*a*b)*(yo-(b/2)+(v*v)/(2*g))
    return v

def plot_projectivles(v,g,r,yo):

    x_range = np.linspace(0,100,100)    
    theta = np.linspace(0,np.pi,r)

    for i in range(len(theta)):
        y = np.tan(theta[i])*x_range+(((-g*0.5)/((v*np.cos(theta[i]))*(v*np.cos(theta[i]))))*x_range*x_range+yo)

        plt.plot(x_range,y)

    plt.axis([0,100,0,200])
    plt.show()

if __name__ == "__main__":
    
    main()
