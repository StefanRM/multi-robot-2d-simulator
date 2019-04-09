import math

def sign(x):
    if x >= 0:
        return 1.0
    else:
        return -1

# returns an angle between [-pi, pi]
def normalize_angle(angle):
    while angle < -math.pi:
        angle += 2 * math.pi
    while angle > math.pi:
        angle -= 2 * math.pi

    return angle