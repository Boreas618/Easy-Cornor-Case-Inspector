import json
import datetime


def load_data():
    # read the the json files
    data: list = []
    for i in range(0, 1):
        with open(f'data/{i}.json', 'r') as f:
            # read the file line by line and append to data
            while True:
                line = f.readline()
                if not line:
                    break
                data.append(json.loads(line))
    data.sort(key=lambda x: x['time_meas'])
    return data


def filter_trajectory(data:list, is_in_area, lower_bound=10000, upper_bound=-1):
    trajectories = dict()
    for item in data:
        position = json.loads(item['position'])
        x = position['x']
        y = position['y']

        if is_in_area([x, y]) is False:
            continue

        if trajectories.get(item['id']) is None:
            trajectories[item['id']] = [(x, y)]
        else:
            trajectories[item['id']].append((x, y))

    filtered_trajectories = dict()
    for i in trajectories.keys():
        if len(trajectories[i]) > upper_bound or len(trajectories[i]) < lower_bound:
            continue
        filtered_trajectories[i] = trajectories[i]

    return filtered_trajectories
