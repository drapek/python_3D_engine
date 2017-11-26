from scenes.objects.basic_polygon import Polygon


def count_line_length(start_point, end_point):
    width = abs(start_point[0] - end_point[0])
    height = abs(start_point[1] - end_point[1])
    deep = abs(start_point[2] - end_point[2])
    return width ** 2 + height ** 2 + deep ** 2


def count_line_central_point(start_point, end_point):
    x = (start_point[0] + end_point[0]) / 2
    y = (start_point[1] + end_point[1]) / 2
    z = (start_point[2] + end_point[2]) / 2
    return [x, y, z, 1]


def divide_triangle(triangle, color):
    max_length = 0
    longest_line_index = 0
    triangle_edges = [(0, 1), (1, 2), (2, 0)]
    for i, edge in enumerate(triangle_edges):
        line_length = count_line_length(triangle.nodes[edge[0]], triangle.nodes[edge[1]])
        if line_length > max_length:
            max_length = line_length
            longest_line_index = i
    longest_line_edges = triangle_edges[longest_line_index]
    line_central_point = count_line_central_point(triangle.nodes[longest_line_edges[0]],
                                                  triangle.nodes[longest_line_edges[1]])
    # Create two sub-triangles
    new_small_triangles = []
    for i, edge in enumerate(triangle_edges):
        if i == longest_line_index:
            continue
        new_small_triangles.append(Polygon([triangle.nodes[edge[0]], triangle.nodes[edge[1]], line_central_point],
                                           color=color))
    return new_small_triangles
