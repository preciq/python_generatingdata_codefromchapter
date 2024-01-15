from random import choice
# imports choice, which allows us to pick a random value from a list

class RandomWalk:
    """A class to generate random walks."""
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        # number of points to be generated; default set to 5000
        
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]
        # above 2 lists stores all x and y values
        
    def fill_walk(self):
        """This method will generate the random walk"""
        # we run a while loop which generates all of the random points that we can walk
        # this loop will run for the number of points (num_points) we have specified
        
        while len(self.x_values) < self.num_points: 
            x_step = generate_step()
            y_step = generate_step()
            
            if x_step == 0 and y_step == 0:
                continue
            # reject moves that lead nowhere
            
            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)
            # -1 index used to refer to the last value in the list
            # so this takes the last value, adds the newly generated x/y value to it, and then appends the result to the end of x_values/y_values list
            # this appended value now becomes the new last value for the next iteration (the next step)

def generate_step():
    """Refactored to generate steps taken"""
    direction = choice([1, -1])
        # randomly selects either 1 or -1
    distance = choice([0, 1, 2, 3, 4])
        # same thing but between 0 - 4
    return direction * distance

