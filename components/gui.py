import pygame

DISP_TRACES_KEY = pygame.K_t
DISP_GRID_KEY = pygame.K_g

class Gui:

    def __init__(self, period = 100, width = 500, height = 500, caption = "Air Simulator"):
        self.period = period # miliseconds
        self.width = width
        self.height = height
        self.caption = caption
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
            

        self.window.fill((0, 0, 0))

        robots = world.get_robots()

        for robot in robots:
            trace = robot.get_trace()
            x = robot.get_coordinate_x()
            y = robot.get_coordinate_y()
            dimension = robot.get_dimensions()
            width = dimension["width"]
            height = dimension["height"]

            if self.display_traces:
                for i in range(len(trace) - 1):
                    (a, b) = trace[i]
                    (c, d) = trace[i + 1]
                    start = (a + width / 2, b + height / 2)
                    stop = (c + width / 2, d + height / 2)
                    pygame.draw.line(self.window, robot.get_color(), start, stop)
            
        for robot in robots:
            x = robot.get_coordinate_x()
            y = robot.get_coordinate_y()
            dimension = robot.get_dimensions()
            width = dimension["width"]
            height = dimension["height"]

            pygame.draw.rect(self.window, robot.get_color(), (x, y, width, height))

        pygame.display.update()

        return True
