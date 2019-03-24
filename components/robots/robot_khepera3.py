from components.robots.interfaces.irobot import IRobot
import math
from components.robots.models.differential_drive import DifferentialDrive
from components.robots.encoder import Encoder
import random

# KEPHERA 3

K3_WHEEL_RADIUS = 0.021         # meters
K3_WHEEL_BASE_LENGTH = 0.0885   # meters
K3_WHEEL_TICKS_PER_REV = 2765
K3_MAX_WHEEL_DRIVE_RATE = 15.0  # rad/s

class RobotKhepera3(IRobot):

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

        self.set_model(DifferentialDrive(K3_WHEEL_RADIUS, K3_WHEEL_BASE_LENGTH))
        self.add_encoder(Encoder(K3_WHEEL_TICKS_PER_REV))
        self.add_encoder(Encoder(K3_WHEEL_TICKS_PER_REV))
        self.sgn = 1

    def move(self):
        # testing
        if (self.v >= 5):
            self.v = 0

        self.sgn = random.randint(-1, 1)

        self.v += self.sgn * 0.5
        self.w += self.sgn * 0.01
        # !testing

        (wl, wr) = self.model.unicycle_to_differential(self.v, self.w)
        self.model.set_rates(wl, wr)
    
    def update_pose(self, world_unit_time):
        self.model.update(world_unit_time, self.pose, self.encoders)

        self.add_current_position_to_trace()

