# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# Set data
df = pd.DataFrame({
'group': ['gag 0.5547,0.4278 FRDYVDRFY,FRDYVYRFY','gag 0.5053 YVDRFYKTL','gag 0.6341 NWMTETLLV','gag 0.9173 KARVLAEAM'],
'Af': [0.521, 0.5323, 0.3494, 0.2933],
'Af Am': [0.50615, 0.5255, 0.3546, 0.3038],
'Carib Bl': [0.49215, 0.5403, 0.3783, 0.3008],
'Carib His': [0.5782, 0.6045, 0.321, 0.1997],
'Chin': [0.3725, 0.45, 0.238, 0.2171],
'Fil': [0.4819, 0.5605, 0.4281, 0.0604],
'His Am': [0.5975, 0.6404, 0.3594, 0.1729],
'Jap': [0.1814, 0.4283, 0.4726, 0.1825],
'Kor': [0.2586, 0.4373, 0.3593, 0.2036],
'Mex': [0.5959, 0.6362, 0.3373, 0.1523],
'E or N Af': [0.72175, 0.6563, 0.3396, 0.1732],
'N Am': [0.6551, 0.6062, 0.292, 0.1771],
'S As': [0.6585, 0.4586, 0.3128, 0.1655],
'SE As': [0.5886, 0.4659, 0.2962, 0.1727],
'Viet': [0.43705, 0.3847, 0.1724, 0.1992],
'Cauc': [0.79305, 0.6829, 0.2229, 0.2232]
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

plt.savefig('gag_new_KARVLAEAM.png')



