from components.config import CONFIG

class World():

    def __init__(self, robots, unit_time=CONFIG['WORLD_UNIT_TIME']):
        self.time = 0.0 # initial world time
        self.unit_time = unit_time

        self.robots = robots

        # obstacles to be added?
        # self.obstacles = []

        self.robots_traces = []
        for robot in robots:
            (x, y) = robot.get_pose().get_position()
            self.robots_traces.append([(x, y), (x, y)])
    
    # obstacles
    # def add_obstacle(self, obstacle):
    #     self.obstacles.append(obstacle)

    def get_robot_trace(self, idx):
        return self.robots_traces[idx]
    
    def get_time(self):
        return self.time
    
    def get_robots(self):
        return self.robots
    
    # obstacles
    # def get_obstacles(self):
    #     return self.obstacles

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
    #  such that a collision event may be signaled to the gui and/or stop the simulation. 5-6 depends on whether
    #  you want sensing / communication or not (for multi-robot systems you usually need both).
    def step(self):
        '''
            Every iteratioon:
             a) update
                -> v, tick, compute pose
                -> compute distance for each robot (for each of its own sensor)
             b) control
                -> each robot move
        '''

        for it, robot in enumerate(self.robots):
            robot.update(self.unit_time)
            (x, y) = robot.get_pose().get_position()
            self.robots_traces[it].append((x, y))

        # sensors update

        for robot in self.robots:
            robot.move(3, 0.1)

        self.control()
        
        self.time += self.unit_time


