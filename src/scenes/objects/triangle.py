from exceptions import ToFewPointsError, ToFewCoordinatesError
from scenes.objects.functions import count_line_length, count_line_central_point


class Triangle:
    nodes = None
    edges = [(0, 1), (1, 2), (2, 0)]

    def __init__(self, *points):
        self.nodes = []
        if len(points) < 3:
            raise ToFewPointsError('Triangle need 3 points!')

        for point in points:
            if len(point) < 3:
                raise ToFewCoordinatesError('This is 3d projection - the minimum number of coordinates is 3.')
            self.nodes.append(point)

    @staticmethod
    def divide(triangle):
        # TODO find the longest line
        max_length = 0
        longest_line_index = 0
        for i, edge in enumerate(triangle.edges):
            line_length = count_line_length(triangle.nodes[edge[0]], triangle.nodes[edge[1]])
            if line_length > max_length:
                max_length = line_length
                longest_line_index = i
        longest_line_edges = triangle.edges[longest_line_index]
        line_central_point = count_line_central_point(triangle.nodes[longest_line_edges[0]],
                                                      triangle.nodes[longest_line_edges[1]])
        # Now create two sub-triangles
        new_small_triangles = []
        for i, edge in enumerate(triangle.edges):
            if i == longest_line_index:
                continue
            new_small_triangles.append(Triangle(triangle.nodes[edge[0]], triangle.nodes[edge[1]], line_central_point))
        return new_small_triangles


