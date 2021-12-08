import numpy as np
from typing import List
    
def part1(lines: List[str]):
    segments = []
    for line in lines:
        p1, p2 = line.split(" -> ")
        x1, y1 = (int(n) for n in  p1.split(","))
        x2, y2 = (int(n) for n in  p2.split(","))

        segments.append(np.asarray([[x1, y1], [x2, y2]]))

    _max, _min =  np.max(segments), np.min(segments)
    diff = abs(_min - _max)
    matrix = np.zeros((diff + 1, diff + 1))

    for line in segments:
        x1, y1, x2, y2 = (n - _min for n in line.flatten())

        if not (x1 == x2 or y1 == y2):
            continue

        x_dir = np.sign(x2 - x1)
        y_dir = np.sign(y2 - y1)

        curr_x = x1
        curr_y = y1
        while not (curr_x, curr_y) == (x2, y2):
            matrix[curr_y, curr_x] += 1

            curr_x += x_dir
            curr_y += y_dir
        matrix[curr_y, curr_x] += 1

    tmp = np.zeros(matrix.shape)
    tmp[np.where(matrix > 1)] = 1
    return int(np.sum(tmp))

def part2(lines: List[str]):
    segments = []
    for line in lines:
        p1, p2 = line.split(" -> ")
        x1, y1 = (int(n) for n in  p1.split(","))
        x2, y2 = (int(n) for n in  p2.split(","))

        segments.append(np.asarray([[x1, y1], [x2, y2]]))

    _max, _min =  np.max(segments), np.min(segments)
    diff = abs(_min - _max)
    matrix = np.zeros((diff + 1, diff + 1))

    for line in segments:
        x1, y1, x2, y2 = (n - _min for n in line.flatten())

        x_dir = np.sign(x2 - x1)
        y_dir = np.sign(y2 - y1)

        curr_x = x1
        curr_y = y1
        while not (curr_x, curr_y) == (x2, y2):
            matrix[curr_y, curr_x] += 1

            curr_x += x_dir
            curr_y += y_dir
        matrix[curr_y, curr_x] += 1

    tmp = np.zeros(matrix.shape)
    tmp[np.where(matrix > 1)] = 1
    return int(np.sum(tmp))