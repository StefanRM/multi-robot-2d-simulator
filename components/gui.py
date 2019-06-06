import pygame
import math
from components.config import CONFIG


class Gui:

    def __init__(self,
                 robots_trace_col,
                 robots_scale=CONFIG['robots_scale'],
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
        
        self.robots_scale = robots_scale
        self.robots_trace_col = robots_trace_col

        self.display_traces = True
        self.display_grid = True
        self.display_sensors = False
        self.press_limiter_toggle_display_traces = False
        self.press_limiter_toggle_display_grid = False
        self.press_limiter_toggle_display_sensors = False

        pygame.init()
        self.window = pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        pygame.display.set_caption(caption)

        # origin of the axis for a 4 quadrant map
        self.origin_x = 0
        self.origin_y = height - CONFIG['DIST_BUTTONS']

        # robot symbol
        self.robot_img = pygame.image.load(CONFIG['path_to_robot_image'])

        # font and size of axis' numbers and buttons' texts
        self.text_font = pygame.font.Font('freesansbold.ttf', 15)

        # pause simulation
        self.pause = False
    
    def toggle_pause(self):
        self.pause = not self.pause
    
    def button(self, msg, x, y, w, h, before_col, after_col, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.window, after_col, (x, y, w, h))

            if click[0] == 1 and action != None:
                action()         
        else:
            pygame.draw.rect(self.window, before_col, (x , y, w, h))

        text_surface = self.text_font.render(msg, True, CONFIG['colors']['white'])
        text_rect = text_surface.get_rect()
        text_rect.center = ((x + (w / 2)), (y + (h / 2)))
        self.window.blit(text_surface, text_rect)
    
    # convert coordinates the window system of coordinates
    def convert_coordinates(self, position):
        (x, y) = position
        return (self.origin_x + self.robots_scale * x, self.origin_y - self.robots_scale * y)

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
                return (False, self.pause)
            elif event.type == pygame.VIDEORESIZE:
                self.window=pygame.display.set_mode(event.dict['size'], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

                # update the new width and height
                (width, height) = event.dict['size']
                self.width = width
                self.height = height

                # origin of the axis for a 4 quadrant map
                self.origin_x = 0
                self.origin_y = height - CONFIG['DIST_BUTTONS']


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

        if keys[CONFIG['PAUSE_SIM_KEY']]:
            if not self.press_limiter_toggle_pause:
                self.toggle_pause()
                self.press_limiter_toggle_pause = True
        else:
            self.press_limiter_toggle_pause = False
            

        # drawing the grid
        if self.display_grid:
            self.window.fill(self.grid_color)
            for i in range(0, self.width, CONFIG['DIST_BETWEEN_GRIDS'] + CONFIG['GRID_CELL_DIM']):
                for j in range(CONFIG['DIST_BETWEEN_GRIDS'] + CONFIG['GRID_CELL_DIM'], self.width, CONFIG['DIST_BETWEEN_GRIDS'] + CONFIG['GRID_CELL_DIM']):
                    pygame.draw.rect(self.window, self.background_color, (i, self.origin_y - j, CONFIG['GRID_CELL_DIM'], CONFIG['GRID_CELL_DIM']))

            # OX axis
            pygame.draw.line(self.window, CONFIG['colors']['gray'], (self.origin_x, self.origin_y), (self.origin_x + self.width, self.origin_y), CONFIG['AXIS_LINE_WIDTH'])
            for i in range(0, self.width, CONFIG['robots_scale']):
                pygame.draw.line(self.window, CONFIG['colors']['gray'], (i - 1/2, self.origin_y), (i - 1/2, self.origin_y - 10), CONFIG['UNIT_LINE_WIDTH'])
                
                if i > 0:
                    text_surface = self.text_font.render(str(int(i / CONFIG['robots_scale'])), True, CONFIG['colors']['gray'])
                    text_surf, text_rect = text_surface, text_surface.get_rect()
                    text_rect.center = (i - 1/2, self.origin_y - 15)
                    self.window.blit(text_surf, text_rect)

            # OY axis
            pygame.draw.line(self.window, CONFIG['colors']['gray'], (self.origin_x, self.origin_y), (self.origin_x, self.origin_y - self.height), CONFIG['AXIS_LINE_WIDTH'])
            for j in range(0, self.height, CONFIG['robots_scale']):
                pygame.draw.line(self.window, CONFIG['colors']['gray'], (self.origin_x, self.origin_y - j - 1/2), (self.origin_x + 10, self.origin_y - j - 1/2), CONFIG['UNIT_LINE_WIDTH'])
                
                if j > 0:
                    text_surface = self.text_font.render(str(int(j / CONFIG['robots_scale'])), True, CONFIG['colors']['gray'])
                    text_surf, text_rect = text_surface, text_surface.get_rect()
                    text_rect.center = (self.origin_x + 15, self.origin_y - j - 1/2)
                    self.window.blit(text_surf, text_rect)

        else:
            self.window.fill(self.background_color)

        robots = world.get_robots()


        for it, robot in enumerate(robots):
            trace = world.get_robot_trace(it)
            (x, y) = robot.get_pose().get_position()

            # drawing the traces
            if self.display_traces:
                for i in range(len(trace) - 1):
                    (a, b) = trace[i]
                    (c, d) = trace[i + 1]
                    start = self.convert_coordinates((a, b))
                    stop = self.convert_coordinates((c, d))
                    pygame.draw.line(self.window, self.robots_trace_col[it], start, stop, CONFIG['TRACE_LINE_WIDTH'])
        
        # drawing the buttons
        self.button("Play / Pause", self.origin_x + self.width / 2, self.origin_y + CONFIG['TEXT_MARGIN_UP'], CONFIG['TEXT_DIM_WIDTH'], CONFIG['TEXT_DIM_HEIGHT'], CONFIG['colors']['green'], CONFIG['colors']['lime'], self.toggle_pause)


        for it, robot in enumerate(robots):
            (x, y) = robot.get_pose().get_position()
            theta = robot.get_pose().get_heading()

            if self.display_sensors:
                sensors = robot.get_sensors()
                for sens in sensors:
                    (x_sens, y_sens) = sens.pose.get_position()

                    sensor_center = (x + x_sens, y + y_sens)
                    sensor_center_conv = self.convert_coordinates(sensor_center)

                    pygame.draw.circle(self.window, CONFIG['colors']['red'], (int(sensor_center_conv[0]), int(sensor_center_conv[1])), 3, 3)

                    sensor_points = [(int(sensor_center_conv[0]), int(sensor_center_conv[1]))]
                    for point in sens.beam_left_points:
                        sensor_points.append(self.convert_coordinates(point.get_position()))
                    sensor_points.append(self.convert_coordinates(sens.max_point.get_position()))
                    for point in sens.beam_right_points:
                        sensor_points.append(self.convert_coordinates(point.get_position()))

                    pygame.draw.polygon(self.window, CONFIG['colors']['red'], sensor_points, 1)
            
            radius = robot.geometry.radius
            center = (x, y)
            center_conv = self.convert_coordinates(center)
            pygame.draw.circle(self.window, CONFIG['colors']['black'], (int(center_conv[0]), int(center_conv[1])), int(radius * self.robots_scale), 1)

            surf = pygame.transform.scale(self.robot_img, (int(radius * self.robots_scale * math.sqrt(2)), int(radius * self.robots_scale * math.sqrt(2))))
            surf = self.rot_center(surf, math.degrees(theta))
            self.window.blit(surf, self.convert_coordinates((x - radius * math.sqrt(2) / 2, y + radius * math.sqrt(2) / 2))) # the image has bottom left corner as origin now

        pygame.display.update()

        return (True, self.pause)
    
    def rot_center(self, image, angle):
        # rotate an image while keeping its center and size
        # https://www.pygame.org/wiki/RotateCenter?parent=CookBook

        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()

        return rot_image
