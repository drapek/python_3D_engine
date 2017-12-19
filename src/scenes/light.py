import numpy as np


class Light:
    class Material:
        METAL = 0
        PLASTIC = 1
        CONCRETE = 2
        # first param is function of the light, second is brightness
        gloss_params = ((lambda x: x, 0.8),
                        (lambda x: 41 * x / 26 - 3825 / 26, 0.8),
                        (lambda x: pow(x / 66, 4), 0.8))
        actual_material = 0

        def __init__(self, material):
            if 0 <= material <= len(self.gloss_params):
                self.actual_material = material
            else:
                self.actual_material = self.METAL

        def next(self):
            self.actual_material += 1
            if self.actual_material >= len(self.gloss_params):
                self.actual_material = 0

        def calculate_gloss(self, original_shade):
            f = self.gloss_params[self.actual_material][0]
            return f(original_shade * self.gloss_params[self.actual_material][1])

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
            v1 = (np.array(polygon.nodes[0]) - np.array(polygon.nodes[2]))[:3]  # make two vectors for each polygon
            v2 = (np.array(polygon.nodes[1]) - np.array(polygon.nodes[2]))[:3]  # v1 and v2 says about the tale (polygon) orientation
            normal = np.cross(v1, v2)  # The vector as product of two vectors. Points direction of the tale
            towards_us = np.dot(normal, [0, 0, -1])  # Product of two arrays
            # Only draw faces that face us
            if towards_us > 0:
                normal /= np.linalg.norm(normal)  # It divides each cell by calculated linalg math norm. (In most cases it will be squared_norm = vector length)
                theta = np.dot(normal, self.position[:3])  # calculate if the factor of slope angle between polygon and the light source
                if theta < 0:
                    # if it is on the other side of the light source, set the minimal brightness
                    shade = self.min_light * np.array(polygon.color)
                else:
                    shade = self.actual_material.\
                        calculate_gloss((theta * self.light_range + self.min_light) * np.array(polygon.color))
                # Color can be build only from numbers 0 - 255. Filter the rest of it.
                if max(shade) > 255:
                    shade = list(map(lambda x: 255 if x > 255 else x, shade))
                if min(shade) < 0:
                    shade = list(map(lambda x: self.min_light if x < 0 else x, shade))
                return shade
            else:
                return None
        except Exception as e:
            print(e)
            return 0, 0, 0
