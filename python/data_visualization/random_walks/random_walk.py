from random import choice

class RandomWalk:
    """A class for generating random walks"""

    def __init__(self, num_points=5000):
        """Initialize walk attributes"""
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Calulate x,y positions for next step"""
        direction = choice([1, -1])
        distance = choice([0,1,2,3,4])
        return direction * distance

    def fill_walk(self):
        """Calculate all points in a walk"""
        # Keep generating steps until the walk has reached the desired length
        while len(self.x_values) < self.num_points:

            # decide which direction to go and how far
            x_step = self.get_step()
            y_step = self.get_step()

            # reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

