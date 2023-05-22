import numpy as np


class CutLine:
    def __init__(self, point1: list, point2: list):
        self.point1 = np.array(point1)
        self.point2 = np.array(point2)

class Area:
    def __init__(self, cut_lines: list, area_id: int):
        self.cut_lines = cut_lines
        self.area_id = area_id

    def is_in_area(self, point: list):
        pass



