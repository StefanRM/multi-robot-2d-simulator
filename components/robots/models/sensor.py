from components.robots.models.pose import Pose
import math
from components.config import CONFIG

class Sensor:
    '''
        min - minimal distance at which the sensor can identify an object
        max - maximal distance at which the sensor can identify an object
        pose - relative position (Pose) to the center of the robot where the sensor is situated
        aperture - the aperture of the sensor beam

            / left_points
           /
    sensor ---- max_point
           \
            \ right_points
    '''
    def __init__(self, max, pose, aperture, initial_pos):
        # self.min = min # to be used in the future
        self.max = max
        self.pose = pose
        self.aperture = aperture
        self.initial_pos = initial_pos

        self.id = 0

        # points determined for the sensor proximity beam
        self.beam_left_points = []
        self.beam_right_points = []
        for i in range(CONFIG['sensor_beam_part_points']):
            self.beam_left_points.append(Pose())
            self.beam_right_points.append(Pose())
        self.max_point = Pose()

    def set_id(self, id):
        self.id = id
    
    def get_id(self):
        return self.id

    def get_pose(self):
        return self.pose
    
    def get_min(self):
        return self.min
    
    def get_max(self):
        return self.max
    
    def get_aperture(self):
        return self.aperture

    def compute_sensors_points(self, robot_position, radius):
        (x, y) = robot_position
        (x_sens, y_sens) = self.pose.get_position()

        # should be modified!
        center = (int(x), int(y))
        sensor_center = (int(x + x_sens), int(y + y_sens))

        # sensors beams
        (x_c, y_c) = (center[0], center[1])
        (x_s, y_s) = (sensor_center[0], sensor_center[1])
        d = self.max

        if x_s - x_c == 0:
            x_d = x_s
            if y_c < y_s:
                y_d = y_s + d
            else:
                y_d = y_s - d
        else:
            m = abs((y_s - y_c) / (x_s - x_c))
            if x_c < x_s:
                x_d = x_s + d / math.sqrt(m * m + 1)
            else:
                x_d = x_s - d / math.sqrt(m * m + 1)

            if y_c < y_s:
                y_d = y_s + d * m / math.sqrt(m * m + 1)
            else:
                y_d = y_s - d * m / math.sqrt(m * m + 1)
        
        self.max_point.set_position(x_d, y_d)

        ang = self.aperture / 2.0
        nr_points = CONFIG['sensor_beam_part_points']
        for i in range(nr_points):
            (x_d1, y_d1) = (x_d - x_s, y_d - y_s)
            (x_d1, y_d1) = (x_d1 * math.cos((nr_points - i) * ang / nr_points) - y_d1 * math.sin((nr_points - i) * ang / nr_points), x_d1 * math.sin((nr_points - i) * ang / nr_points) + y_d1 * math.cos((nr_points - i) * ang / nr_points))
            (x_d1, y_d1) = (x_d1 + x_s, y_d1 + y_s)
            self.beam_left_points[i].set_position(x_d1, y_d1)

            (x_d2, y_d2) = (x_d - x_s, y_d - y_s)
            (x_d2, y_d2) = (x_d2 * math.cos(- (i + 1) * ang / nr_points) - y_d2 * math.sin(- (i + 1) * ang / nr_points), x_d2 * math.sin(- (i + 1) * ang / nr_points) + y_d2 * math.cos(- (i + 1) * ang / nr_points))
            (x_d2, y_d2) = (x_d2 + x_s, y_d2 + y_s)
            self.beam_right_points[i].set_position(x_d2, y_d2)