# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# Set data
df = pd.DataFrame({
'group': ['env 0.6344,0.2722 VYYGVPVWK,VYYGVTVWK','env 0.8407 KLTPLCVTL','env 0.5415 MRDNWRSEL','env 0.8083 RVRQGYSPL'],
'Af': [0.50435, 0.4306, 0.5891, 0.6472],
'Af Am': [0.5196, 0.4438, 0.5775, 0.6667],
'Carib Bl': [0.5349, 0.4492, 0.5788, 0.6714],
'Carib His': [0.4433, 0.4835, 0.6103, 0.588],
'Chin': [0.4921, 0.5388, 0.3556, 0.5635],
'Fil': [0.5282, 0.6144, 0.5266, 0.6052],
'His Am': [0.47805, 0.5978, 0.6278, 0.6286],
'Jap': [0.32455, 0.6147, 0.2691, 0.5392],
'Kor': [0.32455, 0.6147, 0.2691, 0.5392],
'Mex': [0.48745, 0.6519, 0.6171, 0.6321],
'E or N Af': [0.4602, 0.5441, 0.6944, 0.6503],
'N Am': [0.48295, 0.6679, 0.6138, 0.6848],
'S As': [0.49245, 0.4093, 0.5802, 0.5334],
'SE As': [0.48875, 0.4405, 0.5283, 0.5473],
'Viet': [0.4077, 0.4255, 0.3072, 0.55],
'Cauc': [0.45285, 0.6261, 0.6941, 0.7673]
})


# number of variable
categories=list(df)[0:16]
N = len(categories)

# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values=df.loc[3].drop('group').values.flatten().tolist()
values += values[:1]
values
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

my_dpi=100
plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)
my_palette = plt.cm.get_cmap("Set2", len(df.index))

# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:16], categories, color='grey', size=12)
 
# Draw ylabels
#ax.set_rlabel_position(0)
ax.set_rgrids([250,250], angle=90)
plt.yticks([0.5,1.0,1.5], ["0.5","1.0","1.5"], color="grey", size=12)
plt.ylim(0,1.5)
 
# Plot data
title=''+df['group'][3]
plt.title(title, color="darkred", size=14, y=1.1)
ax.plot(angles, values, color="darkred", linewidth=1, linestyle='solid')
 
# Fill area
ax.fill(angles, values, color="darkred", alpha=0.1)

#plt.show(block = True)

plt.savefig('env_new_RVRQGYSPL.png')



