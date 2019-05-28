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

# returns True if midpoint is inside the segment determined by point1 and point2
def check_point_inside(point1, point2, midpoint):
    (x_m, y_m) = midpoint
    (x1, y1) = point1
    (x2, y2) = point2

    dxc = x_m - x1
    dyx = y_m - y1
    dxl = x2 - x1
    dyl = y2 - y1

    if (abs(dxl) >= abs(dyl)):
        if dxl > 0:
            return x1 <= x_m and x_m <= x2
        else:
            return x2 <= x_m and x_m <= x1
    else:
        if dyl > 0:
            return y1 <= y_m and y_m <= y2
        else:
            return y_m and y_m <= y1

# given sensor points (sensor center & sensor beam point), robot position and its radius,
# returns intersection points along the line determined by the sensor points
def find_intersection(sensor_center, sensor_beam_point, robot_pos, radius):
        res = []
        (x_sc, y_sc) = sensor_center
        (x_sb, y_sb) = sensor_beam_point
        (x_rob, y_rob) = robot_pos
        dx = x_sb - x_sc
        dy = y_sb - y_sc

        a = dx * dx + dy * dy
        b = 2 * (dx * (x_sc - x_rob) + dy * (y_sc - y_rob))
        c = (x_sc - x_rob) * (x_sc - x_rob) + (y_sc - y_rob) * (y_sc - y_rob) - radius * radius

        det = b * b - 4 * a * c
        if ((a <= 0.0000001) or (det < 0)):
            pass
        elif det == 0:
            t = - b / (2 * a)
            res.append((x_sc + t * dx, y_sc + t * dy))
        else:
            t = (- b + math.sqrt(det)) / (2 * a)
            res.append((x_sc + t * dx, y_sc + t * dy))
            t = (- b - math.sqrt(det)) / (2 * a)
            res.append((x_sc + t * dx, y_sc + t * dy))
        
        return res
    
def check_robot_collision(r1_center, r2_center, radius):
    (x1, y1) = r1_center
    (x2, y2) = r2_center

    dx = x1 - x2
    dy = y1 - y2

    return math.sqrt(dx * dx + dy * dy) < 2 * radius