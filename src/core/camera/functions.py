from core import settings


def project_3d_point_to_2d(point_3d, observer_distance):
    """
    This function will project 3d point on 2d point which can be draw on canvas.
    :param observer_distance: the length between observer and the canvas
    :param point_3d: tuple (x, y, z)
    :return point_2d: tuple (x, y)
    """
    p_2d_x = ((point_3d[0] * observer_distance) / (point_3d[2] + observer_distance))
    p_2d_y = ((point_3d[1] * observer_distance) / (point_3d[2] + observer_distance))

    return p_2d_x, p_2d_y


def point_2d_to_pixel_position(point_2d):
    """
    We must flip the y coordinate to gain not upside down image
    :param point_2d: (x, y)
    :return: pixel position (x, y)
    """
    return point_2d[0], settings.scree_height - point_2d[1]

