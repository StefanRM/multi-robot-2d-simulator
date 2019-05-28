import pygame
import math
from components.config import CONFIG


class Gui:

    def __init__(self,
                 robots_trace_col,
                 robots_dim=CONFIG['robots_dim'],
                 period=CONFIG['GUI_PERIOD_TIME'],
                 width=CONFIG['win_width'],
                 height=CONFIG['win_height'],
                 caption=CONFIG['win_caption'],
                 background_color=CONFIG['colors']['white'],
                 grid_color=CONFIG['colors']['light-gray']):
        self.period = period # miliseconds
        self.width = width
        self.height = height
        self.caption = caption
        self.background_color = background_color
        
        self.grid_color = grid_color
        
        self.robots_dim = robots_dim
        self.robots_trace_col = robots_trace_col

        self.display_traces = False
        self.display_grid = False
        self.display_sensors = False
        self.press_limiter_toggle_display_traces = False
        self.press_limiter_toggle_display_grid = False
        self.press_limiter_toggle_display_sensors = False

        pygame.init()
        self.window = pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        pygame.display.set_caption(caption)

        # origin of the axis for a 4 quadrant map
        self.origin_x = 0
        self.origin_y = height

        # robot symbol
        self.robot_img = pygame.image.load(CONFIG['path_to_robot_image'])
    
    # convert coordinates the window system of coordinates
    def convert_coordinates(self, position):
        (x, y) = position
        return (self.origin_x + x, self.origin_y - y)

    def toggle_display_traces(self):
        self.display_traces = not self.display_traces
    
    def toggle_display_grid(self):
        self.display_grid = not self.display_grid

    def toggle_display_sensors(self):
        self.display_sensors = not self.display_sensors

    def load_frame(self, world):
        pygame.time.delay(self.period)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.VIDEORESIZE:
                self.window=pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)


        keys = pygame.key.get_pressed()

        if keys[CONFIG['DISP_TRACES_KEY']]:
            if not self.press_limiter_toggle_display_traces:
                self.toggle_display_traces()
                self.press_limiter_toggle_display_traces = True
        else:
            self.press_limiter_toggle_display_traces = False
        
        if keys[CONFIG['DISP_GRID_KEY']]:
            if not self.press_limiter_toggle_display_grid:
                self.toggle_display_grid()
                self.press_limiter_toggle_display_grid = True
        else:
            self.press_limiter_toggle_display_grid = False

        if keys[CONFIG['DISP_SENSORS_KEY']]:
            if not self.press_limiter_toggle_display_sensors:
                self.toggle_display_sensors()
                self.press_limiter_toggle_display_sensors = True
        else:
            self.press_limiter_toggle_display_sensors = False
            

        # drawing the grid
        if self.display_grid:
            self.window.fill(self.grid_color)
            for i in range(0, self.width, CONFIG['DIST_BETWEEN_GRIDS'] + CONFIG['GRID_CELL_DIM']):
                for j in range(0, self.width, CONFIG['DIST_BETWEEN_GRIDS'] + CONFIG['GRID_CELL_DIM']):
                    pygame.draw.rect(self.window, self.background_color, (i, j, CONFIG['GRID_CELL_DIM'], CONFIG['GRID_CELL_DIM']))
        else:
            self.window.fill(self.background_color)

        robots = world.get_robots()


        for it, robot in enumerate(robots):
            trace = world.get_robot_trace(it)
            (x, y) = robot.get_pose().get_position()
            dimension = self.robots_dim
            width = dimension["width"]
            height = dimension["height"]

            # drawing the traces
            if self.display_traces:
                for i in range(len(trace) - 1):
                    (a, b) = trace[i]
                    (c, d) = trace[i + 1]
                    start = self.convert_coordinates((a, b))
                    stop = self.convert_coordinates((c, d))
                    pygame.draw.line(self.window, self.robots_trace_col[it], start, stop, CONFIG['TRACE_LINE_WIDTH'])
            
        for it, robot in enumerate(robots):
            (x, y) = robot.get_pose().get_position()
            theta = robot.get_pose().get_heading()
            dimension = self.robots_dim
            width = dimension["width"]
            height = dimension["height"]

            if self.display_sensors:
                sensors = robot.get_sensors()
                for sens in sensors:
                    (x_sens, y_sens) = sens.pose.get_position()

                    sensor_center = (int(x + x_sens), int(y + y_sens))

                    pygame.draw.circle(self.window, CONFIG['colors']['red'], self.convert_coordinates(sensor_center), 3, 3)
                    pygame.draw.polygon(self.window, CONFIG['colors']['red'], [self.convert_coordinates(sensor_center),
                                                                               self.convert_coordinates(sens.left_point.get_position()),
                                                                               self.convert_coordinates(sens.max_point.get_position()),
                                                                               self.convert_coordinates(sens.right_point.get_position())], 1)
            
            # should be modified!
            radius = int(math.sqrt(width * width + height * height) / 2.0)
            center = (int(x), int(y))
            pygame.draw.circle(self.window, CONFIG['colors']['black'], self.convert_coordinates(center), radius, 1)

            surf = pygame.transform.scale(self.robot_img, (width, height))
            surf = self.rot_center(surf, math.degrees(theta))
            self.window.blit(surf, self.convert_coordinates((x - width / 2, y + height / 2))) # the image has bottom left corner as origin now

        pygame.display.update()

        return True
    
    def rot_center(self, image, angle):
        # rotate an image while keeping its center and size
        # https://www.pygame.org/wiki/RotateCenter?parent=CookBook

        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()

        return rot_image
