from components.robots.pose import Pose

class IRobot:
    def __init__(self, coordinate_x = 0.0, coordinate_y = 0.0, coordinate_theta = 0.0):
        # pose
        self.pose = Pose(x = coordinate_x, y = coordinate_y, theta = coordinate_theta)

        self.encoders = []
        self.sensors = []
        self.model = None
        self.controller = None
        self.trace = [(coordinate_x, coordinate_y), (coordinate_x, coordinate_y)]

        # control inputs
        self.v = 0.0
        self.w = 0.0
        
    def add_sensor(self, sensor):
        self.sensors.append(sensor)
    
    def set_controller(self, sensor):
        self.controller = controller
    
    def add_encoder(self, encoder):
        self.encoders.append(encoder)
    
    def set_model(self, model):
        self.model = model
    
    def get_pose(self):
        return self.pose
    
    def get_trace(self):
        return self.trace
    
    def set_pose(self, x, y, theta):
        self.pose.set_pose(x, y, theta)
    
    def add_current_position_to_trace(self):
        self.trace.append(self.pose.get_position())

    def move(self):
        pass

    def update_pose(self):
        pass
