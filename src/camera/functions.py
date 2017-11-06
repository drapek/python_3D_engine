import math
import numpy as np
from src import settings


def project_3d_point_to_2d(point_3d, observer_distance):
    """
    This function will project 3d point on 2d point which can be drawn on canvas.
    :param observer_distance: the length between observer and the canvas
    :param point_3d: tuple (x, y, z)
    :return point_2d: tuple (x, y)
    """

    screen_center_vertical = settings.scree_height / 2
    screen_center_horizontal = settings.scree_width / 2
    p_2d_x = screen_center_horizontal + ((point_3d[0] * observer_distance) / (point_3d[2] + observer_distance))
    p_2d_y = screen_center_vertical + ((point_3d[1] * observer_distance) / (point_3d[2] + observer_distance))
    # We must flip the y coordinate to gain not upside down image
    p_2d_y = settings.scree_height - p_2d_y
    return p_2d_x, p_2d_y


def move(obj, vector_3d):
    move_matrix = [[1, 0, 0, vector_3d[0]],
                   [0, 1, 0, vector_3d[1]],
                   [0, 0, 1, vector_3d[2]],
                   [0, 0, 0, 1]]
    multiply_object_by_matrix(obj, move_matrix)


def rotate_x(obj, angle):
    rotate_matrix = [[1, 0, 0, 0],
                     [0, math.cos(angle), -math.sin(angle), 0],
                     [0, math.sin(angle), math.cos(angle), 0],
                     [0, 0, 0, 1]]
    multiply_object_by_matrix(obj, rotate_matrix)


def rotate_y(obj, angle):
    rotate_matrix = [[math.cos(angle), 0, math.sin(angle), 0],
                     [0, 1, 0, 0],
                     [-math.sin(angle), 0, math.cos(angle), 0],
                     [0, 0, 0, 1]]
    multiply_object_by_matrix(obj, rotate_matrix)


def rotate_z(obj, angle):
    rotate_matrix = [[math.cos(angle), -math.sin(angle), 0, 0],
                     [math.sin(angle), math.cos(angle), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]]
    multiply_object_by_matrix(obj, rotate_matrix)


def multiply_object_by_matrix(obj, matrix):
    for i, point in enumerate(obj.nodes):
        obj.nodes[i] = np.matmul(matrix, point)
