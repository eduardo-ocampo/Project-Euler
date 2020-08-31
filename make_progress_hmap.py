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
        n_mod = math.modf(progress[i][0]/10)

        x_cord = int(round(n_mod[0]*10))
        y_cord = int(n_mod[1])

        hm_color[y_cord][x_cord-1] = progress[i][1]

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
                ax=axes,cbar_kws={"orientation":"horizontal","shrink":0.70,
                "label":"Difficulty Rating (%)"}   
                             )
    plt.tight_layout()
    plt.savefig('progress_heatmap.png')

    return None
def make_hmap():

    return None

if __name__ == "__main__":

    progress = {  '1': [  1, 5],
                 '18': [ 18, 5],
                 '52': [ 52, 5],
                 '53': [ 53, 5]}

    main(progress)