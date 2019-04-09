class DifferentialDrive:

    def __init__(self):
        # angular speeds (initially zero)
        self.wl = 0.0
        self.wr = 0.0

        # wheel angles (initially zero)
        self.tl = 0
        self.tr = 0

    # TODO: this will be basically called by the user (a.k.a. called through the robot methods)
    def set_drive_speeds(self, wl, wr):
        self.wl = wl
        self.wr = wr

    # TODO: you must pass the duration of the world-loop iteration here
    #   -> This method updates only the wheel angles, not the pose,
    #      since the pose can be obtained through other sensors.
    #   -> Encoders must contain their own update method
    def update(self, world_unit_time):
        self.tl = self.wl * world_unit_time
        self.tr = self.wr * world_unit_time

    # TODO: return the current wheel angles
    def get_wheel_angles(self):
        return (self.tl, self.tr)
