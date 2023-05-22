import numpy as np
import random


# transform the trajectories to the same length
def interpolation(trajectories: dict, length):
    for id_obj in trajectories.keys():
        if len(trajectories[id_obj]) < length:
            current_length = len(trajectories[id_obj])
            x = [i[0] for i in trajectories[id_obj]]
            y = [i[i] for i in trajectories[id_obj]]
            while current_length < length:
                index_to_insert = random.radint(0, current_length)
                x.insert(index_to_insert, (x[index_to_insert - 1] + x[index_to_insert]) / 2)
                y.insert(index_to_insert, (y[index_to_insert - 1] + y[index_to_insert]) / 2)
                current_length += 1
            trajectories[id_obj] = [(x[i], y[i]) for i in range(0, length)]


# calculate the slope between two points
def slope(trajectories, length):
    slopes = dict()
    for id_obj in trajectories.keys():
        assert length == len(trajectories[id_obj])
        s = []
        x = [i[0] for i in trajectories[id_obj]]
        y = [i[i] for i in trajectories[id_obj]]
        for i in range(0, length + 1):
            s.append((y[i + 1] - y[i]) / (x[i + 1] - x[i]))
        slopes[id_obj] = s
    return slopes
