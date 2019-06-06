import pygame

CONFIG = {
    'colors': {
        'red': (255, 0, 0),
        'lime': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 215, 0),
        'magenta': (255, 0, 255),
        'cyan': (0, 255, 255),
        'white': (255, 255, 255),
        'black': (0, 0, 0, 0),
        'silver': (192, 192, 192),
        'gray': (128, 128, 128),
        'maroon': (128, 0, 0),
        'olive': (128, 128, 0),
        'green': (0, 128, 0),
        'purple': (128, 0, 128),
        'teal': (0, 128, 128),
        'navy': (0, 0, 128),
        'light-gray': (211, 211, 211),
    },

    # in world
    'WORLD_UNIT_TIME': 0.05, # seconds

    # in gui
    'GUI_PERIOD_TIME': 50, # miliseconds
    'win_caption': "Multi-Robot 2D Simulator",

    'DISP_TRACES_KEY': pygame.K_t,
    'DISP_GRID_KEY': pygame.K_g,
    'DISP_SENSORS_KEY': pygame.K_s,
    'PAUSE_SIM_KEY': pygame.K_p,

    'GRID_CELL_DIM': 19,
    'DIST_BETWEEN_GRIDS': 1,
    'TRACE_LINE_WIDTH': 2,
    'AXIS_LINE_WIDTH': 5,
    'UNIT_LINE_WIDTH': 3,

    'DIST_BUTTONS' : 40,
    'TEXT_DIM_HEIGHT' : 35,
    'TEXT_DIM_WIDTH' : 100,
    'TEXT_MARGIN_UP' : 4,

    'robots_scale': 40,

    'win_width': 1080,
    'win_height': 720,

    'path_to_robot_image': "resources/robot_model_04.png",

    'sensor_max_range': 3.2,
    'sensor_beam_part_points': 1,
}