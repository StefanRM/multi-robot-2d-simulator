from interfaces import irobot
import math

class Robot1(irobot.IRobot):

    # TODO: use pose
    # TODO: why do you need a color and dimensions here?
    # TODO: what is the model of this robot, is it None (i.e. interface)
    #  or something along the lines of differential, omnidirectional, acherman, etc... ?

    # Note: A generic interface ONLY has a robot model attribute set to None.
    # A implementation of the interface has a model model which contains two parts
    # a navigation part (pose and commands) and a sensor part (e.g. distance, camera, IMU, etc...)
    # In the case of a unicycle the navigation part describes the differential drive, where
    # you can give the robots commands (v, omega) and can request its pose (x, y, theta).

    def __init__(self, coordinate_x = 0.0, coordinate_y = 0.0, coordinate_theta = 0.0, dimensions = {"width" : 40, "height" : 60}, color = (0, 255, 0)):
        super().__init__(coordinate_x, coordinate_y, coordinate_theta, dimensions, color)

    def move(self):
        theta = math.radians(self.coordinate_theta)
        self.coordinate_x = 200 + 100 * math.cos(theta)
        self.coordinate_y = 200 + 100 * math.sin(theta)
        self.coordinate_theta += 1

        self.trace.append((self.coordinate_x, self.coordinate_y))
