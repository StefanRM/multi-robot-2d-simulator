class Encoder:
    # TODO: What are the attributes of an encoder?
    #        -> ticks per revolution
    #        -> number of ticks

    def __init__(self, ticks_per_revolution):
        self.ticks_per_revolution = ticks_per_revolution
        self.tick_count = 0

    def update(self, ticks = 1):
        self.tick_count += ticks

    def get_tick_count(self):
        return tick_count
