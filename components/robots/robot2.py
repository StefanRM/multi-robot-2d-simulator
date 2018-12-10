from interfaces import irobot
import math

class Robot2(irobot.IRobot):

    def __init__(self, coordinate_x = 0.0, coordinate_y = 0.0, coordinate_theta = 0.0, dimensions = {"width" : 40, "height" : 60}, color = (0, 255, 0)):
        super().__init__(coordinate_x, coordinate_y, coordinate_theta, dimensions, color)

    def move(self):
        theta = math.radians(self.coordinate_theta)
        self.coordinate_x = 300 - 5 * 16 * (math.sin(theta) ** 3)
        self.coordinate_y = 300 - 5 * (13 * math.cos(theta) - 5 * math.cos(2 * theta) - 2 * math.cos(3 * theta) - 4 * math.cos(4 * theta))
        self.coordinate_theta += 1

        self.trace.append((self.coordinate_x, self.coordinate_y))
