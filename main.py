#!/usr/bin/env python3

from components import world, gui
from components.robots import robot1, robot2

WORLD_UNIT_TIME = 0.05 # seconds
GUI_PERIOD_TIME = 50 # miliseconds

if __name__ == '__main__':
    world = world.World(WORLD_UNIT_TIME)
    gui = gui.Gui(period = GUI_PERIOD_TIME, background_color = (255, 255, 255), width = 1080, height = 720, grid_color = (211, 211, 211))

    world.add_robot(robot1.Robot1(coordinate_x = 300, coordinate_y = 200), dimensions = {"width" : 20, "height" : 20}, color = (0, 0, 255))
    #world.add_robot(robot2.Robot2(coordinate_x = 300, coordinate_y = 300), dimensions = {"width" : 20, "height" : 20}, color = (0, 255, 0))

    last_time = 0

    while gui.load_frame(world):
        if last_time != int(world.get_time()):
            print("TIME: {} s".format(last_time))
            last_time += 1
        world.step()
