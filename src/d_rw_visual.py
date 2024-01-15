import matplotlib.pyplot as plt

from c_random_walk import RandomWalk

keep_generating = True

while(keep_generating):
    # plotting the random walk generated in 3_random_walk
    # generate another by inputting 'y'
    # stop generating by inputting 'n'
    rw = RandomWalk()
    # constructor call
    #     rw = RandomWalk(num_points=50000) # can also increase the number of generated points this way; we set this as a constructor parameter in c_random_walk
    
    rw.fill_walk()
    # fills up the points

    plt.style.use('classic')
    # theme
    fig, ax = plt.subplots(figsize=(15, 9))
    # can specify size of the generated figure via figsize
    # 15, 9 are in inches
    
    point_numbers = range(rw.num_points)
    # creates a range of numbers from 0 up to (but not including) the value specified in num_points (0 - 4999 in this case)
    
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)    
    # plots all of the above points
    # c=point_numbers, cmap=plt.cm.Blues sets a gradient color of blue that slowly darkens later points (i.e. point 1000 will be a darker blue than point 500)
    # this helps to visualize the progression of the walk

    ax.set_aspect('equal')
    # makes the x axis and y axis the same scale (distances in the x axis between 2 ticks are the same in the y axis, i.e. from 0 - 100 on the x axis is the same as 0 - 100 on the y axis)
    # so no uneven stretching of the axes

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    # first point is 0, 0 (see c_random_walk)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    s=100)
    # allows easy inspection of the first and last points in the diagram
    # first point is colored green
    # last point is colored red
    # both points are also larger (s=100 vs s=15 for regular points) than regular points
    # we also do this here so that the first and last points are (re)drawn JUST BEFORE the diagram is shown

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    # this is to allow focus on the path rather than the axes
    # probably not a good idea but its an option and this is how you do it

    plt.show()
    
    keep_generating = input("Generate another? y/n --> ") == 'y'