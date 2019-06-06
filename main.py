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
                            CONFIG['colors']['black'],
                            CONFIG['colors']['purple'],
                            CONFIG['colors']['teal'],
                            CONFIG['colors']['navy']]
        self.gui = gui.Gui(robots_trace_col=robots_trace_col)

    def start(self):
        last_time = 0
        collision = False

        while True:
            (running, pause) = self.gui.load_frame(self.world)

            if last_time != int(self.world.get_time()):
                print("TIME: {} s".format(last_time))
                last_time += 1
            
            if (not collision) and (not pause):
              collision = self.world.step()

            if running is False:
                 break

def init_sensors(r_geo):
       radius = r_geo.radius

       sens_arc_len = CONFIG['sensor_max_range'] * math.pi / 4.0

       CONFIG['sensor_beam_part_points'] = int(sens_arc_len / radius)

       return {"encoders"  : [Encoder(r_geo.resolution),
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
                                   math.pi / 4, 7 * math.pi / 4)]}
                   
def main():

    r_geo = Khepera3Geometry()
    robots = []

    radius = r_geo.radius

    # Atraction (aggegation): distance between robots is greater than dc (= 2.0)
#     robots.append(DifferentialDriveRobot(x=2.5, y=3, geometry=r_geo, sensors=init_sensors(r_geo))) # activ
#     robots.append(DifferentialDriveRobot(x=3, y=7.5, geometry=r_geo, sensors=init_sensors(r_geo)))
#     robots.append(DifferentialDriveRobot(x=4.5, y=11, geometry=r_geo, sensors=init_sensors(r_geo))) # activ
#     robots.append(DifferentialDriveRobot(x=5, y=5, geometry=r_geo, sensors=init_sensors(r_geo)))
#     robots.append(DifferentialDriveRobot(x=7, y=2, geometry=r_geo, sensors=init_sensors(r_geo)))
#     robots.append(DifferentialDriveRobot(x=7.5, y=8, geometry=r_geo, sensors=init_sensors(r_geo)))
#     robots.append(DifferentialDriveRobot(x=8, y=11, geometry=r_geo, sensors=init_sensors(r_geo)))
#     robots.append(DifferentialDriveRobot(x=8.5, y=4.5, geometry=r_geo, sensors=init_sensors(r_geo)))
#     robots.append(DifferentialDriveRobot(x=10.5, y=8.5, geometry=r_geo, sensors=init_sensors(r_geo)))
#     robots.append(DifferentialDriveRobot(x=11.5, y=5, geometry=r_geo, sensors=init_sensors(r_geo))) # activ
#     robots.append(DifferentialDriveRobot(x=12.5, y=2, geometry=r_geo, sensors=init_sensors(r_geo)))

    # Repulsion (dispersion): distance between robots is smaller than dc (= 2.0)
    robots.append(DifferentialDriveRobot(x=4.2, y=4, geometry=r_geo, sensors=init_sensors(r_geo)))
    robots.append(DifferentialDriveRobot(x=5, y=4, geometry=r_geo, sensors=init_sensors(r_geo)))
    robots.append(DifferentialDriveRobot(x=5.8, y=4, geometry=r_geo, sensors=init_sensors(r_geo)))
    robots.append(DifferentialDriveRobot(x=4.2, y=5.2, geometry=r_geo, sensors=init_sensors(r_geo)))
    robots.append(DifferentialDriveRobot(x=5, y=5.2, geometry=r_geo, sensors=init_sensors(r_geo)))
    robots.append(DifferentialDriveRobot(x=5.8, y=5.2, geometry=r_geo, sensors=init_sensors(r_geo)))
    robots.append(DifferentialDriveRobot(x=4.2, y=6.4, geometry=r_geo, sensors=init_sensors(r_geo)))
    robots.append(DifferentialDriveRobot(x=5, y=6.4, geometry=r_geo, sensors=init_sensors(r_geo)))
    robots.append(DifferentialDriveRobot(x=5.8, y=6.3, geometry=r_geo, sensors=init_sensors(r_geo)))
    robots.append(DifferentialDriveRobot(x=3.7, y=2.7, geometry=r_geo, sensors=init_sensors(r_geo)))
    robots.append(DifferentialDriveRobot(x=5.8, y=2.9, geometry=r_geo, sensors=init_sensors(r_geo)))

    return robots


if __name__ == '__main__':
    robots = main()
    simulation = Simulation(robots)
    simulation.start()
