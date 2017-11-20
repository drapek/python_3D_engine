from camera.functions import move, rotate_x, rotate_y, rotate_z


class Scene:
    observer_to_canvas_dist = 300
    available_objects = []
    available_basic_triangles = []

    def add_object(self, object_to_add):
        self.available_objects.append(object_to_add)
        self.available_basic_triangles.extend(object_to_add.child_triangles)

    def draw_scene_in_2d(self, screen):
        """
        This function should translate scene coordinates to the camera coordinates, and
        project it to 2D image.
        :return:
        """
        # TODO @Adam: In self.available_basic_triangles you will find all triangles - sort them! :)
        # TODO sort the triangles using central point z coordinate
        for triangle in self.available_basic_triangles:
            triangle.draw(screen, self.observer_to_canvas_dist)

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
