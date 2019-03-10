import math

class DifferentialDrive:

    ''' TODO: The differential drive is composed of two motors which we must simulate.
              To acomplishs this, you must compute the number of revolutions (turns) in this
              world-loop iteration.

    '''

    # TODO: You need to know vl/vr and number of revolutions for each motor
    def __init__(self, wheel_radius, wheel_base):
        # robot physical properties
        self.wheel_radius = wheel_radius # R
        self.wheel_base = wheel_base # L

        # angular speeds (initially zero)
        self.wl = 0.0
        self.wr = 0.0

    # TODO: you must pass the duration of the world-loop iteration here
    def update(self, world_unit_time, pose, encoders):
        # angles done by each wheel
        angle_l = world_unit_time * self.wl
        angle_r = world_unit_time * self.wr

        # distances done by each wheel
        dl = angle_l * self.wheel_radius
        dr = angle_r * self.wheel_radius
        dc = (dl + dr) / 2

        (x, y) = pose.get_position()
        theta = pose.get_heading()

        # compute the new pose
        x_new = x + dc * math.cos(theta)
        y_new = y + dc * math.sin(theta)
        theta_new = theta + (dr - dl) / self.wheel_base

        # compute the revolutions of each wheel
        revolutions_l = angle_l / (2 * math.pi)
        revolutions_r = angle_r / (2 * math.pi)

        # update the pose and the encoder
        pose.set_pose(x_new, y_new, theta_new)
        encoders[0].update(revolutions_l)
        encoders[1].update(revolutions_r)

    # TODO; return a the list [vl, vr] -> instead i use a tuple for ease: (wl, wr) = get_revs()
    def get_revolutions(self):
        return (wl, wr)

    # TODO; Set the drive angular rates
    def set_rates(self, wl, wr):
        self.wl = wl
        self.wr = wr
