class World():

    def __init__(self, unit_time = 0.1):
        self.time = 0.0 # world time
        self.unit_time = unit_time

        self.robots = []
        self.obstacles = []

        # robots' dimensions
        self.robots_dimensions = []

        # robots' colors (representation)
        self.robots_colors = []

    def add_robot(self, robot, dimensions = {"width" : 40, "height" : 60}, color = (0, 0, 255)):
        self.robots.append(robot)
        self.robots_dimensions.append(dimensions)
        self.robots_colors.append(color)
    
    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)
    
    def get_time(self):
        return self.time
    
    def get_robots(self):
        return self.robots
    
    def get_obstacles(self):
        return self.obstacles

    def get_robots_dimensions(self):
        return self.robots_dimensions

    def get_robots_colors(self):
        return self.robots_colors

    def step(self):
        '''
            Every iteratioon:
             a) update
                -> v, tick, compute pose
                -> compute distance for each robot (for each of its own sensor)
             b) control
                -> each robot move
        '''

        self.update()
        self.control()
        
        self.time += self.unit_time

    def update(self):
        for robot in self.robots:
            robot.update_pose(self.unit_time)

        # sensors update

    def control(self):
        for robot in self.robots:
            robot.move()

