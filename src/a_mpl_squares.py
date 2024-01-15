import matplotlib.pyplot as plt

"""
Will create a plot of square numbers from 1 - 5
"""
input_values = [1, 2, 3, 4, 5]
# specifying x coordinates
squares = [1, 4, 9, 16, 25]
# specifying y coordinates

plt.style.use('seaborn-v0_8')
"""
can specify a style for the graph as well, like 'seaborn-v0_8'
for a full list of styles, run the following in terminal: 
python3
import matplotlib.pyplot as plt
plt.style.available
"""

fig, ax = plt.subplots()
"""
Standard convention for plotting with matplot
ax represents a single subplot point
fig represents the entire plot or diagram (kind of like the entire pygame window from before)
Here, we are just drawing one subplot (a line graph from 1 - 25, going through the squares)
If we wanted to draw multiple subplots, we could do so like this: 

# Data for the plots
squares = [1, 4, 9, 16, 25]
cubes = [1, 8, 27, 64, 125]

# Create a figure and two subplots (arranged in 2 rows and 1 column)
fig, (ax1, ax2) = plt.subplots(2, 1)

# ax1 and ax2 represent two different subplots in the figure

# Draw a line plot of the square numbers on the first subplot
ax1.plot(squares)
ax1.set_title('Squares')

# Draw a line plot of the cube numbers on the second subplot
ax2.plot(cubes)
ax2.set_title('Cubes')

# Display the figure and its plots
plt.tight_layout()  # This ensures that the plots do not overlap
plt.show()

This draws 2 subplots (2 diagrams) on top of one another (2 rows, 1 column, specified by (2, 1)), within the same window (fig)
Adds titles to them as well
"""

ax.plot(input_values, squares, linewidth=3)
# this then connects the points we specified in the subplot 'ax' above in a meaningful way (by default, looks like a line)
# Set chart title and label axes.
# We also specify the value of the x coordinates and corresponding y coordinates in 2 lists (input_values, squares)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()
# display the created plot