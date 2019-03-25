import math


class Encoder:
    # TODO: What are the attributes of an encoder?
    #        -> ticks per revolution --> this is the encoder resolution
    #        -> number of ticks --> this is the encoder tick_count since initialisation

    def __init__(self, resolution):
        self.resolution = resolution
        self.tick_count = 0

    # TODO: this will be called by the engine to update the encoder tick count
    #   -> Having the resolution (i.e. counts/2*pi) and the wheel angle in this iteration,
    #      update the number of encoder ticks
    def update(self, wheel_angle):
        pass

    def get_tick_count(self):
        return self.tick_count
