import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# set matplotlib figure to be used during FuncAnimation
fig, ax = plt.subplots()
line, = ax.plot([],[])

# Plot 1,000,000 limit 
ax.plot([i for i in range(-10,120)],[1000*1000]*len(range(-10,120)),
         color='Red')

# set plot limits and lables
ax.set_ylabel('Combinations',fontsize=8,fontweight='bold')
ax.set_xlabel('r',fontsize=8,fontweight='bold')
ax.set_xlim(0, 110)

def update(i):

    label = 'N = {0}'.format(i)

    combs = [reverse_factorial(i,i-r)/math.factorial(i-r)
            for r in range(0,i-1)]

    vals = np.greater_equal(combs,1000*1000)
    # combs=np.array(combs)
    r_range=[r for r in range(0,i-1)]

    # Update the line and the axes (with a new xlabel). Return a tuple of
    # "artists" that have to be redrawn for this frame
    line.set_data(r_range,combs)

    ax.set_ylim(0, max(combs)+100000) #added ax attribute here
    ax.set_title(label)

    fig.text(0.70,0.80,'Percentage of Combinations \nExceeding 1E6 = {:2.2f}%'.format((sum(vals)/len(vals))*100),bbox={'facecolor': 'white'},
             fontsize=6)

    return line, ax

def reverse_factorial(n,x):

    f = 1
    for i in range(0,x):
        f = f*(n-i)

    return f

def gen_plot_props(axes,title,ticks_op=True):

    # add title
    axes[0].set_title(title,size=8,fontdict=dict(weight='bold'))

    # add the same gride sytle to each subplot
    for x in range(len(axes)):
        axes[x].grid()
        if ticks_op == True:
            axes[x].minorticks_on()
        axes[x].grid(which='major',linestyle='solid',color='0.01',linewidth=0.20)
        axes[x].grid(which='minor',linestyle='dotted',color='0.01',linewidth=0.10)
        axes[x].tick_params(labelsize=8)

if __name__ == '__main__':
    # add general plot properties
    gen_plot_props(np.array([ax]),'')

    # FuncAnimation will call the 'update' function for each frame; here
    # animating over 45 frames, with an interval of 350ms between frames.
    anim = FuncAnimation(fig, update, frames=range(10,100,3),interval=350)
    anim.save('nCr_animation.gif', writer='imagemagick',fps=5)
    plt.show()
