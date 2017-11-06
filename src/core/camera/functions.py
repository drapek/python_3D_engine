from core import settings


def project_3d_point_to_2d(point_3d, observer_distance):
    """
    This function will project 3d point on 2d point which can be draw on canvas.
    :param observer_distance: the length between observer and the canvas
    :param point_3d: tuple (x, y, z)
    :return point_2d: tuple (x, y)
    """

    screen_center_vertical = settings.scree_height / 2
    screen_center_horizontal = settings.scree_width / 2
    p_2d_x = screen_center_horizontal + ((point_3d[0] * observer_distance) / (point_3d[2] + observer_distance))
    p_2d_y = screen_center_vertical + ((point_3d[1] * observer_distance) / (point_3d[2] + observer_distance))
    p_2d_z = (())

    # We must flip the y coordinate to gain not upside down image
    p_2d_y = settings.scree_height - p_2d_y

    return p_2d_x, p_2d_y
