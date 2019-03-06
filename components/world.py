class World():

    def __init__(self, unit_time = 0.1):
        self.time = 0.0 # world time
        self.unit_time = unit_time

        self.robots = []
        self.obstacles = []

        # robots' colors (representation)
        self.robots_colors = []

    def add_robot(self, robot, color = (0, 0, 255)):
        self.robots.append(robot)
        self.robots_colors.append(color)
    
    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)
    
    def get_time(self):
        return self.time
    
    def get_robots(self):
        return self.robots
    
    def get_obstacles(self):
        return self.obstacles

    def get_robots_colors(self):
        return self.robots_colors

    def step(self):
        for robot in self.robots:
            robot.move()
        
        self.time += self.unit_time
