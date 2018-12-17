class IRobot:
    def __init__(self, coordinate_x = 0.0, coordinate_y = 0.0, coordinate_theta = 0.0, dimensions = {"width" : 40, "height" : 60}, color = (0, 0, 255)):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.coordinate_theta = coordinate_theta

        self.dimensions = dimensions

        self.sensors = []
        self.controllers = []
        self.trace = [(coordinate_x, coordinate_y), (coordinate_x, coordinate_y)]

        self.color = color
        
    def add_sensor(self, sensor):
        self.sensors.append(sensor)
    
    def add_controller(self, sensor):
        self.controllers.append(controller)
    
    def get_coordinate_x(self):
        return self.coordinate_x
    
    def get_coordinate_y(self):
        return self.coordinate_y
    
    def get_coordinate_theta(self):
        return self.coordinate_theta
    
    def get_trace(self):
        return self.trace
    
    def get_dimensions(self):
        return self.dimensions

    def get_color(self):
        return self.color

    def move(self):
        pass
