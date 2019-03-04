# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# Set data
df = pd.DataFrame({
'group': ['env 0.8843 FLGAAGSTM','env 0.4226,0.3339 RAIEAQQHL,RAIEEQQHM','env 0.8247 LQLTVWGIK','env 0.7527 LTVQARQLL'],
'Af': [0.8474, 0.3943, 0.3652, 0.2758],
'Af Am': [0.8468, 0.3791, 0.3703, 0.2613],
'Carib Bl': [0.8334, 0.35855, 0.3938, 0.2467],
'Carib His': [0.8857, 0.4066, 0.3055, 0.2836],
'Chin': [0.7249, 0.2691, 0.36, 0.1946],
'Fil': [0.7394, 0.13685, 0.3684, 0.1093],
'His Am': [0.9849, 0.33225, 0.3149, 0.2226],
'Jap': [0.8003, 0.2947, 0.1387, 0.1752],
'Kor': [0.862, 0.41035, 0.2085, 0.2742],
'Mex': [1.0333, 0.3101, 0.3171, 0.2103],
'E or N Af': [1.0074, 0.4708, 0.3623, 0.3189],
'N Am': [1.0678, 0.3507, 0.2953, 0.2624],
'S As': [0.7705, 0.4597, 0.3569, 0.3678],
'SE As': [0.7557, 0.39835, 0.3569, 0.3099],
'Viet': [0.6732, 0.252, 0.3085, 0.2093],
'Cauc': [1.0775, 0.46265, 0.3197, 0.3504]
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
plt.title(title, color="darkblue", size=14, y=1.1)
ax.plot(angles, values, color="darkblue", linewidth=1, linestyle='solid')
 
# Fill area
ax.fill(angles, values, color="darkblue", alpha=0.1)

#plt.show(block = True)

plt.savefig('env_known_LTVQARQLL.png')



