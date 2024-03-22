##################################
#     SimTech Python Lesson 1    #
#      SENSEable Design Lab      #
##################################
# v1.0
# 8/30/22
##################################
# EXP: 'python TestScript.py'
##################################
# Authors: 
# Sermarini
##################################

# Import our libraries
import matplotlib.pyplot as plt

# Define our line points
x1 = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 2, 3, 4, 5]
y2 = [1, 1, 1, 1, 1, 1]


##########################
### Plot just one plot
##########################
"""
fig, ax = plt.subplots() # Create the empty plot

ax.plot(x1, y1) # Add the first line to the plot
ax.plot(x1, y2) # Add the second line to the plot

plt.show() # Show the plot
"""

##########################
### Plot multiple plots (Vertically)
##########################
"""
fig, axs = plt.subplots(2) # the 2 parameter indicates how many plots you are putting in the column

axs[0].plot(x1, y1) # Set the first plot
axs[1].plot(x1, y2) # Set the second plot

plt.show() # Show the plot
"""

##########################
### Plot multiple plots (Horizontally)
##########################
fig, axs = plt.subplots(1, 2) # the 2 parameter indicates how many plots you are putting in the row

axs[0].plot(x1, y1) # Set the first plot
axs[1].plot(x1, y2) # Set the second plot

plt.show() # Show the plot

##########################
### Plot multiple plots (Both)
##########################
"""
fig, axs = plt.subplots(2, 2) # Number of rows, number of columns

# Take a look at how the numbering of the 1's and 0's is. As you add more plots, these numbers will increase in this same fashion
axs[0, 0].plot(x1, y1) # 1st row, 1st column
axs[0, 1].plot(x1, y2) # 1st row, 2nd column
axs[1, 0].plot(x1, y1) # 2nd row, 1st column
axs[1, 1].plot(x1, y2) # 2nd row, 2nd column

plt.show() # Show the plot
"""
