class Pose:

    def __init__(self, x = 0, y = 0, theta = 0):
        self.x = x
        self.y = y
        self.theta = theta

    # TODO: all separate sets/gets

    def get_position(self):
        return [self.x, self.y]

    def get_heading(self):
        return self.theta
