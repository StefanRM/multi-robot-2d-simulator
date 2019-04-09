#!/usr/bin/env python3

from components import world, gui
from components.robots.models.ddrobot import DifferentialDriveRobot
from components.robots.models.khepera3geometry import Khepera3Geometry
from components.robots.models.encoder import Encoder
from components.config import CONFIG


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

        while self.gui.load_frame(self.world):
            if last_time != int(self.world.get_time()):
                print("TIME: {} s".format(last_time))
                last_time += 1
            self.world.step()

def main():

    r_geo = Khepera3Geometry()
    robots = []

    robots.append(DifferentialDriveRobot(x=300,
                                         y=200,
                                         geometry=r_geo,
                                         sensors={"encoders" : [Encoder(r_geo.resolution),
                                                                Encoder(r_geo.resolution)]}))
    robots.append(DifferentialDriveRobot(x=300,
                                         y=300,
                                         geometry=r_geo,
                                         sensors={"encoders" : [Encoder(r_geo.resolution),
                                                                Encoder(r_geo.resolution)]}))
    robots.append(DifferentialDriveRobot(x=100,
                                         y=300,
                                         geometry=r_geo,
                                         sensors={"encoders" : [Encoder(r_geo.resolution),
                                                                Encoder(r_geo.resolution)]}))
    robots.append(DifferentialDriveRobot(x=200,
                                         y=300,
                                         geometry=r_geo,
                                         sensors={"encoders" : [Encoder(r_geo.resolution),
                                                                Encoder(r_geo.resolution)]}))
    robots.append(DifferentialDriveRobot(x=300,
                                         y=100,
                                         geometry=r_geo,
                                         sensors={"encoders" : [Encoder(r_geo.resolution),
                                                                Encoder(r_geo.resolution)]}))
    robots.append(DifferentialDriveRobot(x=200,
                                         y=200,
                                         geometry=r_geo,
                                         sensors={"encoders" : [Encoder(r_geo.resolution),
                                                                Encoder(r_geo.resolution)]}))
    robots.append(DifferentialDriveRobot(x=100,
                                         y=100,
                                         geometry=r_geo,
                                         sensors={"encoders" : [Encoder(r_geo.resolution),
                                                                Encoder(r_geo.resolution)]}))
    robots.append(DifferentialDriveRobot(x=200,
                                         y=100,
                                         geometry=r_geo,
                                         sensors={"encoders" : [Encoder(r_geo.resolution),
                                                                Encoder(r_geo.resolution)]}))

    return robots


if __name__ == '__main__':
    robots = main()
    simulation = Simulation(robots)
    simulation.start()
