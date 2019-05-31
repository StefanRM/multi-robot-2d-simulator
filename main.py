#!/usr/bin/env python3

from components import world, gui
from components.robots.models.ddrobot import DifferentialDriveRobot
from components.robots.models.khepera3geometry import Khepera3Geometry
from components.robots.models.encoder import Encoder
from components.config import CONFIG
import math
from components.robots.models.sensor import Sensor
from components.robots.models.pose import Pose


class Simulation:

    def __init__(self, robots):
        self.world = world.World(robots)

        robots_trace_col = [CONFIG['colors']['red'],
                            CONFIG['colors']['lime'],
                            CONFIG['colors']['blue'],
                            CONFIG['colors']['yellow'],
                            CONFIG['colors']['magenta'],
                            CONFIG['colors']['cyan'],
                            CONFIG['colors']['olive'],
                            CONFIG['colors']['black']]
        self.gui = gui.Gui(robots_trace_col=robots_trace_col)

    def start(self):
        last_time = 0
        collision = False

        while self.gui.load_frame(self.world):
            if last_time != int(self.world.get_time()):
                print("TIME: {} s".format(last_time))
                last_time += 1
            
            if not collision:
              collision = self.world.step()
                   
def main():

    r_geo = Khepera3Geometry()
    robots = []

    # should be modified!
    dimension = CONFIG['robots_dim']
    width = dimension["width"]
    height = dimension["height"]
    radius = int(math.sqrt(width * width + height * height) / 2.0)

    robots.append(DifferentialDriveRobot(x=500,
                                         y=300,
                                         geometry=r_geo,
                                         sensors={"encoders"  : [Encoder(r_geo.resolution),
                                                                 Encoder(r_geo.resolution)],
                                                  "proximity" : [Sensor(CONFIG['sensor_max_range'],
                                                                        Pose(radius * math.cos(0), radius * math.sin(0), 0),
                                                                        math.pi / 4, 0),
                                                                 Sensor(CONFIG['sensor_max_range'],
                                                                        Pose(radius * math.cos(math.pi / 4), radius * math.sin(math.pi / 4), math.pi / 4),
                                                                        math.pi / 4, math.pi / 4),
                                                                 Sensor(CONFIG['sensor_max_range'],
                                                                        Pose(radius * math.cos(math.pi / 2), radius * math.sin(math.pi / 2), math.pi / 2),
                                                                        math.pi / 4,  math.pi / 2),
                                                                 Sensor(CONFIG['sensor_max_range'],
                                                                        Pose(radius * math.cos(3 * math.pi / 4), radius * math.sin(3 * math.pi / 4), 3 * math.pi / 4),
                                                                        math.pi / 4, 3 * math.pi / 4),
                                                                 Sensor(CONFIG['sensor_max_range'],
                                                                        Pose(radius * math.cos(math.pi), radius * math.sin(math.pi), math.pi),
                                                                        math.pi / 4, math.pi),
                                                                 Sensor(CONFIG['sensor_max_range'],
                                                                        Pose(radius * math.cos(5 * math.pi / 4), radius * math.sin(5 * math.pi / 4), 5 * math.pi / 4),
                                                                        math.pi / 4, 5 * math.pi / 4),
                                                                 Sensor(CONFIG['sensor_max_range'],
                                                                        Pose(radius * math.cos(3 * math.pi / 2), radius * math.sin(3 * math.pi / 2), 3 * math.pi / 2),
                                                                        math.pi / 4, 3 * math.pi / 2),
                                                                 Sensor(CONFIG['sensor_max_range'],
                                                                        Pose(radius * math.cos(7 * math.pi / 4), radius * math.sin(7 * math.pi / 4), 7 * math.pi / 4),
                                                                        math.pi / 4, 7 * math.pi / 4)]}))
    robots.append(DifferentialDriveRobot(x=500,
                                         y=200,
                                         geometry=r_geo,
                                         sensors={"encoders" : [Encoder(r_geo.resolution),
                                                                Encoder(r_geo.resolution)],
                                                  "proximity" : [Sensor(CONFIG['sensor_max_range'],
                                                                        Pose(radius * math.cos(0), radius * math.sin(0), 0),
                                                                        math.pi / 4, 0),
                                                                 Sensor(CONFIG['sensor_max_range'],
                                                                        Pose(radius * math.cos(math.pi / 4), radius * math.sin(math.pi / 4), math.pi / 4),
                                                                        math.pi / 4, math.pi / 4),
                                                                 Sensor(CONFIG['sensor_max_range'],
                                                                        Pose(radius * math.cos(math.pi / 2), radius * math.sin(math.pi / 2), math.pi / 2),
                                                                        math.pi / 4,  math.pi / 2),
                                                                 Sensor(CONFIG['sensor_max_range'],
                                                                        Pose(radius * math.cos(3 * math.pi / 4), radius * math.sin(3 * math.pi / 4), 3 * math.pi / 4),
                                                                        math.pi / 4, 3 * math.pi / 4),
                                                                 Sensor(CONFIG['sensor_max_range'],
                                                                        Pose(radius * math.cos(math.pi), radius * math.sin(math.pi), math.pi),
                                                                        math.pi / 4, math.pi),
                                                                 Sensor(CONFIG['sensor_max_range'],
                                                                        Pose(radius * math.cos(5 * math.pi / 4), radius * math.sin(5 * math.pi / 4), 5 * math.pi / 4),
                                                                        math.pi / 4, 5 * math.pi / 4),
                                                                 Sensor(CONFIG['sensor_max_range'],
                                                                        Pose(radius * math.cos(3 * math.pi / 2), radius * math.sin(3 * math.pi / 2), 3 * math.pi / 2),
                                                                        math.pi / 4, 3 * math.pi / 2),
                                                                 Sensor(CONFIG['sensor_max_range'],
                                                                        Pose(radius * math.cos(7 * math.pi / 4), radius * math.sin(7 * math.pi / 4), 7 * math.pi / 4),
                                                                        math.pi / 4, 7 * math.pi / 4)]}))
#     robots.append(DifferentialDriveRobot(x=100,
#                                          y=300,
#                                          geometry=r_geo,
#                                          sensors={"encoders" : [Encoder(r_geo.resolution),
#                                                                 Encoder(r_geo.resolution)],
#                                                   "proximity" : [Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(0), radius * math.sin(0), 0),
#                                                                         math.pi / 4, 0),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi / 4), radius * math.sin(math.pi / 4), math.pi / 4),
#                                                                         math.pi / 4, math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi / 2), radius * math.sin(math.pi / 2), math.pi / 2),
#                                                                         math.pi / 4,  math.pi / 2),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(3 * math.pi / 4), radius * math.sin(3 * math.pi / 4), 3 * math.pi / 4),
#                                                                         math.pi / 4, 3 * math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi), radius * math.sin(math.pi), math.pi),
#                                                                         math.pi / 4, math.pi),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(5 * math.pi / 4), radius * math.sin(5 * math.pi / 4), 5 * math.pi / 4),
#                                                                         math.pi / 4, 5 * math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(3 * math.pi / 2), radius * math.sin(3 * math.pi / 2), 3 * math.pi / 2),
#                                                                         math.pi / 4, 3 * math.pi / 2),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(7 * math.pi / 4), radius * math.sin(7 * math.pi / 4), 7 * math.pi / 4),
#                                                                         math.pi / 4, 7 * math.pi / 4)]}))
#     robots.append(DifferentialDriveRobot(x=200,
#                                          y=300,
#                                          geometry=r_geo,
#                                          sensors={"encoders" : [Encoder(r_geo.resolution),
#                                                                 Encoder(r_geo.resolution)],
#                                                   "proximity" : [Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(0), radius * math.sin(0), 0),
#                                                                         math.pi / 4, 0),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi / 4), radius * math.sin(math.pi / 4), math.pi / 4),
#                                                                         math.pi / 4, math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi / 2), radius * math.sin(math.pi / 2), math.pi / 2),
#                                                                         math.pi / 4,  math.pi / 2),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(3 * math.pi / 4), radius * math.sin(3 * math.pi / 4), 3 * math.pi / 4),
#                                                                         math.pi / 4, 3 * math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi), radius * math.sin(math.pi), math.pi),
#                                                                         math.pi / 4, math.pi),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(5 * math.pi / 4), radius * math.sin(5 * math.pi / 4), 5 * math.pi / 4),
#                                                                         math.pi / 4, 5 * math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(3 * math.pi / 2), radius * math.sin(3 * math.pi / 2), 3 * math.pi / 2),
#                                                                         math.pi / 4, 3 * math.pi / 2),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(7 * math.pi / 4), radius * math.sin(7 * math.pi / 4), 7 * math.pi / 4),
#                                                                         math.pi / 4, 7 * math.pi / 4)]}))
#     robots.append(DifferentialDriveRobot(x=300,
#                                          y=100,
#                                          geometry=r_geo,
#                                          sensors={"encoders" : [Encoder(r_geo.resolution),
#                                                                 Encoder(r_geo.resolution)],
#                                                   "proximity" : [Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(0), radius * math.sin(0), 0),
#                                                                         math.pi / 4, 0),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi / 4), radius * math.sin(math.pi / 4), math.pi / 4),
#                                                                         math.pi / 4, math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi / 2), radius * math.sin(math.pi / 2), math.pi / 2),
#                                                                         math.pi / 4,  math.pi / 2),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(3 * math.pi / 4), radius * math.sin(3 * math.pi / 4), 3 * math.pi / 4),
#                                                                         math.pi / 4, 3 * math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi), radius * math.sin(math.pi), math.pi),
#                                                                         math.pi / 4, math.pi),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(5 * math.pi / 4), radius * math.sin(5 * math.pi / 4), 5 * math.pi / 4),
#                                                                         math.pi / 4, 5 * math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(3 * math.pi / 2), radius * math.sin(3 * math.pi / 2), 3 * math.pi / 2),
#                                                                         math.pi / 4, 3 * math.pi / 2),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(7 * math.pi / 4), radius * math.sin(7 * math.pi / 4), 7 * math.pi / 4),
#                                                                         math.pi / 4, 7 * math.pi / 4)]}))
#     robots.append(DifferentialDriveRobot(x=200,
#                                          y=200,
#                                          geometry=r_geo,
#                                          sensors={"encoders" : [Encoder(r_geo.resolution),
#                                                                 Encoder(r_geo.resolution)],
#                                                   "proximity" : [Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(0), radius * math.sin(0), 0),
#                                                                         math.pi / 4, 0),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi / 4), radius * math.sin(math.pi / 4), math.pi / 4),
#                                                                         math.pi / 4, math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi / 2), radius * math.sin(math.pi / 2), math.pi / 2),
#                                                                         math.pi / 4,  math.pi / 2),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(3 * math.pi / 4), radius * math.sin(3 * math.pi / 4), 3 * math.pi / 4),
#                                                                         math.pi / 4, 3 * math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi), radius * math.sin(math.pi), math.pi),
#                                                                         math.pi / 4, math.pi),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(5 * math.pi / 4), radius * math.sin(5 * math.pi / 4), 5 * math.pi / 4),
#                                                                         math.pi / 4, 5 * math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(3 * math.pi / 2), radius * math.sin(3 * math.pi / 2), 3 * math.pi / 2),
#                                                                         math.pi / 4, 3 * math.pi / 2),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(7 * math.pi / 4), radius * math.sin(7 * math.pi / 4), 7 * math.pi / 4),
#                                                                         math.pi / 4, 7 * math.pi / 4)]}))
#     robots.append(DifferentialDriveRobot(x=100,
#                                          y=100,
#                                          geometry=r_geo,
#                                          sensors={"encoders" : [Encoder(r_geo.resolution),
#                                                                 Encoder(r_geo.resolution)],
#                                                   "proximity" : [Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(0), radius * math.sin(0), 0),
#                                                                         math.pi / 4, 0),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi / 4), radius * math.sin(math.pi / 4), math.pi / 4),
#                                                                         math.pi / 4, math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi / 2), radius * math.sin(math.pi / 2), math.pi / 2),
#                                                                         math.pi / 4,  math.pi / 2),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(3 * math.pi / 4), radius * math.sin(3 * math.pi / 4), 3 * math.pi / 4),
#                                                                         math.pi / 4, 3 * math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi), radius * math.sin(math.pi), math.pi),
#                                                                         math.pi / 4, math.pi),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(5 * math.pi / 4), radius * math.sin(5 * math.pi / 4), 5 * math.pi / 4),
#                                                                         math.pi / 4, 5 * math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(3 * math.pi / 2), radius * math.sin(3 * math.pi / 2), 3 * math.pi / 2),
#                                                                         math.pi / 4, 3 * math.pi / 2),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(7 * math.pi / 4), radius * math.sin(7 * math.pi / 4), 7 * math.pi / 4),
#                                                                         math.pi / 4, 7 * math.pi / 4)]}))
#     robots.append(DifferentialDriveRobot(x=200,
#                                          y=100,
#                                          geometry=r_geo,
#                                          sensors={"encoders" : [Encoder(r_geo.resolution),
#                                                                 Encoder(r_geo.resolution)],
#                                                   "proximity" : [Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(0), radius * math.sin(0), 0),
#                                                                         math.pi / 4, 0),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi / 4), radius * math.sin(math.pi / 4), math.pi / 4),
#                                                                         math.pi / 4, math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi / 2), radius * math.sin(math.pi / 2), math.pi / 2),
#                                                                         math.pi / 4,  math.pi / 2),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(3 * math.pi / 4), radius * math.sin(3 * math.pi / 4), 3 * math.pi / 4),
#                                                                         math.pi / 4, 3 * math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(math.pi), radius * math.sin(math.pi), math.pi),
#                                                                         math.pi / 4, math.pi),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(5 * math.pi / 4), radius * math.sin(5 * math.pi / 4), 5 * math.pi / 4),
#                                                                         math.pi / 4, 5 * math.pi / 4),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(3 * math.pi / 2), radius * math.sin(3 * math.pi / 2), 3 * math.pi / 2),
#                                                                         math.pi / 4, 3 * math.pi / 2),
#                                                                  Sensor(CONFIG['sensor_max_range'],
#                                                                         Pose(radius * math.cos(7 * math.pi / 4), radius * math.sin(7 * math.pi / 4), 7 * math.pi / 4),
#                                                                         math.pi / 4, 7 * math.pi / 4)]}))

    return robots


if __name__ == '__main__':
    robots = main()
    simulation = Simulation(robots)
    simulation.start()
