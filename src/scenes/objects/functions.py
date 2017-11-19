

def count_line_length(start_point, end_point):
    width = abs(start_point[0] - end_point[0])
    hight = abs(start_point[1] - end_point[1])
    deep = abs(start_point[2] - end_point[2])
    return width**2 + hight**2 + deep**2


def count_line_central_point(start_point, end_point):
    x = (start_point[0] + end_point[0]) / 2
    y = (start_point[1] + end_point[1]) / 2
    z = (start_point[2] + end_point[2]) / 2
    return [x, y, z, 1]
