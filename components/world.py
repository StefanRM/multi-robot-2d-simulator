class World():
    # TODO: what are the hardcoded default values? 0.1 means a second, a year or 100ms ?
    #       -->create constant and document it
    def __init__(self, unit_time = 0.1):
        self.time = 0.0 # world time
        self.unit_time = unit_time

        self.robots = []
        self.obstacles = []

        # TODO: This needs to happen transparently and its a hole geometry, not only dimensions
        #       --> a solution would be to add to the constructor of each robot the registration with the world engine
        # robots' dimensions
        self.robots_dimensions = []

        # TODO: These seem more like display properties, not really part of the world engine
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

    # TODO: This needs to contain a hole lot more:
    #   1. In each iteration the robots may move --> hence you must first call the differential-drive update
    #   2. Based on the now updated angle, you can update the encoders
    #   3. Then you can update the pose
    #   4. Check for any collisions among the robots and the obstacles (do this efficiently)
    #   5. Update the other sensors, e.g. proximity, range, LiDAR
    #   6. Pass any messages between the robots if communication is to be simulated
    #  Note: Steps 1-3 are dependent on the model, so this needs to be organized into a single method, 4 is required
    #  such that a collision event may be signaled to the qui and/or stop the simulation. 5-6 depends on whether
    #  you want sensing / communication or not (for multi-robot systems you usually need both).
    def step(self):
        for robot in self.robots:
            robot.move()
        
        self.time += self.unit_time
