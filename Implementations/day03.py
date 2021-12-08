import numpy as np
from typing import List
    
def part1(lines: List[str]):
    gamma = ""
    epsilon = ""

    lines = np.asarray([[int(b) for b in line] for line in lines])
    sums = np.sum(lines, axis=0)
    length = lines.shape[0]

    for s in sums:
        if s > length / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2) * int(epsilon, 2)

def part2(lines: List[str]):
    oxygen = "0"
    co2 = "0"

    lines = np.asarray([[int(b) for b in line] for line in lines])
    o_lines = np.copy(lines)
    c_lines = np.copy(lines)

    column = 0
    while len(o_lines) > 1:
        sums = np.sum(o_lines, axis=0)
        criteria = 1 if sums[column] >= len(o_lines) / 2 else 0
        o_lines = [line for line in o_lines if line[column] == criteria]

        column += 1
    oxygen = "".join(str(n) for n in o_lines[0])

    column = 0
    while len(c_lines) > 1:
        sums = np.sum(c_lines, axis=0)
        criteria = 0 if sums[column] >= len(c_lines) / 2 else 1
        c_lines = [line for line in c_lines if line[column] == criteria]

        column += 1
    co2 = "".join(str(n) for n in c_lines[0])

    return int(oxygen, 2) * int(co2, 2)