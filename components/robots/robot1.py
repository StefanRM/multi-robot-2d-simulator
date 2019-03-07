from components.robots.interfaces import irobot
import math

class Robot1(irobot.IRobot):

    # TODO: use pose -> checked
    # TODO: why do you need a color and dimensions here? -> checked
    # TODO: what is the model of this robot, is it None (i.e. interface)
    #  or something along the lines of differential, omnidirectional, acherman, etc... ?

    # Note: A generic interface ONLY has a robot model attribute set to None.
    # A implementation of the interface has a model model which contains two parts
    # a navigation part (pose and commands) and a sensor part (e.g. distance, camera, IMU, etc...)
    # In the case of a unicycle the navigation part describes the differential drive, where
    # you can give the robots commands (v, omega) and can request its pose (x, y, theta).

    def __init__(self, coordinate_x = 0.0, coordinate_y = 0.0, coordinate_theta = 0.0):
        super().__init__(coordinate_x, coordinate_y, coordinate_theta)
        self.my_theta = 0.0

    def move(self):
        (old_x, old_y) = self.pose.get_position()
        theta = self.pose.get_heading()

        my_theta_rad = math.radians(self.my_theta)
        x = 200 + 100 * math.cos(my_theta_rad)
        y = 200 + 100 * math.sin(my_theta_rad)
        theta = math.degrees(math.atan2(y - old_y, x - old_x))

        self.my_theta += 1

        self.set_pose(x, y, theta)

        self.trace.append(self.pose.get_position())
