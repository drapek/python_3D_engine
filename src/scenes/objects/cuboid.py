import pygame

from camera.functions import project_3d_point_to_2d
import settings
from scenes.objects.triangle import Triangle


class Cuboid:
    """
        Cuboid object.
        Cuboid parameter to scene parameters:
        width = X-axis
        deep = Y-axis
        height = Z-axis
    """
    child_triangles = None
    cubic_nodes = None
    # edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6),
    #          (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]

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

        self.cubic_nodes = []
        self.cubic_nodes.append(start_point)
        self.cubic_nodes.append([start_point[0] + width, start_point[1], start_point[2], 1])
        self.cubic_nodes.append([start_point[0] + width, start_point[1] + deep, start_point[2], 1])
        self.cubic_nodes.append([start_point[0], start_point[1] + deep, start_point[2], 1])
        self.cubic_nodes.append([start_point[0], start_point[1], start_point[2] + height, 1])
        self.cubic_nodes.append([start_point[0] + width, start_point[1], start_point[2] + height, 1])
        self.cubic_nodes.append([start_point[0] + width, start_point[1] + deep, start_point[2] + height, 1])
        self.cubic_nodes.append([start_point[0], start_point[1] + deep, start_point[2] + height, 1])

        # create the sub triangles for each cubic wall
        self.child_triangles = []
        self.child_triangles.append(Triangle(self.cubic_nodes[0], self.cubic_nodes[4], self.cubic_nodes[5]))
        self.child_triangles.append(Triangle(self.cubic_nodes[0], self.cubic_nodes[1], self.cubic_nodes[5]))

        self.child_triangles.append(Triangle(self.cubic_nodes[1], self.cubic_nodes[5], self.cubic_nodes[6]))
        self.child_triangles.append(Triangle(self.cubic_nodes[1], self.cubic_nodes[2], self.cubic_nodes[6]))

        self.child_triangles.append(Triangle(self.cubic_nodes[2], self.cubic_nodes[6], self.cubic_nodes[7]))
        self.child_triangles.append(Triangle(self.cubic_nodes[2], self.cubic_nodes[3], self.cubic_nodes[7]))

        self.child_triangles.append(Triangle(self.cubic_nodes[3], self.cubic_nodes[7], self.cubic_nodes[4]))
        self.child_triangles.append(Triangle(self.cubic_nodes[3], self.cubic_nodes[0], self.cubic_nodes[4]))

        self.child_triangles.append(Triangle(self.cubic_nodes[4], self.cubic_nodes[5], self.cubic_nodes[6]))
        self.child_triangles.append(Triangle(self.cubic_nodes[4], self.cubic_nodes[7], self.cubic_nodes[6]))

        self.child_triangles.append(Triangle(self.cubic_nodes[1], self.cubic_nodes[0], self.cubic_nodes[3]))
        self.child_triangles.append(Triangle(self.cubic_nodes[1], self.cubic_nodes[2], self.cubic_nodes[3]))

        self.divide_sub_triangles(number_of_times=4)

    def draw_on_screen(self, screen, observer_distance):
        for sub_triangle in self.child_triangles:
            for edge in sub_triangle.edges:
                line_from = project_3d_point_to_2d(sub_triangle.nodes[edge[0]], observer_distance)
                line_to = project_3d_point_to_2d(sub_triangle.nodes[edge[1]], observer_distance)
                pygame.draw.line(screen, settings.line_color, line_from, line_to, settings.line_thickness)

    def divide_sub_triangles(self, number_of_times=1):
        for i in range(number_of_times):
            new_child_triangles = []
            for sub_triangle in self.child_triangles:
                new_triangles = Triangle.divide(sub_triangle)
                new_child_triangles.append(new_triangles[0])
                new_child_triangles.append(new_triangles[1])
            self.child_triangles = new_child_triangles
