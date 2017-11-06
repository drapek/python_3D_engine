import pygame
import numpy as np
import math

from core.camera.functions import project_3d_point_to_2d
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
        if start_point is None:
            start_point = [0, 0, 0, 1]
        # if specified start point has only 3 dimensions (x, y, z), add additional 1 to get 'normal' coordinates
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
            pygame.draw.line(screen, settings.line_color, line_from, line_to, settings.line_thickness)

