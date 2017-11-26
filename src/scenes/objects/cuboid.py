from scenes.objects.triangle import Triangle


class Cuboid:
    """
        Cuboid object.
        Cuboid parameter to scene parameters:
        width = X-axis
        deep = Y-axis
        height = Z-axis
    """
    child_polygons = None
    cubic_nodes = None

    def __init__(self, width, depth, height, start_point=None, color=(255, 105, 180)):
        """
        4 dimensions because it is normal coordinate system
        :param width:
        :param depth:
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
        self.cubic_nodes.append([start_point[0] + width, start_point[1] + depth, start_point[2], 1])
        self.cubic_nodes.append([start_point[0], start_point[1] + depth, start_point[2], 1])
        self.cubic_nodes.append([start_point[0], start_point[1], start_point[2] + height, 1])
        self.cubic_nodes.append([start_point[0] + width, start_point[1], start_point[2] + height, 1])
        self.cubic_nodes.append([start_point[0] + width, start_point[1] + depth, start_point[2] + height, 1])
        self.cubic_nodes.append([start_point[0], start_point[1] + depth, start_point[2] + height, 1])

        # create the sub triangles for each cubic wall
        self.child_polygons = []
        self.child_polygons.append(Triangle(self.cubic_nodes[0], self.cubic_nodes[4], self.cubic_nodes[5], color=color))
        self.child_polygons.append(Triangle(self.cubic_nodes[0], self.cubic_nodes[1], self.cubic_nodes[5], color=color))

        self.child_polygons.append(Triangle(self.cubic_nodes[1], self.cubic_nodes[5], self.cubic_nodes[6], color=color))
        self.child_polygons.append(Triangle(self.cubic_nodes[1], self.cubic_nodes[2], self.cubic_nodes[6], color=color))

        self.child_polygons.append(Triangle(self.cubic_nodes[2], self.cubic_nodes[6], self.cubic_nodes[7], color=color))
        self.child_polygons.append(Triangle(self.cubic_nodes[2], self.cubic_nodes[3], self.cubic_nodes[7], color=color))

        self.child_polygons.append(Triangle(self.cubic_nodes[3], self.cubic_nodes[7], self.cubic_nodes[4], color=color))
        self.child_polygons.append(Triangle(self.cubic_nodes[3], self.cubic_nodes[0], self.cubic_nodes[4], color=color))

        self.child_polygons.append(Triangle(self.cubic_nodes[4], self.cubic_nodes[5], self.cubic_nodes[6], color=color))
        self.child_polygons.append(Triangle(self.cubic_nodes[4], self.cubic_nodes[7], self.cubic_nodes[6], color=color))

        self.child_polygons.append(Triangle(self.cubic_nodes[1], self.cubic_nodes[0], self.cubic_nodes[3], color=color))
        self.child_polygons.append(Triangle(self.cubic_nodes[1], self.cubic_nodes[2], self.cubic_nodes[3], color=color))

        self._divide_sub_triangles(number_of_times=4)

    def _divide_sub_triangles(self, number_of_times=1):
        for i in range(number_of_times):
            new_child_triangles = []
            for sub_triangle in self.child_polygons:
                new_triangles = Triangle.divide(sub_triangle, color=sub_triangle.color)
                new_child_triangles.append(new_triangles[0])
                new_child_triangles.append(new_triangles[1])
            self.child_polygons = new_child_triangles


