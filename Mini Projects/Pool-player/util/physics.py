from util.settings import *

import math
import numpy as np
from shapely.geometry import Point
from shapely.geometry import LineString
from scipy.spatial.distance import cdist

def distance_between_two_points(p1, p2):
    dist_diff = p1 - p2
    return np.hypot(*dist_diff)

def point_in_rectangle(point, rect):
    x1, x2, y1, y2 = rect
    x, y = point
    if (x1 < x and x < x2):
        if (y1 < y and y < y2):
            return True
    return False

def inverse_angle(angle, calibrator=0):
    return (180 - angle) + calibrator

def extend_line_to(start_point, mid_point, length=900):
    theta = np.arctan2(start_point[1] - mid_point[1], start_point[0] - mid_point[0])
    if length < 0:
        return (int(mid_point[0] - length * np.cos(theta)), int(mid_point[1] - length * np.sin(theta)))
    return (int(start_point[0] - length * np.cos(theta)), int(start_point[1] - length * np.sin(theta)))

def get_center_from_pred(prediction):
    return np.array([int((prediction[0] + prediction[2]) / 2), 
                    int((prediction[1] + prediction[3]) / 2)])

def remove_duplicate_points(points_array):
    sorted_idx = np.lexsort(points_array.T)
    sorted_data = points_array[sorted_idx, :]
    row_mask = np.append([True], np.any(np.diff(sorted_data, axis=0), 1))

    return sorted_data[row_mask]

def closest_node(node, nodes, return_index=False):
    dist = cdist([node], nodes)
    if return_index:
        return dist.argmin()
    return nodes[dist.argmin()]

def point_line_eqtn(pt1, pt2):
    # y = mx + b
    x_coords, y_coords = zip(*[pt1, pt2])
    a = np.vstack([x_coords, np.ones(len(x_coords))]).T
    m, b = np.linalg.lstsq(a, y_coords)[0]
    return m, b

def general_line_eqtn(pt1, pt2):
    # Ax + By = C
    (x1, y1), (x2, y2) = pt1, pt2
    a = y1 - y2
    b = x2 - x1
    c = (x1 - x2) * y1 + (y2 - y1) * x1
    return a, b, c

def check_collision(a, b, c, x, y, radius):
    # finding the distance of line from center.
    dist = ((abs(a * x + b * y + c)) /
            math.sqrt(a * a + b * b))
    
    return radius >= dist

def circle_line_intersection(cue_ball_center, ball, end_pt, radius=8):
    p = Point(ball[0], ball[1])
    c = p.buffer(radius).boundary
    l = LineString([cue_ball_center, end_pt])
    i = c.intersection(l)
    if i:
        try:
            i1, i2 = i.geoms[0].coords[0], i.geoms[1].coords[0]
            intersections = closest_node(cue_ball_center, [i1, i2])
        except AttributeError:
            intersections = i.coords[0]

        return np.round(intersections).astype(int)

    return None

def bounce(pt1, pt2, degrees=1, return_bounded=False):
    inside_pt = None
    outside_pt = None
    reversed_pt = None
    if not point_in_rectangle(pt1, RAIL_LOCATION):
        outside_pt = pt1
        inside_pt = pt2
    elif not point_in_rectangle(pt2, RAIL_LOCATION):
        outside_pt = pt2
        inside_pt = pt1
    
    if outside_pt is None:
        return None
    
    m, b = point_line_eqtn(inside_pt, outside_pt)
    if outside_pt[0] < RAIL_LOCATION[0]:
        outside_pt = (RAIL_LOCATION[0], m * RAIL_LOCATION[0] + b)
        y = outside_pt[1] - inside_pt[1]
        reversed_pt = (inside_pt[0], inside_pt[1] + 2 * y)
    elif outside_pt[0] > RAIL_LOCATION[1]:
        outside_pt = (RAIL_LOCATION[1], m * RAIL_LOCATION[1] + b)
        y = outside_pt[1] - inside_pt[1]
        reversed_pt = (inside_pt[0], inside_pt[1] + 2 * y)
    elif outside_pt[1] < RAIL_LOCATION[3]:
        outside_pt = ((RAIL_LOCATION[2] - b) / m, RAIL_LOCATION[2])
        x = outside_pt[0] - inside_pt[0]
        reversed_pt = (inside_pt[0] + 2 * x, inside_pt[1])
    else:
        outside_pt = ((RAIL_LOCATION[3] - b) / m, RAIL_LOCATION[3])
        x = outside_pt[0] - inside_pt[0]
        reversed_pt = (inside_pt[0] + 2 * x, inside_pt[1])
    if return_bounded:
        return outside_pt
    
    return outside_pt, bounce(extend_line_to(outside_pt, reversed_pt), outside_pt, return_bounded=True)

    
