class Scene:
    observer_to_canvas_dist = 300
    available_objects = []

    def add_object(self, object_to_add):
        self.available_objects.append(object_to_add)

    def draw_scene_in_2d(self, screen):
        """
        This function should translate scene coordinates to the camera coordinates, and
        project it to 2D image.
        :return:
        """
        for scene_obj in self.available_objects:
            scene_obj.draw_on_screen(screen, self.observer_to_canvas_dist)

    def move_objects_on_scene(self, vector_3d):
        for scene_obj in self.available_objects:
            scene_obj.move(vector_3d)

    def rotate_x_objects_on_scene(self, angle):
        for scene_obj in self.available_objects:
            scene_obj.rotate_x(angle)

    def rotate_y_objects_on_scene(self, angle):
        for scene_obj in self.available_objects:
            scene_obj.rotate_y(angle)

    def rotate_z_objects_on_scene(self, angle):
        for scene_obj in self.available_objects:
            scene_obj.rotate_z(angle)

    def change_camera_zoom(self, step):
        self.observer_to_canvas_dist += step
