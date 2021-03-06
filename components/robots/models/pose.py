class Pose:

    def __init__(self, x = 0.0, y = 0.0, theta = 0.0):
        self.x = x
        self.y = y
        self.theta = theta

    # separated coordinates
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # 2D position (x, y)
    def get_position(self):
        return self.x, self.y

    def get_heading(self):
        return self.theta

    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y
    
    def set_heading(self, theta):
        self.theta = theta
    
    def set_position(self, x, y):
        self.x = x
        self.y = y

    # Re-using methods is good OOP, but definetly a lot slower since each implies a call further down the stack
    # Hence, we set them directly, no reuse --> sorry :)
    def set_pose(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
