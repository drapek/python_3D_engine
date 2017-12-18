import numpy as np


class Light:
    class Material:
        METAL = 0
        PLASTIC = 1
        CONCRETE = 2
        gloss_functions = (lambda x: x,
                           lambda x: pow(x / 66, 4),
                           lambda x: 41 * x / 26 - 3825 / 26)
        gloss_brightness = (0.9,
                            0.7,
                            0.6)
        # TODO repair the brightness and functions to fit each others
        actual_material = 0

        def __init__(self, material):
            if 0 <= material <= len(self.gloss_functions):
                self.actual_material = material
            else:
                self.actual_material = self.METAL

        def next(self):
            self.actual_material += 1
            if self.actual_material >= len(self.gloss_functions):
                self.actual_material = 0

        def calculate_gloss(self, original_shade):
            f = self.gloss_functions[self.actual_material]
            return f(original_shade * self.gloss_brightness[self.actual_material])

    position = None
    min_light = None
    max_light = None
    light_range = None

    def __init__(self, light_position=None, min_light=0.1, max_light=1, actual_material=Material(Material.METAL)):
        if light_position is None:
            light_position = [-0.62, 0.12, -1.52]

        self.position = light_position
        self.min_light = min_light
        self.max_light = max_light
        self.light_range = max_light - min_light
        self.actual_material = actual_material

    def calculate_lighting(self, polygon):
        try:
            v1 = (np.array(polygon.nodes[0]) - np.array(polygon.nodes[2]))[:3]
            v2 = (np.array(polygon.nodes[1]) - np.array(polygon.nodes[2]))[:3]
            normal = np.cross(v1, v2)
            towards_us = np.dot(normal, [0, 0, -1])
            # Only draw faces that face us
            if towards_us > 0:
                normal /= np.linalg.norm(normal)
                theta = np.dot(normal, self.position[:3])
                if theta < 0:
                    shade = self.min_light * np.array(polygon.color)
                else:
                    # TODO here should be some kind of function
                    shade = self.actual_material.\
                        calculate_gloss((theta * self.light_range + self.min_light) * np.array(polygon.color))

                if max(shade) > 255:
                    shade = list(map(lambda x: 255 if x > 255 else x, shade))
                return shade
            else:
                return None
        except Exception as e:
            print(e)
            return 0, 0, 0
