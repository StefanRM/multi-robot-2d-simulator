from components.robots.pose import Pose

class IRobot:
    def __init__(self, coordinate_x = 0.0, coordinate_y = 0.0, coordinate_theta = 0.0):
        # pose
        self.pose = Pose(x = coordinate_x, y = coordinate_y, theta = coordinate_theta)

        self.sensors = []
        self.controllers = []
        self.trace = [(coordinate_x, coordinate_y), (coordinate_x, coordinate_y)]
        
    def add_sensor(self, sensor):
        self.sensors.append(sensor)
    
    def add_controller(self, sensor):
        self.controllers.append(controller)
    
    def get_pose(self):
        return self.pose

    def get_position(self):
        return (self.coordinate_x, self.coordinate_y)

    def get_heading(self):
        return self.coordinate_theta
    
    def get_trace(self):
        return self.trace
    
    def set_pose(self, x, y, theta):
        self.pose.set_pose(x, y, theta)

    def move(self):
        pass
