import math
from components.robots.interfaces.irobot import Robot
from components.robots.models.differential_drive import DifferentialDrive
from components.robots.models.pose import Pose
# from components.robots.encoder import Encoder


# TODO: Move sign function to an utilities module and import here
def sign(x):
    if x >= 0:
        return 1.0
    else:
        return -1

# TODO: The robot has:
#   1. a state --> Pose
#   2. a interface --> Robot

# TODO: Add default values for the interface part
#   -> Here we do know that the kinematics are in fact for a differential drive
#   -> Geometry and sensor vary, so create defaults from which we can latter derive a configuration files


class DifferentialDriveRobot(Robot):
    def __init__(self, geometry, sensors, x=0.0, y=0.0, theta=0.0):
        super(DifferentialDriveRobot, self).__init__(geometry, DifferentialDrive(), sensors)
        self.pose = Pose(x, y, theta)

# TODO: Implement the unicycle to differential drive transform
    def move(self, v, omega):
        r = self.geometry.wheel_radius
        l = self.geometry.robot_base
        max_speed = self.geometry.max_speed

        # TODO: the total speed can not greater than the maximum possible speed --> limit it

        # TODO: Compute the left/right wheel speeds: (v, omega) --> (wl, wr)
        wl = None
        wr = None

        self.kinematics.set_drive_speeds(wl, wr)

    # TODO: You can compute a pose update in this world loop iteration in two ways:
    #   -> as in the course by using the encoder counts or
    #   -> directly from the angle in this world loop iteration
    #      (prefered -- since latter on we might add noise to motion)
    #
    # TODO:  Alternatively we can burden the user with this, since we already provide encoder ticks.
    #   -> However, this also means that we will have to keep track for each of the
    #      robot poses in the world model, separately. This is required for representing the world state
    #      which gets drawn.

    # TODO: Move the code you write here as the last thing you do in the method below, then delete this method
    def __update_pose(self):
        # TODO: distances done by each wheel

        # TODO: compute the new pose

        # TODO: the angle may require normalization/ do not use the atan2 trick because its very slow
        pass

    # TODO: This should update the differential drive part of the robot: angles, encoders, pose --> in this order
    def update(self, world_unit_time):
        pass



