import math 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
""" ---------------------------------------------------------------------- """

def main(progress):
    """
    Parameters
    ----------
    progress: dict
        See notes, for now progress cells are limited to the first 100
        problems

    Notes
    -----
        Update which problems have been solved by adding them to the
        'progress' dictionary. Where the dict key is the problem 
        number as a string and the key values is a list containing 
        both the problem numberand difficulty rating as an int

    Example:
    -------- 
        progress  = {'34': [34,5]}
    """


    # create 2d array containing problem number and difficulty rating
    hm_color = np.zeros((12,10))
    txt_data = np.array(range(1,121)).reshape(12,10)

    for i in progress.keys():
        n_mod = math.modf(int(i)/10)

        if n_mod[0] == 0:
            # Handle mults of 10
            x_cord = int(n_mod[1])
            y_cord = int(n_mod[1])-1
            hm_color[y_cord][9] = progress[i]
        else:
            x_cord = int(round(n_mod[0]*10))
            y_cord = int(n_mod[1])
            hm_color[y_cord][x_cord-1] = progress[i]


    # this block adds a line to include problem 317 which is outside
    # original 100 problems
    # hide row 10 by setting color value equal to nan
    hm_color[10][:] = np.nan 
    txt_data[11][:] = range(311,321)

    hm_color[11][6] = 35

    # Draw heatmap, with numerica values in each cell
    fig, axes = plt.subplots(figsize=(9,11))
    axes.set_axis_off()

    sns.heatmap(hm_color,annot=txt_data,cmap="BuPu",fmt="d",linewidth=0.6,
                ax=axes,cbar_kws={"orientation":"horizontal","shrink":0.80,
                "label":"Difficulty Rating (%)"},annot_kws={"size": 12})

    plt.tight_layout()
    plt.savefig('progress_heatmap.png')

    return None
    
def make_hmap():

    return None

if __name__ == "__main__":

    # Move Soduku scripts to something call game_thoery
    # Setup: {'#Problem',%difficulty}
    progress = {  '1':  5,
                  '3':  5,
                  '7':  5,
                 '10':  5,
                 '13':  5,
                 '15':  5,
                 '18':  5,
                 '52':  5,
                 '53':  5,
                #  '60': 20, # Working
                 '67':  5,
                 '81': 10,
                 '85': 15,
                #  '96': 25 # Finish write up
               }

    main(progress)