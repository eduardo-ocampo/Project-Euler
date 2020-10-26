from Counting_Rectangles import calc_area
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
v,h = 1,1
h_array = np.arange(v,100)
w_array = np.arange(h,100).reshape(-1,1)

rects = (w_array*w_array+w_array)*(h_array*h_array+h_array)/4

fig, axes = plt.subplots(figsize=(9,11))

sns.heatmap(rects, vmin=0, vmax=2e6,ax=axes, xticklabels = 10, yticklabels = 10,
            cbar_kws={"orientation":"horizontal","shrink":0.90,
            "label":"Rectangles Formed"},
            annot_kws={"size": 14})
            
axes.set_title("Number of Rectangles Formed\nHeatmap solutions limited to 2e6\n",
               fontweight="bold")

axes.set_ylabel("m (Grid Height)")
axes.set_xlabel("n (Grid Width)")

axes.xaxis.tick_top() # x axis on top
axes.xaxis.set_label_position('top')

plt.savefig('rectangles_formed.png')