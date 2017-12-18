import numpy as np


class Light:
    position = None
    min_light = None
    max_light = None
    light_range = None

    def __init__(self, light_position=None, min_light=0.1, max_light=0.7):
        if light_position is None:
            light_position = [-0.62, 0.12, -1.52]

        self.position = light_position
        self.min_light = min_light
        self.max_light = max_light
        self.light_range = max_light - min_light

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
                    shade = (theta * self.light_range + self.min_light) * np.array(polygon.color)

                if max(shade) > 255:
                    shade = list(map(lambda x: 255 if x > 255 else x, shade))
                return shade
            else:
                return None
        except Exception as e:
            print(e)
            return 0, 0, 0

