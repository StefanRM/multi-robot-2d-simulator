#!/usr/bin/env python3

from components import world, gui
# TODO: Get rid of robot1, robot2 --> they don't actually simulate anything
from components.robots import robot1, robot2
from components.robots.interfaces.irobot import Robot
from components.robots.models.ddrobot import DifferentialDriveRobot

# TODO: Get rid of these constants
#   --> create constants with in the class and use as default values
#   --> create additional methods for to set these parameters
WORLD_UNIT_TIME = 0.05 # seconds
GUI_PERIOD_TIME = 50 # miliseconds

# TODO: Organize this as simulation.init() / simulation.start()
#   --> The main method should be left for the user
#   --> Something along the lines of:
#       user code (either through import or definition here)
#       def main():
#           user code (initialization for the robots --> either manually or through configuration loading methods)
#       if __name__ == '__main__':
#           main()
#           simulation.init()
#           simulation.start()

if __name__ == '__main__':
    world = world.World(WORLD_UNIT_TIME)
    gui = gui.Gui(period = GUI_PERIOD_TIME, background_color = (255, 255, 255), width = 1080, height = 720, grid_color = (211, 211, 211))

    world.add_robot(robot1.Robot1(coordinate_x = 300, coordinate_y = 200), dimensions = {"width" : 20, "height" : 20}, color = (0, 0, 255))
    world.add_robot(robot2.Robot2(coordinate_x = 300, coordinate_y = 300), dimensions = {"width" : 20, "height" : 20}, color = (0, 255, 0))

    last_time = 0

    while gui.load_frame(world):
        if last_time != int(world.get_time()):
            print("TIME: {} s".format(last_time))
            last_time += 1
        world.step()
