from components.robots.interfaces import irobot
import math

class Robot2(irobot.IRobot):

    def __init__(self, coordinate_x = 0.0, coordinate_y = 0.0, coordinate_theta = 0.0):
        super().__init__(coordinate_x, coordinate_y, coordinate_theta)
        self.my_theta = 0.0

    def move(self):
        (old_x, old_y) = self.pose.get_position()
        theta = self.pose.get_heading()

        my_theta_rad = math.radians(self.my_theta)
        x = 300 - 5 * 16 * (math.sin(my_theta_rad) ** 3)
        y = 300 - 5 * (13 * math.cos(my_theta_rad) - 5 * math.cos(2 * my_theta_rad) - 2 * math.cos(3 * my_theta_rad) - 4 * math.cos(4 * my_theta_rad))
        theta = math.degrees(math.atan2(y - old_y, x - old_x))

        self.my_theta += 1

        self.set_pose(x, y, theta)

        self.add_current_position_to_trace()
