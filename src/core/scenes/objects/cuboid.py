import pygame
import numpy as np
import math

from core.camera.functions import project_3d_point_to_2d, point_2d_to_pixel_position, center_world_origin
from core import settings


class Cuboid:
    """
        Cuboid object.
        Cuboid parameter to scene parameters:
        width = X-axis
        deep = Y-axis
        height = Z-axis
    """
    nodes = None
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6),
             (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]

    def __init__(self, width, deep, height, start_point=None):
        """
        4 dimensions because it is normal coordinate system
        :param width:
        :param deep:
        :param height:
        :param start_point:
        """
        # Because default parameter can't be immutable
        if start_point is None:
            start_point = [0, 0, 0, 1]
        # if smb inserted only 3 (x, y, z) dimensions, add additional 1 to get 'normal' coordinates
        if len(start_point) == 3:
            start_point.append(1)

        self.nodes = []
        self.nodes.append(start_point)
        self.nodes.append([start_point[0] + width, start_point[1], start_point[2], 1])
        self.nodes.append([start_point[0] + width, start_point[1] + deep, start_point[2], 1])
        self.nodes.append([start_point[0], start_point[1] + deep, start_point[2], 1])
        self.nodes.append([start_point[0], start_point[1], start_point[2] + height, 1])
        self.nodes.append([start_point[0] + width, start_point[1], start_point[2] + height, 1])
        self.nodes.append([start_point[0] + width, start_point[1] + deep, start_point[2] + height, 1])
        self.nodes.append([start_point[0], start_point[1] + deep, start_point[2] + height, 1])

    def draw_on_screen(self, screen, observer_distance):
        for edge in self.edges:
            line_from = project_3d_point_to_2d(self.nodes[edge[0]], observer_distance)
            line_to = project_3d_point_to_2d(self.nodes[edge[1]], observer_distance)
            # Flip the y coordinates, to not have upside down image
            line_from = point_2d_to_pixel_position(line_from)
            line_to = point_2d_to_pixel_position(line_to)
            # # center the world origin
            # line_from = center_world_origin(line_from)
            # line_to = center_world_origin(line_to)
            pygame.draw.line(screen, settings.line_color, line_from, line_to, settings.line_thickness)

    def move(self, vector_3d):
        move_matrix = [[1, 0, 0, vector_3d[0]],
                       [0, 1, 0, vector_3d[1]],
                       [0, 0, 1, vector_3d[2]],
                       [0, 0, 0, 1]]
        self.multiply_object_by_matrix(move_matrix)

    def rotate_x(self, angle):
        rotate_matrix = [[1, 0, 0, 0],
                         [0, math.cos(angle), -math.sin(angle), 0],
                         [0, math.sin(angle), math.cos(angle), 0],
                         [0, 0, 0, 1]]
        self.multiply_object_by_matrix(rotate_matrix)

    def rotate_y(self, angle):
        rotate_matrix = [[math.cos(angle), 0, math.sin(angle), 0],
                         [0, 1, 0, 0],
                         [-math.sin(angle), 0, math.cos(angle), 0],
                         [0, 0, 0, 1]]
        self.multiply_object_by_matrix(rotate_matrix)

    def rotate_z(self, angle):
        rotate_matrix = [[math.cos(angle), -math.sin(angle), 0, 0],
                         [math.sin(angle), math.cos(angle), 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]]
        self.multiply_object_by_matrix(rotate_matrix)

    def multiply_object_by_matrix(self, matrix):
        for i, point in enumerate(self.nodes):
            self.nodes[i] = np.matmul(matrix, point)
