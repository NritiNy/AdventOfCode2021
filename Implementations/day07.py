import numpy as np
from typing import List
    
def part1(lines: List[str]):
    positions = np.asarray([int(n) for n in lines[0].split(",")])

    sums = [np.sum(np.abs(positions - i)) for i in range(np.min(positions), np.max(positions))]

    return np.min(sums)

def part2(lines: List[str]):
    positions = np.asarray([int(n) for n in lines[0].split(",")])

    sums = [np.sum([n*(n+1)/2 for n in np.abs(positions - i)], dtype=int) for i in range(np.min(positions), np.max(positions))]

    return np.min(sums)