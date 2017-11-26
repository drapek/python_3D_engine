import pygame

from camera.functions import project_3d_point_to_2d


class Polygon:
    nodes = None
    color = None
    edges_color = (0, 0, 0)

    def __init__(self, points, color=(0, 0, 0)):
        self.color = color
        self.nodes = []
        for point in points:
            self.nodes.append(point)

    def draw(self, screen, observer_distance, show_edges=True):
        try:
            polygon_points = [project_3d_point_to_2d(point, observer_distance) for point in self.nodes]
            pygame.draw.polygon(screen, self.color, polygon_points)
            if show_edges:
                pygame.draw.polygon(screen, self.edges_color, polygon_points, 1)
        except Exception as e:
            print("[Warring] Polygon can't we draw. Error body: ", e)

    def get_z_cords(self):
        """
        This function will return Z coordinates of each triangle point
        :return:
        """
        return [node[2] for node in self.nodes]

