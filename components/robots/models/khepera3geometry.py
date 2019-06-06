class Khepera3Geometry:

    def __init__(self):
        self.wheel_radius = 0.0885 # meters
        self.robot_base = 0.021 # meters
        # self.max_speed = 0.3148 # meters / seconds
        self.max_speed = 0.8 # meters / seconds
        self.max_ang_speed = 2.2763 # radians / seconds
        self.resolution = 2765 # ticks / 2pi
        self.radius = 0.25 # meters