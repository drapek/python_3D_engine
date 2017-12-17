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

    def draw(self, screen, observer_distance, light_source, show_edges=True):
        try:
            polygon_points = [project_3d_point_to_2d(point, observer_distance) for point in self.nodes]
            color_with_shading = light_source.calculate_lighting(self)
            if color_with_shading is not None:
                # Do not draw empty polygons (with no color)
                pygame.draw.polygon(screen, color_with_shading, polygon_points)
            if show_edges:
                pygame.draw.polygon(screen, self.edges_color, polygon_points, 1)
        except Exception as e:
            print("[Warring] Polygon can't be drawn. Error body: ", e)

    def get_z_cords(self):
        """
        This function will return Z coordinates of each polygon point
        :return:
        """
        return [node[2] for node in self.nodes]

