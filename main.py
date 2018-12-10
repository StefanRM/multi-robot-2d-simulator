#!/usr/bin/env python3

from components import world, gui
from components.robots import robot1, robot2

if __name__ == '__main__':
    world = world.World(0.05)
    gui = gui.Gui(50)

    world.add_robot(robot1.Robot1(coordinate_x = 300, coordinate_y = 200, dimensions = {"width" : 40, "height" : 60}, color = (0, 0, 255)))
    world.add_robot(robot2.Robot2(coordinate_x = 300, coordinate_y = 300, dimensions = {"width" : 20, "height" : 20}, color = (0, 255, 0)))

    last_time = 0

    while gui.load_frame(world):
        if last_time != int(world.get_time()):
            print("TIME: {} s".format(last_time))
            last_time += 1
        world.step()
