import numpy as np
from typing import List
    
def part1(lines: List[str]):
    levels = np.asarray([[int(x) for x in line] for line in lines], dtype=int)

    amount_flashes = 0
    for _ in range(100):
        levels = levels + 1
        flashing = levels > 9

        flashed = flashing
        while np.any(flashing):
            for y in range(flashing.shape[0]):
                for x in range(flashing.shape[1]):
                    if flashing[y, x]:
                        levels[max(0, y-1):min(y+2,flashing.shape[0]),max(0, x-1):min(flashing.shape[1], x+2)] += 1
            
            levels[flashing] = 0
            flashed += flashing
            flashing = levels > 9
        
        amount_flashes += np.sum(1 * flashed)
        levels[flashed] = 0      

    return amount_flashes

def part2(lines: List[str]):
    levels = np.asarray([[int(x) for x in line] for line in lines], dtype=int)

    step = 0
    while True:
        levels = levels + 1
        flashing = levels > 9

        flashed = flashing
        while np.any(flashing):
            for y in range(flashing.shape[0]):
                for x in range(flashing.shape[1]):
                    if flashing[y, x]:
                        levels[max(0, y-1):min(y+2,flashing.shape[0]),max(0, x-1):min(flashing.shape[1], x+2)] += 1
            
            levels[flashing] = 0
            flashed += flashing
            flashing = levels > 9

        levels[flashed] = 0
        amount_flashes = np.sum(1 * flashed)
        step += 1
        if amount_flashes == levels.shape[0] * levels.shape[1]:
            return step
        