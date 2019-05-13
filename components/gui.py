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
        self.window = pygame.display.set_mode((width, height))
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
                radius = int(math.sqrt(width * width + height * height) / 2.0)
                center = (int(x), int(y))
                sensor_center = (int(x + radius * math.cos(theta + math.pi)), int(y + radius * math.sin(theta + math.pi)))
                pygame.draw.circle(self.window, CONFIG['colors']['black'], self.convert_coordinates(center), radius, 1)
                pygame.draw.circle(self.window, CONFIG['colors']['red'], self.convert_coordinates(sensor_center), 5, 5)

                # sensors beams
                (x_c, y_c) = (center[0], center[1])
                (x_s, y_s) = (sensor_center[0], sensor_center[1])
                d = 20
                pygame.draw.circle(self.window, CONFIG['colors']['green'], self.convert_coordinates(center), radius + d, 1)
                if x_s - x_c == 0:
                    x_d = x_s
                    if y_c < y_s:
                        y_d = y_s + d
                    else:
                        y_d = y_s - d
                else:
                    m = abs((y_s - y_c) / (x_s - x_c))
                    if x_c < x_s:
                        x_d = x_s + d / math.sqrt(m * m + 1)
                    else:
                        x_d = x_s - d / math.sqrt(m * m + 1)

                    if y_c < y_s:
                        y_d = y_s + d * m / math.sqrt(m * m + 1)
                    else:
                        y_d = y_s - d * m / math.sqrt(m * m + 1)
                pygame.draw.line(self.window, CONFIG['colors']['red'], self.convert_coordinates(sensor_center), self.convert_coordinates((x_d, y_d)), 5)
            
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
