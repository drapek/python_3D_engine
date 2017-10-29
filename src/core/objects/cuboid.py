class Cuboid:

    def __init__(self, width, deep, height, start_point=(0, 0, 0)):
        self.corner1 = start_point
        self.corner2 = (start_point[0] + width, start_point[1], start_point[2])
        self.corner3 = (start_point[0] + width, start_point[1] + deep, start_point[2])
        self.corner4 = (start_point[0], start_point[1] + deep, start_point[2])
        self.corner5 = (start_point[0], start_point[1], start_point[2] + height)
        self.corner6 = (start_point[0] + width, start_point[1], start_point[2] + height)
        self.corner7 = (start_point[0] + width, start_point[1] + deep, start_point[2] + height)
        self.corner8 = (start_point[0], start_point[1] + deep, start_point[2] + height)

    def draw(self):
        # TODO implement it!
        pass
