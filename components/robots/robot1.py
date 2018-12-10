from interfaces import irobot
import math

class Robot1(irobot.IRobot):

    def __init__(self, coordinate_x = 0.0, coordinate_y = 0.0, coordinate_theta = 0.0, dimensions = {"width" : 40, "height" : 60}, color = (0, 255, 0)):
        super().__init__(coordinate_x, coordinate_y, coordinate_theta, dimensions, color)

    def move(self):
        theta = math.radians(self.coordinate_theta)
        self.coordinate_x = 200 + 100 * math.cos(theta)
        self.coordinate_y = 200 + 100 * math.sin(theta)
        self.coordinate_theta += 1

        self.trace.append((self.coordinate_x, self.coordinate_y))
