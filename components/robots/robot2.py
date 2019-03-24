from components.robots.interfaces.irobot import IRobot
import math
from components.robots.models.differential_drive import DifferentialDrive
from components.robots.encoder import Encoder
import random

K3_WHEEL_RADIUS = 0.021         # meters
K3_WHEEL_BASE_LENGTH = 0.0885   # meters
K3_WHEEL_TICKS_PER_REV = 2765
K3_MAX_WHEEL_DRIVE_RATE = 15.0  # rad/s

class Robot2(IRobot):

    def __init__(self, coordinate_x = 0.0, coordinate_y = 0.0, coordinate_theta = 0.0):
        super().__init__(coordinate_x, coordinate_y, coordinate_theta)
        # self.my_theta = 0.0
        self.set_model(DifferentialDrive(K3_WHEEL_RADIUS, K3_WHEEL_BASE_LENGTH))
        self.add_encoder(Encoder(K3_WHEEL_TICKS_PER_REV))
        self.add_encoder(Encoder(K3_WHEEL_TICKS_PER_REV))

    def move(self):
        # (old_x, old_y) = self.pose.get_position()
        # theta = self.pose.get_heading()

        # my_theta_rad = math.radians(self.my_theta)
        # x = 300 - 5 * 16 * (math.sin(my_theta_rad) ** 3)
        # y = 300 - 5 * (13 * math.cos(my_theta_rad) - 5 * math.cos(2 * my_theta_rad) - 2 * math.cos(3 * my_theta_rad) - 4 * math.cos(4 * my_theta_rad))
        # theta = math.atan2(y - old_y, x - old_x)

        # self.my_theta += 1

        # self.set_pose(x, y, theta)

        # self.add_current_position_to_trace()
        self.v = random.randint(1, 5)
        self.w = random.randint(1, 5)
        (wl, wr) = self.model.unicycle_to_differential(self.v, self.w)
        self.model.set_rates(wl, wr)
    
    def update_pose(self, world_unit_time):
        self.model.update(world_unit_time, self.pose, self.encoders)

        self.add_current_position_to_trace()

