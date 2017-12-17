import numpy as np

import settings
from camera.functions import move, rotate_x, rotate_y, rotate_z, rotate_one_point_x, rotate_one_point_y


class Scene:
    observer_to_canvas_dist = 300
    available_objects = []
    available_basic_polygons = []

    def __init__(self, light_source):
        self.light_source = light_source

    def add_object(self, object_to_add):
        self.available_objects.append(object_to_add)
        self.available_basic_polygons.extend(object_to_add.child_polygons)

    def draw_scene_in_2d(self, screen):
        """
        This function should translate scene coordinates to the camera coordinates, and
        project it to 2D image.
        :return:
        """
        # print('debug')  # TODO debug only
        # sort the triangles by it's 'z' coordinate in descending order. (Painter's algorithm)
        self.available_basic_polygons.sort(key=lambda x: np.mean(x.get_z_cords()), reverse=True)
        for polygon in self.available_basic_polygons:
            polygon.draw(screen, self.observer_to_canvas_dist, self.light_source,
                         show_edges=settings.sub_triangs_line_visible)

    def move_objects_on_scene(self, vector_3d):
        for scene_obj in self.available_objects:
            move(scene_obj, vector_3d)

    def rotate_x_objects_on_scene(self, angle):
        for scene_obj in self.available_objects:
            rotate_x(scene_obj, angle)

    def rotate_y_objects_on_scene(self, angle):
        for scene_obj in self.available_objects:
            rotate_y(scene_obj, angle)

    def rotate_z_objects_on_scene(self, angle):
        for scene_obj in self.available_objects:
            rotate_z(scene_obj, angle)

    def change_camera_zoom(self, step):
        self.observer_to_canvas_dist += step

    def rotate_light_x(self, angle):
        rotate_one_point_x(self.light_source.position, angle)

    def rotate_light_y(self, angle):
        rotate_one_point_y(self.light_source.position, angle)
