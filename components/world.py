from components.config import CONFIG
import math
import sys
from components import utilities

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

        if self.update():
            print("Collision occured!")
            return True

        self.control()
        
        self.time += self.unit_time

        return False

    def update(self):
        for it, robot in enumerate(self.robots):
            robot.update(self.unit_time)
            (x, y) = robot.get_pose().get_position()
            self.robots_traces[it].append((x, y))

        # sensors update
        dimension = CONFIG['robots_dim']
        width = dimension["width"]
        height = dimension["height"]

        radius = int(math.sqrt(width * width + height * height) / 2.0)

        for robot in self.robots:
            (x, y) = robot.get_pose().get_position()
            sensors = robot.get_sensors()
            neigh_detected = []

            for other_robot in self.robots:

                min_d = sensors[0].get_max()
                found = False
                sens_id = -1
                
                if robot != other_robot:
                    if utilities.check_robot_collision((x, y), other_robot.get_pose().get_position(), radius):
                        return True
                        # pass
                    for sens in sensors:
                        (x_sens, y_sens) = sens.pose.get_position()
                        (x_sc, y_sc) = ((x + x_sens), (y + y_sens))
                        
                        points_to_check = []
                        for point in sens.beam_left_points:
                            points_to_check.append(point.get_position())
                        points_to_check.append(sens.max_point.get_position())
                        for point in sens.beam_right_points:
                            points_to_check.append(point.get_position())

                        for point in points_to_check:
                            res = utilities.find_intersection((x_sc, y_sc), point, other_robot.get_pose().get_position(), radius)
                            for sol in res:
                                (x_sol, y_sol) = sol

                                if (utilities.check_point_inside((x_sc, y_sc), point, sol)):
                                    d = math.sqrt((x_sc - x_sol) * (x_sc - x_sol) + (y_sc - y_sol) * (y_sc - y_sol))
                                    # print(d)

                                    blocked = False
                                    new_neigh_detected = []

                                    for neigh in neigh_detected:
                                        (ot_rid, s_id, m_d) = neigh
                                        if (s_id == sens.get_id()) and utilities.check_collinearity(robot.get_pose().get_position(),
                                                                                                    self.robots[ot_rid].get_pose().get_position(),
                                                                                                    other_robot.get_pose().get_position()):
                                            if m_d < d:
                                                blocked = True
                                            else:
                                                continue
                                        new_neigh_detected.append(neigh)

                                    neigh_detected = new_neigh_detected

                                    if (not blocked) and (d <= min_d):
                                        min_d = d
                                        found = True
                                        sens_id = sens.get_id()
                        
                if found:
                    # print("r_id({})-other_r_id({})-sens_id({}): {}".format(robot.id, other_robot.id, sens_id, min_d))
                    neigh_detected.append((other_robot.id, sens_id, min_d))
                    # t=sys.stdin.readline()
            # print("{}: {}".format(robot.id, neigh_detected))
            robot.neigh_list = neigh_detected
        
        return False

    def control(self):
        # i = 0
        # for robot in self.robots:
        #     if i == 3:
        #         robot.move(40, 0.75)
        #     else:
        #         robot.move(40, 1)
            
        #     i += 1
        dc = 20
        for robot in self.robots:
            ui = 0
            wi = 0
            for neigh in robot.neigh_list:
                (ot_rid, sens_id, d) = neigh
                (xi, yi) = robot.get_pose().get_position()
                thetai = robot.get_pose().get_heading()
                (xj, yj) = self.robots[ot_rid].get_pose().get_position()

                kd = 1 - math.exp(dc - d * d)
                gy = ((xi - xj) * math.cos(thetai) + (yi - yj) * math.sin(thetai)) * kd

                ui -= gy

                phiij = robot.get_sensors()[sens_id].get_pose().get_heading()
                # phiij = math.atan2(yj - yi, xj - xi)
                wi += thetai - kd * phiij + (kd - 1) * math.pi / 4

            robot.move(ui + 30, wi)
