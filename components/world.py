class World():

    def __init__(self, unit_time = 0.1):
        self.time = 0.0 # world time
        self.unit_time = unit_time

        self.robots = []
        self.obstacles = []

    def add_robot(self, robot):
        self.robots.append(robot)
    
    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)
    
    def get_time(self):
        return self.time
    
    def get_robots(self):
        return self.robots
    
    def get_obstacles(self):
        return self.obstacles

    def step(self):
        for robot in self.robots:
            robot.move()
        
        self.time += self.unit_time
