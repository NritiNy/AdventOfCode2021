import numpy as np
from typing import List
    
def part1(lines: List[str]):
    fold_idx = 0
    points = []

    for i, line in enumerate(lines):
        if len(line) > 0:
            points.append(line.split(","))
            continue
        fold_idx = i+1
        break

    points = np.asarray(points, dtype=int)
    x_max = np.max(points[:, 0]) 
    y_max = np.max(points[:, 1])

    matrix = np.zeros((y_max+1, x_max+1))
    for p in points[:]:
        matrix[p[1], p[0]] = 1

    instruction = lines[fold_idx].split(" ")[-1]
    axis, value = instruction.split("=")
    value = int(value)

    if axis == "y":
        top = matrix[:value,:]
        bottom = matrix[value+1:,:]
        
        matrix = 1 * (top + np.flip(bottom, 0) >= 1)
    else:
        left = matrix[:, :value]
        right = matrix[:, value+1:]

        matrix = 1 * (left + np.flip(right, 1) >= 1)

    return np.sum(matrix)

def part2(lines: List[str]):
    fold_idx = 0
    points = []

    for i, line in enumerate(lines):
        if len(line) > 0:
            points.append(line.split(","))
            continue
        fold_idx = i+1
        break
    points = np.asarray(points, dtype=int)

    x_max = np.max(points[:, 0]) 
    y_max = np.max(points[:, 1])

    matrix = np.zeros((y_max+1, x_max+1))
    for p in points[:]:
        matrix[p[1], p[0]] = 1

    for instruction in lines[fold_idx:]:
        instruction = instruction.split(" ")[-1]
        axis, value = instruction.split("=")
        value = int(value)

        if axis == "y":
            top = matrix[:value,:]
            bottom = matrix[value+1:,:]
            
            matrix = 1 * (top + np.flip(bottom, 0) >= 1)
        else:
            left = matrix[:, :value]
            right = matrix[:, value+1:]

            matrix = 1 * (left + np.flip(right, 1) >= 1)

    for line in matrix[:]:
        print("".join("#" if x == 1 else " " for x in line))
    return -1