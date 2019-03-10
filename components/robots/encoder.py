class Encoder:
    # TODO: What are the attributes of an encoder?
    #        -> ticks per revolution
    #        -> number of ticks

    def __init__(self, ticks_per_revolution):
        self.ticks_per_revolution = ticks_per_revolution
        self.total_nr_revolutions = 0.0
        self.tick_count = 0

    def update(self, revolutions):
        self.total_nr_revolutions += revolutions
        self.tick_count = int(self.total_nr_revolutions * self.ticks_per_revolution)

    def get_tick_count(self):
        return tick_count
