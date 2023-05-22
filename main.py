import json
import datetime
from area import Area, CutLine


class AreaA(Area):
    def __init__(self, cut_lines: list, area_id: int):
        super().__init__(cut_lines, area_id)

    def is_in_area(self, point: list):
        if self.cut_lines[0].point1[0] <= point[0] <= self.cut_lines[0].point2[0] and \
                point[1] <= min(self.cut_lines[0].point1[1], self.cut_lines[0].point2[1]):
            return True
        return False


if __name__ == '__main__':
    # read the the json files
    data: list = []
    for i in range(0, 1):
        with open(f'./data/{i}.json', 'r') as f:
            # read the file line by line and append to data
            while True:
                line = f.readline()
                if not line:
                    break
                data.append(json.loads(line))

    data.sort(key=lambda x: x['time_meas'])

    area_a = AreaA([CutLine([-100, -210], [-60, -230])], 1)
    trajectory = dict()
    time = dict()

    for item in data:
        position = json.loads(item['position'])
        x = position['x']
        y = position['y']

        if not area_a.is_in_area([x, y]):
            continue

        if trajectory.get(item['id']) is None:
            trajectory[item['id']] = [(x, y)]
        else:
            trajectory[item['id']].append((x, y))

        if time.get(item['id']) is None:
            # get the time and convert it from UNIX timestamp to datetime
            utc_time = datetime.datetime.utcfromtimestamp(item['time_meas'] / 1000000)
            time[item['id']] = [utc_time]
        else:
            utc_time = datetime.datetime.utcfromtimestamp(item['time_meas'] / 1000000)
            time[item['id']].append(utc_time)

    count_child_set_1 = 0
    count_child_set_2 = 0
    count = 0

    for i in trajectory.keys():
        if len(trajectory[i]) < 10:
            count_child_set_1 += 1
        if 10 <= len(trajectory[i]) <= 100:
            count_child_set_2 += 1
        count += 1

    print(count_child_set_1 / count)
    print(count_child_set_2 / count)
    print(count)


