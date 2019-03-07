class DifferentialDrive:

    ''' TODO: The differential drive is composed of two motors which we must simulate.
              To acomplishs this, you must compute the number of revolutions (turns) in this
              world-loop iteration.

    '''

    # TODO: You need to know vl/vr and number of revolutions for each motor
    def __init__(self, wheel_radius, wheel_base):
        # robot physical properties
        self.wheel_radius = wheel_radius # R
        self.wheel_base = wheel_base # L

        # wheel speeds (initially zero)
        self.vl = 0
        self.vr = 0

    # TODO: you must pass the duration of the world-loop iteration here
    def update(self, speed, angular_velocity, world_loop_time):
        # still thinking        

    # TODO; return a the list [vl, vr] -> instead i use a tuple for ease: (vl, vr) = get_revs()
    def get_revolutions(self):
        return (vl, vr)

    # TODO; Set the drive angular rates
    def set_rates(self, vl, vr):
        self.vl = vl
        self.vr = vr
