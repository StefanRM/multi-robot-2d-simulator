import pygame

DISP_TRACES_KEY = pygame.K_t
DISP_GRID_KEY = pygame.K_g

GRID_CELL_DIM = 20
DIST_BETWEEN_GRIDS = 1
TRACE_LINE_WIDTH = 2

class Gui:

    def __init__(self, period = 100, width = 500, height = 500, caption = "Multi-Robot 2D Simulator", background_color = (0, 0, 0), grid_color = -1):
        self.period = period # miliseconds
        self.width = width
        self.height = height
        self.caption = caption
        self.background_color = background_color
        if grid_color == -1:
            self.grid_color = (255 - background_color[0], 255 - background_color[1], 255 - background_color[2])
        else:
            self.grid_color = grid_color

        self.display_traces = False
        self.display_grid = False
        self.press_limiter_toggle_display_traces = False
        self.press_limiter_toggle_display_gird = False

        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

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

        if keys[DISP_TRACES_KEY]:
            if not self.press_limiter_toggle_display_traces:
                self.toggle_display_traces()
                self.press_limiter_toggle_display_traces = True
        else:
            self.press_limiter_toggle_display_traces = False
        
        if keys[DISP_GRID_KEY]:
            if not self.press_limiter_toggle_display_gird:
                self.toggle_display_grid()
                self.press_limiter_toggle_display_gird = True
        else:
            self.press_limiter_toggle_display_gird = False
            

        # drawing the grid
        if self.display_grid:
            self.window.fill(self.grid_color)
            for i in range(0, self.width, DIST_BETWEEN_GRIDS + GRID_CELL_DIM):
                for j in range(0, self.width, DIST_BETWEEN_GRIDS + GRID_CELL_DIM):
                    pygame.draw.rect(self.window, self.background_color, (i, j, GRID_CELL_DIM, GRID_CELL_DIM))
        else:
            self.window.fill(self.background_color)

        robots = world.get_robots()

        for robot in robots:
            trace = robot.get_trace()
            x = robot.get_coordinate_x()
            y = robot.get_coordinate_y()
            dimension = robot.get_dimensions()
            width = dimension["width"]
            height = dimension["height"]

            # drawing the traces
            if self.display_traces:
                for i in range(len(trace) - 1):
                    (a, b) = trace[i]
                    (c, d) = trace[i + 1]
                    start = (a + width / 2, b + height / 2)
                    stop = (c + width / 2, d + height / 2)
                    pygame.draw.line(self.window, robot.get_color(), start, stop, TRACE_LINE_WIDTH)
            
        for robot in robots:
            x = robot.get_coordinate_x()
            y = robot.get_coordinate_y()
            dimension = robot.get_dimensions()
            width = dimension["width"]
            height = dimension["height"]

            pygame.draw.rect(self.window, robot.get_color(), (x, y, width, height))

        pygame.display.update()

        return True
