import matplotlib.pyplot as plt

"""
Refactoring this as a method to easily call on subplots above
"""
def set_x_and_y_labels_fonts(ax):
    # Set chart title and label axes.
    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)
    # Set size of tick labels.
    ax.tick_params(labelsize=14)

plt.style.use('seaborn-v0_8')
# style

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(12, 14)) 
#  figsize=(12, 14) sets the overall picture size to 12 inches wide by 14 inches tall, which could be helpful if image is a bit compact and there is overlap happening

"""SUBPLOT 1"""
ax1.scatter(2, 4, s=200)
# this creates a single point at the coordinates (2, 4)
# s=200 is the size of the point (enlargen the point by increasing)

"""SUBPLOT 2"""
x2_values = [1, 2, 3, 4, 5]
y2_values = [1, 4, 9, 16, 25]

ax2.scatter(x2_values, y2_values, s=100)
# similarly, this plots multiple points. We specify their size with the s parameter
# since we specified scatter, they are unconnected

set_x_and_y_labels_fonts(ax2)

"""SUBPLOT 3"""
x3_values = range(1, 1001)
y3_values = [x**2 for x in x3_values]
# can also mass specify points using loops (list comprehension used here, but we could write this out)
# this first generates a list of numbers for x from 1 - 1000
# it then squares each number and adds that to a list of numbers for y
ax3.scatter(x3_values, y3_values, color='red', s=10)
# even though the points are technically not connected, since there are so many of them in such a small area, they appear so
# can specify color of the points with the 'color' param
    # custom colors also specifiable using RGB: ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)

set_x_and_y_labels_fonts(ax3)

# Set the range for each axis.
ax3.axis([0, 1100, 0, 1_100_000])
ax3.ticklabel_format(style='plain')
# this removes the default scientific notation for large numbers on the x and y axis
# so 1000000 will look like 1e6 by default
# but 'plain' removes that

"""SUBPLOT 4"""
x4_values = range(1, 100)
y4_values = [x**2 for x in x4_values]
ax4.scatter(x4_values, y4_values, c=y4_values, cmap=plt.cm.Blues, s=10)
# we can also use gradients like this, where the color changes if the values change
    # in this example, higher y values will have a darker blue; lower ones will have a lighter blue

set_x_and_y_labels_fonts(ax3)

ax4.axis([0, 110, 0, 11_000])
ax4.ticklabel_format(style='plain')

plt.subplots_adjust(left=0.1,    # 10% padding from the left edge of the figure
                    right=0.9,   # 10% padding from the right edge of the figure
                    bottom=0.1,  # 10% padding from the bottom edge of the figure
                    top=0.9,     # 10% padding from the top edge of the figure
                    wspace=0.4,  # 40% width space between subplots
                    hspace=0.6)  # 60% height space between subplots

plt.savefig('squares_plot.png', dpi=900, bbox_inches='tight')
# saves the plot in squares_plot.png, with a resolution of 900 dots per inch. tight reduces white space

plt.tight_layout()
plt.show()
# displays all plots