from components.robots.models.pose import Pose


# TODO: a robot interface describes four main things:
#   1. Its geometry, i.e. body size, sensor mounting places, axel position, how big are the wheels, max speed and so on
#   2. Its kinematics, i.e. differential-drive/unicycle or car-drive/bicycle or synchro-drive/ominidirectional and so on
#   3. Its sensors, i.e. encoders, IMU, proximity, range, LiDAR, camera and so on.
#   4. A state, i.e. mainly the pose, but can include are status information
# TODO: Aditionally it can also contain other properties mainly for display/logging purposes like trance, color and so.
#       It may be better to maintain something like color in the gui, since in the gui we add features like "color
#       assignment menu". On the other hand, the traces are usually maintained as a log in the world engine.
#       However display properties of each trace (width, color) are part of the qui, since we want to be able to
#       easily introduce or extend display features latter on.
# TODO: Robots may need unique ids
class IRobot:
    def __init__(self, coordinate_x = 0.0, coordinate_y = 0.0, coordinate_theta = 0.0):
        # pose
        self.pose = Pose(x = coordinate_x, y = coordinate_y, theta = coordinate_theta)

        self.sensors = []
        self.controllers = []
        self.trace = [(coordinate_x, coordinate_y), (coordinate_x, coordinate_y)]
        
    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    # TODO: This is part of the user application, i.e. we provide the robots, while the user designs controllers
    def add_controller(self, controller):
        self.controllers.append(controller)
    
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


# TODO: Replace IRobot with robot, a robot is already generic because it can be diff-drive, a car or drone or ...
class Robot:
    def __init__(self, geometry, kinematics, sensors):
        self.geometry = geometry
        self.kinematics = kinematics
        self.sensors = sensors
        self.pose = None

    def get_pose(self):
        return self.pose

    def move(self):
        pass

    def update(self, unit_time):
        pass