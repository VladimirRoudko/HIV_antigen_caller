# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 
# Set data
df = pd.DataFrame({
'group': ['FSPEVIPMF','IYKRWIILG','VRMYSPVSI,VRMYTPVSI','HQMKDCTER'],
'African': [0.8607, 0.022, 0.40985, 0.0079],
'African American': [0.8636, 0.0245, 0.396, 0.01],
'Caribean Black': [0.8557, 0.0251, 0.3689, 0.0094],
'Caribean Hispanic': [0.8659, 0.0938, 0.4335, 0.0289],
'Chinese': [0.8205, 0.1519, 0.3148, 0.0242],
'Filipino': [0.8792, 0.2399, 0.35035, 0.0059],
'Hispanic American': [0.9401, 0.1316, 0.40275, 0.0439],
'Japanese': [0.9265, 0.353, 0.222, 0.0849],
'Korean': [0.8168, 0.2211, 0.2666, 0.0535],
'Mexican': [0.9516, 0.1304, 0.3936, 0.0531],
'East or North Africa': [0.9678, 0.1174, 0.51185, 0.0186],
'North American': [0.9245, 0.1292, 0.4167, 0.0737],
'South Asian': [0.8464, 0.1362, 0.47315, 0.0331],
'Southeast Asian': [0.8343, 0.138, 0.4334, 0.0259],
'Vietnamese': [0.6921, 0.1109, 0.2689, 0.0137],
'Caucasian': [0.9096, 0.0846, 0.507, 0.027]
})
 
# ------- PART 1: Define a function that do a plot for one line of the dataset!
 
def make_spider( row, title, color):
 
# number of variable
	categories=list(df)[0:16]
	N = len(categories)
	print N
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
	angles = [n / float(N) * 2 * pi for n in range(N)]
	angles += angles[:1]
 
# Initialise the spider plot
	ax = plt.subplot(2,2,row+1, polar=True, )
 
# If you want the first axis to be on top:
	ax.set_theta_offset(pi / 2)
	ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels labels yet
	plt.xticks(angles[:-1], categories, color='grey', size=10)
 
# Draw ylabels
	#ax.set_rlabel_position(0)
	ax.set_rgrids([5,10], angle=22)
	plt.yticks([0.5,1.0,1.5], ["0.5","1.0","1.5"], color="grey", size=7)
	plt.ylim(0,1.5)
 
# Ind1
	values=df.loc[row].drop(['group']).values.flatten().tolist()
	values += values[:1]
	ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
	ax.fill(angles, values, color=color, alpha=0.4)
 
# Add a title
	plt.title(title, size=14, color=color, y=1.1)
 	#plt.show(block = True)
	#plt.savefig('test.png')
	#plt.close()


# ------- PART 2: Apply to all individuals
# initialize the figure
my_dpi=80
plt.figure(figsize=(1500/my_dpi, 1500/my_dpi), dpi=my_dpi)
 
# Create a color palette:
my_palette = plt.cm.get_cmap("Set2", len(df.index))
 
# Loop to plot
for row in range(0, len(df.index)):
	make_spider( row=row, title=''+df['group'][row], color=my_palette(row))
plt.savefig('test.png')

