import math
from components import utilities

def listmann(robots):
    dc = 2
    ud = 0.1
    thetad = - math.pi / 4
    for robot in robots:
        ui = 0
        wi = 0
        print("{}: {}".format(robot.id, robot.neigh_list))
        for neigh in robot.neigh_list:
            (ot_rid, sens_id, d) = neigh
            (xi, yi) = robot.get_pose().get_position()
            thetai = robot.get_pose().get_heading()
            (xj, yj) = robots[ot_rid].get_pose().get_position()

            kd = 1 - math.exp(dc - d * d)
            gy = -((xi - xj) * math.cos(thetai) + (yi - yj) * math.sin(thetai)) * kd

            ui += gy

            # phiij = robot.get_sensors()[sens_id].get_pose().get_heading()
            phiij = math.atan2(yj - yi, xj - xi)
            wi += -(thetai - kd * phiij) + (kd - 1) * thetad

        print(ui)
        robot.move(ui + ud, wi)

def novischi(robots):
    ku = 1
    vmax = 0.02
    alfa = 1
    ud = 0.1
    thetad = - math.pi / 4
    ds = 0.2
    kalfa = 1
    dc = 1
    for robot in robots:
        ui = 0
        wi = 0
        print("{}: {}".format(robot.id, robot.neigh_list))
        for neigh in robot.neigh_list:
            (ot_rid, sens_id, d) = neigh
            (xi, yi) = robot.get_pose().get_position()
            thetai = robot.get_pose().get_heading()
            (xj, yj) = robots[ot_rid].get_pose().get_position()

            sigma = 2.0 / (1 + math.exp(- (dc - d * d)))
            gy = ((xi - xj) * math.cos(thetai) + (yi - yj) * math.sin(thetai))

            if (d <= ds):
                alfa = kalfa
            else:
                alfa = 1

            ui += utilities.sgn(gy) * (1 - alfa * sigma)

            # phiij = robot.get_sensors()[sens_id].get_pose().get_heading()
            phiij = math.atan2(yj - yi, xj - xi)
            wi += -(thetai - (1 - sigma) * phiij) - sigma * thetad
        
        print(ui)

        ui = - ku * vmax * ui + ud
        robot.move(ui, wi)

def gasparri(robots):
    dc = 2
    ud = 0.1
    thetad = - math.pi / 4
    for robot in robots:
        sum_dist = 1
        ui = 0
        wi = 0
        print("{}: {}".format(robot.id, robot.neigh_list))
        for neigh in robot.neigh_list:
            (ot_rid, sens_id, d) = neigh
            (xi, yi) = robot.get_pose().get_position()
            thetai = robot.get_pose().get_heading()
            (xj, yj) = robots[ot_rid].get_pose().get_position()

            kd = 1 - math.exp(dc - d * d)
            gy = -((xi - xj) * math.cos(thetai) + (yi - yj) * math.sin(thetai)) * kd
            sum_dist += d * d

            ui += gy

            # phiij = robot.get_sensors()[sens_id].get_pose().get_heading()
            phiij = math.atan2(yj - yi, xj - xi)
            wi += -(thetai - kd * phiij) + (kd - 1) * thetad

        print(ui)
        ui = ui / sum_dist + ud
        robot.move(ui, wi)