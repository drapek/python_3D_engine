import numpy as np

from scenes.objects.basic_polygon import Polygon


class Spheroid:
    nodes = None
    edges = None
    child_polygons = None

    def __init__(self, rx, ry, rz, start_point=None, color=(181, 181, 181), resolution=10):
        self.nodes = []
        self.child_polygons = []

        if start_point is None:
            start_point = [0, 0, 0, 1]
        # if specified start point has only 3 dimensions (x, y, z), add additional 1 to get 'normal' coordinates
        if len(start_point) == 3:
            start_point.append(1)

        latitudes = [n * np.pi / resolution for n in range(1, resolution)]
        longitudes = [n * 2 * np.pi / resolution for n in range(resolution)]

        # Add nodes except for poles
        self.nodes = [[start_point[0] + rx * np.sin(n) * np.sin(m),
                       start_point[1] - ry * np.cos(m),
                       start_point[2] - rz * np.cos(n) * np.sin(m),
                       1]
                      for m in latitudes for n in longitudes]

        # Add square faces to whole spheroid but poles
        num_nodes = resolution * (resolution - 1)
        face_list = ([(m + n,
                       (m + resolution) % num_nodes + n,
                       (m + resolution) % resolution ** 2 + (n + 1) % resolution,
                       m + (n + 1) % resolution)
                      for n in range(resolution) for m in range(0, num_nodes - resolution, resolution)])

        for node_list in face_list:
            num_nodes = len(node_list)
            if all((node < len(self.nodes) for node in node_list)):
                polygon_nodes = [self.nodes[node] for node in node_list]
                self.child_polygons.append(Polygon(polygon_nodes, color=color))
                self.edges = [(node_list[n - 1], node_list[n]) for n in range(num_nodes)]

        # Add poles and triangular faces around poles
        self.nodes += [(start_point[0], start_point[1] + ry, start_point[2], start_point[3]),
                       (start_point[0], start_point[1] - ry, start_point[2], start_point[3])]
        sphere_cup_nodes = [(n, (n + 1) % resolution, len(self.nodes) - 1) for n in range(resolution)]
        start_node = len(self.nodes) - resolution - 2  # because we already add 2 points to the end of the nodes list
        sphere_cup_nodes += [(len(self.nodes) - 2, start_node + (n + 1) % resolution, start_node + n)
                             for n in range(resolution)]

        for node_list in sphere_cup_nodes:
            nodes_cords = [self.nodes[node] for node in node_list]
            self.child_polygons.append(Polygon(nodes_cords, color=color))
