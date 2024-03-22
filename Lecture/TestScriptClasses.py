##################################
#     SimTech Python Lesson 1    #
#      SENSEable Design Lab      #
##################################
# v1.0
# 8/30/22
##################################
# EXP: 'python TestScriptClasses.py'
##################################
# Authors: 
# Sermarini
##################################

# Information on Python classes:
# https://www.w3schools.com/python/python_classes.asp

# Import our libraries
import matplotlib.pyplot as plt

##########################
### Create simulation-relevant classes
##########################
class Mine:
	def __init__(self, top_down_coordinates, danger_level):
		self.top_down_coordinates = top_down_coordinates # (x, y)
		self.danger_level = danger_level # 0 = lowest, 4 = highest

class UnderwaterMine(Mine):
	def __init__(self, top_down_coordinates, danger_level, depth):
		super().__init__(top_down_coordinates, danger_level)
		self.depth = depth # meters below surface of the water

	def update_depth(self, depth):
		self.depth = depth

##########################
### Prepare simulation
##########################
mines = [] # Empty mine list
ScarySammy = UnderwaterMine((2, 3), 4, 20)
mines.append(ScarySammy) # Add this mine to the mine master list
GentleGillian = UnderwaterMine((1, 5), 0, 20)
GentleGillian.update_depth(50)
mines.append(GentleGillian) # Add this mine to the mine master list

##########################
### Plot the mine positions
##########################
fig, axs = plt.subplots(1, 2) # Number of rows, number of columns

x = []
y = []
depths = []
for m in mines:
	print(m.depth)
	x.append(m.top_down_coordinates[0])
	y.append(m.top_down_coordinates[1])
	depths.append(-m.depth)

axs[0].scatter(x, x) # top down position
axs[1].scatter(x, depths) # side view

plt.show() # Show the plot
