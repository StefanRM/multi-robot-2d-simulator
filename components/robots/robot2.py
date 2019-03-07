from components.robots.interfaces import irobot
import math

class Robot2(irobot.IRobot):

    def __init__(self, coordinate_x = 0.0, coordinate_y = 0.0, coordinate_theta = 0.0):
        super().__init__(coordinate_x, coordinate_y, coordinate_theta)

    def move(self):
        (x, y) = self.pose.get_position()
        theta = self.pose.get_heading()
        theta_rad = math.radians(theta)
 
        x = 300 - 5 * 16 * (math.sin(theta_rad) ** 3)
        y = 300 - 5 * (13 * math.cos(theta_rad) - 5 * math.cos(2 * theta_rad) - 2 * math.cos(3 * theta_rad) - 4 * math.cos(4 * theta_rad))
        theta += 1

        self.set_pose(x, y, theta)

        self.trace.append(self.pose.get_position())
