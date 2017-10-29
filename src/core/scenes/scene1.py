from ..objects.cuboid import Cuboid


class Scene:
    available_objects = []

    def add_object(self, object_to_add):
        self.available_objects.append(object_to_add)


def build_scene():

    scene = Scene()
    tower_1 = Cuboid(10, 10, 10, start_point=(20, 20, 0))
    tower_2 = Cuboid(10, 10, 10, start_point=(40, 20, 0))
    tower_3 = Cuboid(10, 10, 20, start_point=(20, 40, 0))
    tower_4 = Cuboid(10, 10, 20, start_point=(40, 40, 0))
    tower_5 = Cuboid(10, 10, 40, start_point=(20, 70, 0))
    tower_6 = Cuboid(10, 10, 40, start_point=(40, 70, 0))

    scene.add_object(tower_1)
    scene.add_object(tower_2)
    scene.add_object(tower_3)
    scene.add_object(tower_4)
    scene.add_object(tower_5)
    scene.add_object(tower_6)
