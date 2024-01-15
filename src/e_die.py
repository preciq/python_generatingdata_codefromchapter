from random import randint

class Die:
    """A class representing a single die (dice)"""
    def __init__(self, num_of_sides=6):
        # number of sides can be changed via num_of_sides parameter
        """6 sided die"""
        self.num_of_sides = num_of_sides
        
    def roll(self):
        """Generate a random value between 1 and however many sides there are"""
        return randint(1, self.num_of_sides)
    
x = Die()
print(x.roll())
# test, will print number between 1 and number of sides, inclusive