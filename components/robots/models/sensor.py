class Sensor:
    '''
        min - minimal distance at which the sensor can identify an object
        max - maximal distance at which the sensor can identify an object
        pose - relative position (Pose) to the center of the robot where the sensor is situated
        aperture - the aperture of the sensor beam
    '''
    def __init__(self, min, max, pose, aperture, initial_pos):
        self.min = min
        self.max = max
        self.pose = pose
        self.aperture = aperture
        self.initial_pos = initial_pos

    def get_pose(self):
        return self.pose
    
    def get_min(self):
        return self.min
    
    def get_max(self):
        return self.max
    
    def get_aperture(self):
        return self.aperture
