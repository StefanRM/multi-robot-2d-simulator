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
        self.press_limiter_toggle_display_traces = False
        self.press_limiter_toggle_display_grid = False

        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

        # origin of the axis for a 4 quadrant map
        self.origin_x = 0
        self.origin_y = height

        # robot symbol
        self.robot_img = pygame.image.load("resources/robot_model_04.png")
    
    # convert coordinates the window system of coordinates
    def convert_coordinates(self, position):
        (x, y) = position
        return (self.origin_x + x, self.origin_y - y)

    def toggle_display_traces(self):
        self.display_traces = not self.display_traces
    
    def toggle_display_grid(self):
        self.display_grid = not self.display_grid

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
                    start = self.convert_coordinates((a + width / 2, b + height / 2))
                    stop = self.convert_coordinates((c + width / 2, d + height / 2))
                    pygame.draw.line(self.window, self.robots_trace_col[it], start, stop, CONFIG['TRACE_LINE_WIDTH'])
            
        for it, robot in enumerate(robots):
            (x, y) = robot.get_pose().get_position()
            dimension = self.robots_dim
            width = dimension["width"]
            height = dimension["height"]

            # pygame.draw.rect(self.window, robot.get_color(), (x, y, width, height))
            theta = robot.get_pose().get_heading()
            surf = pygame.transform.scale(self.robot_img, (width, height))
            surf = pygame.transform.rotate(surf, math.degrees(theta))
            self.window.blit(surf, self.convert_coordinates((x, y + height))) # the image has bottom left corner as origin now

        pygame.display.update()

        return True
